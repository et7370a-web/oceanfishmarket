# Species photos — Google AI Studio (manual)

Generate 16 images that look like one shoot: same angle, light, surface, framing.
Only the fish changes.

## Steps
1. Go to **aistudio.google.com** → new chat → set the model to an **image
   generation** one (e.g. "Nano Banana" / Gemini 2.5 Flash Image).
2. For each fish below, paste the whole block as the prompt. Generate.
   If the result looks wrong (wrong species, extra fins, cut in half, dark
   background), say "try again, <fix>" or re-run.
3. Download each image. Put them all in a folder named **`_species_inbox/`** in
   the project root, named just by the key: `salmon.png`, `tuna.png`,
   `branzino.png`, … (png or jpg, whatever it gives you).
4. Tell me — I run `python scripts/import-species-photos.py`, which crops each to
   4:3, resizes, and drops it into `assets/` with the right filename. The section
   already points at those filenames, so nothing else to change.

Keys (folder filename → what it becomes):
salmon, tuna, branzino, snapper, grouper, cod, halibut, flounder, tilefish,
whiting, mullet, buffalofish, carp, dorado, tilapia, graysole

---

### salmon
Commercial food photography of ONE whole raw salmon, whole and uncut, lying flat in left-facing side profile on a shallow bed of crushed ice. The salmon has a blue-silver back fading to a bright silver belly with faint small black spots on the upper body. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### tuna
Commercial food photography of ONE whole raw small tuna, whole and uncut, lying flat in left-facing side profile on a shallow bed of crushed ice. The tuna has a torpedo shape, a dark metallic blue back, silver flanks, and small finlets before the tail. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### branzino
Commercial food photography of ONE whole raw branzino (European sea bass), whole and uncut, lying flat in left-facing side profile on a shallow bed of crushed ice. The branzino has a slender bright silver body, a single spiny dorsal fin, and a small pointed head. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### snapper
Commercial food photography of ONE whole raw red snapper, whole and uncut, lying flat in left-facing side profile on a shallow bed of crushed ice. The red snapper has rosy pinkish-red skin and fins, a sloped forehead, a pointed snout, and a reddish eye. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### grouper
Commercial food photography of ONE whole raw grouper, whole and uncut, lying flat in left-facing side profile on a shallow bed of crushed ice. The grouper has a stout mottled brown-grey body, a very large mouth, and thick rounded fins. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### cod
Commercial food photography of ONE whole raw Atlantic cod, whole and uncut, lying flat in left-facing side profile on a shallow bed of crushed ice. The cod has an olive-brown speckled body, a pale curved lateral line, a small chin barbel, and three dorsal fins. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### halibut
Commercial food photography of ONE whole raw halibut, whole and uncut, lying flat with the dark side up in left-facing profile on a shallow bed of crushed ice. The halibut is a large elongated flatfish with both eyes on the dark grey-brown upper side and a narrow diamond-shaped body. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight above the fish, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### flounder
Commercial food photography of ONE whole raw flounder, whole and uncut, lying flat with the dark side up in left-facing profile on a shallow bed of crushed ice. The flounder is a smaller oval flatfish with a brown mottled upper side and faint darker spots. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight above the fish, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### tilefish
Commercial food photography of ONE whole raw golden tilefish, whole and uncut, lying flat in left-facing side profile on a shallow bed of crushed ice. The tilefish has a long blue-grey body flecked with yellow-gold, a fleshy ridge on the head, and yellow markings on the face. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### whiting
Commercial food photography of ONE whole raw whiting, whole and uncut, lying flat in left-facing side profile on a shallow bed of crushed ice. The whiting has a slim silvery body with a faint golden lateral tint, a small head, and a forked tail. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### mullet
Commercial food photography of ONE whole raw grey mullet, whole and uncut, lying flat in left-facing side profile on a shallow bed of crushed ice. The grey mullet has a torpedo body, silver with faint horizontal grey stripes, a blunt rounded head, and two separate dorsal fins. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### buffalofish
Commercial food photography of ONE whole raw buffalo fish, whole and uncut, lying flat in left-facing side profile on a shallow bed of crushed ice. The buffalo fish has a heavy deep bronze-grey body, large coarse scales, a high arched back, and a small downturned mouth. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### carp
Commercial food photography of ONE whole raw common carp, whole and uncut, lying flat in left-facing side profile on a shallow bed of crushed ice. The carp has large golden-brown scales, a thick body, two short barbels at the mouth corners, and orange-tinged lower fins. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### dorado  — PICK ONE, delete the other
(gilt-head bream) Commercial food photography of ONE whole raw gilt-head bream, whole and uncut, lying flat in left-facing side profile on a shallow bed of crushed ice. It has an oval silver body, a golden band between the eyes, and a small dark spot by the gill cover. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

(mahi-mahi) Commercial food photography of ONE whole raw mahi-mahi, whole and uncut, lying flat in left-facing side profile on a shallow bed of crushed ice. It has a bright green-gold body and a steep blunt forehead. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### tilapia
Commercial food photography of ONE whole raw tilapia, whole and uncut, lying flat in left-facing side profile on a shallow bed of crushed ice. The tilapia has a deep compact grey body with faint vertical bars, a long spiny dorsal fin, and a rounded snout. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight on the side of the fish, about 10 degrees above horizontal, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

### graysole
Commercial food photography of ONE whole raw gray sole (witch flounder), whole and uncut, lying flat with the grey-brown side up in left-facing profile on a shallow bed of crushed ice. It is a slender oval flatfish with an even grey-brown upper side and a very small mouth. Seamless pale blue-grey studio background. Bright, even, soft diffused top light with gentle front fill, no harsh shadows, no color cast. Camera straight above the fish, 50mm lens, the fish spans about 80% of the frame width and is centered, landscape 4:3. Fresh and glistening, clear bright eye, natural realistic color. No hands, no props, no garnish, no packaging, no text or watermark. Sharp focus, high detail.

---

## Notes
- Eyeball each against a real reference image of that species — generators
  sometimes blend species or add fins.
- AI Studio images are fine for commercial use; there's a small invisible
  SynthID watermark, which is fine for a storefront.
