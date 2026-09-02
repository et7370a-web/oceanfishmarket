"""
Normalize hand-generated fish photos into assets/.

Drop downloads into  _species_inbox/  named by key (salmon.png, tuna.jpg, ...).
Then:  python scripts/import-species-photos.py

Each file is cropped to 4:3, resized to 1200x900, and written to assets/ under
the filename the section expects. Original drops are left in _species_inbox/.
"""
import sys
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "_species_inbox"
ASSETS = ROOT / "assets"

# key -> asset filename that sections/shop-by-species.liquid references
DEST = {
    "salmon": "species-salmon.jpg",
    "tuna": "species-tuna.jpg",
    "branzino": "species-branzino.jpg",
    "snapper": "species-snapper.jpg",
    "grouper": "species-grouper.jpg",
    "cod": "species-cod.jpg",
    "halibut": "species-halibut.jpg",
    "flounder": "species-flounder.jpg",
    "tilefish": "species-tilefish.jpg",
    "whiting": "species-whiting.jpg",
    "mullet": "species-mullet.jpg",
    "buffalofish": "species-buffalofish.jpg",
    "carp": "species-carp.jpg",
    "dorado": "species-dorado.jpg",
    "tilapia": "species-tilapia.jpg",
    "graysole": "species-graysole.jpg",
}
EXTS = (".png", ".jpg", ".jpeg", ".webp")

if not INBOX.exists():
    sys.exit(f"no {INBOX.relative_to(ROOT)}/ folder - create it and add the downloads")

found = 0
for key, dest in DEST.items():
    src = next((INBOX / f"{key}{e}" for e in EXTS if (INBOX / f"{key}{e}").exists()), None)
    if not src:
        continue
    found += 1
    im = Image.open(src).convert("RGB")
    im = ImageOps.fit(im, (1200, 900), method=Image.LANCZOS, centering=(0.5, 0.5))
    out = ASSETS / dest
    if out.suffix.lower() in (".jpg", ".jpeg"):
        im.save(out, "JPEG", quality=90, optimize=True)
    else:
        im.save(out, "WEBP", quality=90, method=6)
    print(f"  {src.name:20s} -> assets/{dest}  ({out.stat().st_size // 1024} KB)")

missing = [k for k in DEST if not any((INBOX / f"{k}{e}").exists() for e in EXTS)]
print(f"\nimported {found}/16")
if missing:
    print("still missing:", ", ".join(missing))
