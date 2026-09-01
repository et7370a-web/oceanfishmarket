"""
Generate a consistent whole-fish photo set for sections/shop-by-species.liquid.

Backends:
  gemini  (default, free tier)  -- model gemini-2.5-flash-image ("Nano Banana")
                                   key: .gemini_key  or  GEMINI_API_KEY
                                   get one free at https://aistudio.google.com/apikey
  openai                        -- model gpt-image-1 (paid)
                                   key: .oai_key  or  OPENAI_API_KEY

Usage:
  python scripts/generate-species-photos.py                    # all 16, gemini
  python scripts/generate-species-photos.py salmon tuna        # just those
  python scripts/generate-species-photos.py --backend openai
  python scripts/generate-species-photos.py --dorado mahi      # gilthead (default) | mahi
"""
import base64, io, os, sys, time
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
RAW = ROOT / "_species_raw"          # git-ignored, keeps the full-res originals
RAW.mkdir(exist_ok=True)

STYLE = (
    "Commercial food photography of ONE whole raw {fish}, whole and uncut, lying "
    "flat in left-facing side profile on a shallow bed of crushed ice. Seamless "
    "pale blue-grey studio background (#eef5f8). Bright, even, soft diffused top "
    "light with gentle front fill, no harsh shadows, no color cast. Camera straight "
    "on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish "
    "spans about 80% of the frame width and is centered, framed in landscape 4:3. "
    "Fresh and glistening, clear bright eye, natural realistic color. No hands, no "
    "props, no garnish, no packaging, no text or watermark. Sharp focus, high detail."
)

FISH = {
    "salmon":      ("species-salmon.jpg",      "salmon with a blue-silver back fading to a bright silver belly and faint small black spots on the upper body"),
    "tuna":        ("species-tuna.jpg",         "small tuna with a torpedo shape, dark metallic blue back, silver flanks, and small finlets before the tail"),
    "branzino":    ("species-branzino.jpg",    "branzino (European sea bass) with a slender bright silver body, a single spiny dorsal fin, and a small pointed head"),
    "snapper":     ("species-snapper.jpg",     "red snapper with rosy pinkish-red skin and fins, a sloped forehead, a pointed snout and a reddish eye"),
    "grouper":     ("species-grouper.jpg",     "grouper with a stout mottled brown-grey body, a very large mouth and thick rounded fins"),
    "cod":         ("species-cod.jpg",         "Atlantic cod with an olive-brown speckled body, a pale curved lateral line, a small chin barbel and three dorsal fins"),
    "halibut":     ("species-halibut.jpg",     "halibut, a large elongated flatfish with both eyes on the dark grey-brown upper side and a narrow diamond-shaped body"),
    "flounder":    ("species-flounder.jpg",    "flounder, a smaller oval flatfish with a brown mottled upper side and faint darker spots"),
    "tilefish":    ("species-tilefish.webp",    "golden tilefish with a long blue-grey body flecked with yellow-gold, a fleshy ridge on the head and yellow markings on the face"),
    "whiting":     ("species-whiting.webp",     "whiting with a slim silvery body, a faint golden lateral tint, a small head and a forked tail"),
    "mullet":      ("species-mullet.webp",      "grey mullet with a torpedo body, silver with faint horizontal grey stripes, a blunt rounded head and two separate dorsal fins"),
    "buffalofish": ("species-buffalofish.webp", "buffalo fish with a heavy deep bronze-grey body, large coarse scales, a high arched back and a small downturned mouth"),
    "carp":        ("species-carp.jpg",        "common carp with large golden-brown scales, a thick body, two short barbels at the mouth corners and orange-tinged lower fins"),
    "dorado":      ("species-dorado.webp",      None),  # filled from --dorado
    "tilapia":     ("species-tilapia.webp",     "tilapia with a deep compact grey body, faint vertical bars, a long spiny dorsal fin and a rounded snout"),
    "graysole":    ("species-graysole.webp",    "gray sole (witch flounder), a slender oval flatfish with an even grey-brown upper side and a very small mouth"),
}
DORADO = {
    "gilthead": "gilt-head bream with an oval silver body, a golden band between the eyes and a small dark spot by the gill cover",
    "mahi":     "mahi-mahi (dorado) with a bright green-gold body and a steep blunt forehead",
}


def read_key(fname, envvar):
    f = ROOT / fname
    if f.exists():
        return f.read_text(encoding="utf-8").strip()
    if os.environ.get(envvar):
        return os.environ[envvar].strip()
    sys.exit(f"No API key. Put it in {fname} (project root) or set {envvar}.")


def gen_gemini(prompt):
    from google import genai
    client = getattr(gen_gemini, "_c", None)
    if client is None:
        client = genai.Client(api_key=read_key(".gemini_key", "GEMINI_API_KEY"))
        gen_gemini._c = client
    resp = client.models.generate_content(
        model="gemini-2.5-flash-image", contents=prompt
    )
    for part in resp.candidates[0].content.parts:
        if getattr(part, "inline_data", None) and part.inline_data.data:
            return part.inline_data.data
    raise RuntimeError("no image in Gemini response: " + str(resp))


def gen_openai(prompt):
    from openai import OpenAI
    client = getattr(gen_openai, "_c", None)
    if client is None:
        client = OpenAI(api_key=read_key(".oai_key", "OPENAI_API_KEY"))
        gen_openai._c = client
    r = client.images.generate(
        model="gpt-image-1", prompt=prompt, size="1536x1024", quality="high", n=1
    )
    return base64.b64decode(r.data[0].b64_json)


def finish(img_bytes, out_name):
    im = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    im = ImageOps.fit(im, (1200, 900), method=Image.LANCZOS, centering=(0.5, 0.5))
    out = ASSETS / out_name
    if out.suffix.lower() in (".jpg", ".jpeg"):
        im.save(out, "JPEG", quality=90, optimize=True)
    else:
        im.save(out, "WEBP", quality=90, method=6)
    print(f"  saved {out.relative_to(ROOT)}  {out.stat().st_size // 1024} KB")


def main():
    args = sys.argv[1:]
    backend, dorado, picks = "gemini", "gilthead", []
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--backend":
            backend = args[i + 1]; i += 2; continue
        if a == "--dorado":
            dorado = args[i + 1]; i += 2; continue
        picks.append(a); i += 1

    gen = {"gemini": gen_gemini, "openai": gen_openai}[backend]
    FISH["dorado"] = (FISH["dorado"][0], DORADO[dorado])
    todo = picks or list(FISH)

    for name in todo:
        if name not in FISH:
            print(f"skip unknown: {name}"); continue
        out_name, desc = FISH[name]
        prompt = STYLE.format(fish=desc)
        print(f"[{name}] {backend} generating...")
        t0 = time.time()
        for attempt in range(3):
            try:
                data = gen(prompt)
                break
            except Exception as e:
                print(f"  retry {attempt + 1}: {e}")
                time.sleep(8 * (attempt + 1))
        else:
            print(f"  FAILED {name}"); continue
        (RAW / f"{name}.png").write_bytes(data)
        finish(data, out_name)
        print(f"  {time.time() - t0:.0f}s")
        time.sleep(2)  # be gentle on free-tier rate limits


if __name__ == "__main__":
    main()
