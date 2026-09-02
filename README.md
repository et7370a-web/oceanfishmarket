# Ocean Fish BH

Shopify theme for Ocean Fish BH, built on top of [Shopify's Dawn theme](https://github.com/Shopify/dawn). Theme code (Liquid, CSS, JS) lives here in GitHub; Shopify pulls from this repo to deploy the storefront.

Branding and copy are pulled from the existing [oceanfishmarketbh.lovable.app](https://preview--oceanfishmarketbh.lovable.app) site: New York's premium wild-caught fish market, family operated, founder Slavik, three retail locations plus a wholesale operation, 24-hour delivery to NYC/Long Island/NJ, open Sunday–Thursday (closed Friday/Saturday), Kosher certified. Order questions: (646) 750-9232.

See [DAWN-REFERENCE.md](./DAWN-REFERENCE.md) for Dawn's original docs (theme structure, developer tools, staying in sync with upstream Dawn changes).

## Project setup status

- [x] Theme code initialized from Dawn
- [x] Branding pass: palette matched to the existing site (navy `#0B2A45` + teal `#229E97` + gold `#C9A227`), real hero copy, trust badges, header/footer
- [x] "Our Story", "Shipping", and "Contact" pages matching the real site's content
- [x] Catalog simplified to one model: every product is a whole fish, $9.99/lb, 5 lb minimum
- [x] Wholesale membership theme logic: gated pricing/add-to-cart, membership landing page, homepage sections
- [ ] GitHub repo created and this local repo pushed to it
- [ ] Shopify store connected to this GitHub repo (Online Store > Themes > Add theme > Connect from GitHub)
- [ ] Node.js + Shopify CLI installed locally for `shopify theme dev` live preview (optional but recommended)
- [ ] Real logo file and product photos (currently text wordmark + illustrated whole-fish icons — no image-generation tool is available here, so real photos need to come from you, including possibly the existing Lovable site's photography)
- [ ] Navigation menu (Home / Shop / Our Story / Shipping / Contact) — lives in Shopify Admin, not this repo, see below
- [ ] Admin-side setup for payments and membership — see below, none of this lives in the theme repo

## Branding

- **Colors:** navy `#0B2A45` (header nav is white/light instead — see note below — but hero photo overlay, footer, and dark sections use navy), teal `#229E97` (primary CTA buttons, matching "Shop Our Catch" on the real site), gold `#C9A227` (badges, sale tags, accents — matching the real site's script-text and "Best Seller" badge). Defined in `config/settings_data.json` under `color_schemes` (scheme-1 through scheme-5) — adjustable live in the Shopify theme editor under Theme settings > Colors, no code changes needed.
- **Logo:** the real site has a designed two-line "OCEAN / FISH BH" logo with an icon — send the logo file (SVG/PNG) and I'll wire it into Theme settings > Logo. Until then the header falls back to the store's name as a text wordmark, which only reads "Ocean Fish BH" once the actual Shopify store is named that.
- **Images:** the homepage's "Our market" and "Shop by type" sections use hand-drawn SVG placeholders (in `sections/our-market.liquid` and `sections/shop-by-species.liquid`) so the layout isn't empty. The real site has professional product photography (salmon fillets, market interior) — if you have the source image files, send them and I'll swap the placeholders and wire up real product images.

## Catalog model: every fish is whole, $9.99/lb

The catalog is one uniform line — every product is a whole fish, priced at $9.99/lb, 5 lb minimum per order (species can be mixed to hit the minimum). There's no separate "retail fillet" tier.

**Every product requires membership to order** — this is now enforced site-wide in the theme (not dependent on tagging individual products): everyone can see prices, but only customers tagged `member` can actually add to cart. Non-members see a "Join to order wholesale" prompt, plus a "Log in" link if they already have an account. A dedicated `/collections/wholesale` isn't needed; links throughout the theme point at `/collections/all`.

**How membership is "remembered":** this relies on Shopify's own customer accounts, not custom code. Once someone's account is tagged `member` (the Shopify Subscriptions app does this automatically when their subscription is active), the theme checks `customer.tags` on every page load — as long as they're logged in, Shopify's session cookie keeps them recognized across visits. Make sure customer accounts are enabled (Settings > Customer accounts) so members can actually log in.

`sections/shop-by-species.liquid` renders whole-fish photos for most species (salmon, tuna, branzino, red snapper, grouper, cod, halibut, flounder, whiting, tile fish, mullet, buffalo fish, carp, dorado, tilapia, gray sole) with an illustrated fallback for anything without a photo yet (currently Chilean Sea Bass isn't shown — send a photo and I'll add it back).

## Wholesale membership

The theme enforces membership gating, but **billing and tagging are Shopify Admin/app configuration — not code.** Here's what's built vs. what you still need to set up.

### Built into the theme

- `snippets/buy-buttons.liquid`: every product shows its price to everyone, but only checks out for customers tagged `member` — non-members see a "Join to order wholesale" card linking to `/pages/membership`, plus a "Log in" link if they're not signed in. Also shows a "5 lb minimum per order" note.
- `templates/page.membership.json`: a membership landing page (benefits, pricing, how it works) — publish it as a page with handle `membership` so it matches the links above.
- Homepage sections: hero (real copy, "Shop Our Catch" / "Our Story" buttons), trust badges (24-Hour Delivery / Wild Caught / 30+ Years Experience / Kosher Certified), membership CTA (near the top), species photo cards ($9.99/lb whole fish).
- `templates/page.our-story.json`: full founder story page — publish as a page with handle `our-story`.
- `templates/page.shipping.json` / `sections/shipping-info.liquid`: delivery-area and delivery-schedule cards matching the real Shipping page, plus a free-shipping-for-members note.
- `templates/page.contact.json`: intro copy + Dawn's native contact form (Name/Email/Phone/Message) — this is a real, working Shopify contact form, no extra setup needed beyond publishing the page.

## Navigation

Dawn's header pulls its menu from Shopify's own navigation data (Admin > Online Store > Navigation), not from this repo. To match the real site, create a menu named "Main menu" with: Home, Shop (→ `/collections/all`), Our Story (→ `/pages/our-story`), Shipping (→ `/pages/shipping`), Contact (→ `/pages/contact`) — publish those three pages first (see setup steps below) so the links resolve.

### You'll need to do in Shopify Admin

1. **Enable payments**: Settings > Payments — enable Shopify Payments or another provider. Required before any checkout works; involves your bank/business details, so this has to be you.
2. **Install the free Shopify Subscriptions app** (Shopify App Store) and create the membership product:
   - Handle it as `ocean-fish-market-membership` (or update the links in `templates/page.membership.json` and `snippets/buy-buttons.liquid` to match whatever handle you use).
   - Add two selling plans: monthly at $3.00, annual at $36.00.
   - In the app's settings, turn on auto-tagging so an active subscriber gets tagged `member` on their customer profile — this is what the theme checks to unlock checkout.
   - Enable customer accounts (Settings > Customer accounts) so members can log in and be recognized.
3. **Create products** (every one a whole fish): price at $9.99/lb (sold by weight, or list per-lb and let quantity = pounds), and set each variant's quantity rule to **minimum 5, increment 1** (Admin > product > variant > "This item has quantity rules") so 5 lb is enforced at checkout. No special tag needed — every product is gated by default now.
4. **Free shipping for members**: Admin > Discounts > create an automatic discount, 100% off shipping, restricted to a customer segment filtered by the `member` tag.
5. **Create the membership page**: Online Store > Pages > Add page, handle `membership`, template = `page.membership`.
6. **Create the Shipping and Contact pages**: handles `shipping` (template `page.shipping`) and `contact` (template `page.contact`).
7. Upload product photos per-product (Admin > Products > [product] > Media) and a real market photo to replace the illustrated placeholder sections above.

## Workflow

1. Edit theme files locally (sections, templates, assets, etc.) or directly in the Shopify theme editor.
2. Commit and push to this repo.
3. If connected via Shopify's GitHub integration, pushes to the connected branch auto-sync to a theme in your Shopify Admin — review in the theme editor, then publish when ready.
4. Use a non-`main` branch (e.g. `develop`) for work-in-progress and only merge to `main` when you want it live, or use Shopify's per-branch theme preview to stage changes before publishing.

## Local development (optional)

Requires [Node.js](https://nodejs.org/) and the [Shopify CLI](https://shopify.dev/docs/themes/tools/cli):

```bash
npm install -g @shopify/cli @shopify/theme
shopify auth login
shopify theme dev --store=your-store.myshopify.com
```

This gives you a local hot-reload preview at `http://127.0.0.1:9292` synced to your store's data.

## Getting this connected

1. Create an empty repository on GitHub (no README/gitignore — this folder already has them).
2. `git remote add origin <your-repo-url>` then `git push -u origin main`.
3. In Shopify Admin: **Online Store > Themes > Add theme > Connect from GitHub**, authorize, and pick this repo + branch.
