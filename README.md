# Ocean Fish BH

Shopify theme for Ocean Fish BH, built on top of [Shopify's Dawn theme](https://github.com/Shopify/dawn). Theme code (Liquid, CSS, JS) lives here in GitHub; Shopify pulls from this repo to deploy the storefront.

Branding and copy are pulled from the existing [oceanfishmarketbh.lovable.app](https://preview--oceanfishmarketbh.lovable.app) site: New York's premium wild-caught fish market, family operated, founder Slavik, three retail locations plus a wholesale operation, next-day delivery to NYC/Long Island/NJ, Kosher certified.

See [DAWN-REFERENCE.md](./DAWN-REFERENCE.md) for Dawn's original docs (theme structure, developer tools, staying in sync with upstream Dawn changes).

## Project setup status

- [x] Theme code initialized from Dawn
- [x] Branding pass: palette matched to the existing site (navy `#0B2A45` + teal `#229E97` + gold `#C9A227`), real hero copy, trust badges, header/footer
- [x] "Our Story" page with the real founder/company story
- [x] Wholesale membership theme logic: gated pricing/add-to-cart on wholesale products, membership landing page, homepage sections
- [ ] GitHub repo created and this local repo pushed to it
- [ ] Shopify store connected to this GitHub repo (Online Store > Themes > Add theme > Connect from GitHub)
- [ ] Node.js + Shopify CLI installed locally for `shopify theme dev` live preview (optional but recommended)
- [ ] Real logo file and product/market photos (currently text wordmark + illustrated placeholders — the existing Lovable site has professional product photography worth reusing if you have the source files)
- [ ] Navigation menu (Home / Shop / Our Story / Shipping / Contact) — lives in Shopify Admin, not this repo, see below
- [ ] Shipping and Contact pages — not yet built, send the content and I'll add them
- [ ] Admin-side setup for payments and membership — see below, none of this lives in the theme repo

## Branding

- **Colors:** navy `#0B2A45` (header nav is white/light instead — see note below — but hero photo overlay, footer, and dark sections use navy), teal `#229E97` (primary CTA buttons, matching "Shop Our Catch" on the real site), gold `#C9A227` (badges, sale tags, accents — matching the real site's script-text and "Best Seller" badge). Defined in `config/settings_data.json` under `color_schemes` (scheme-1 through scheme-5) — adjustable live in the Shopify theme editor under Theme settings > Colors, no code changes needed.
- **Logo:** the real site has a designed two-line "OCEAN / FISH BH" logo with an icon — send the logo file (SVG/PNG) and I'll wire it into Theme settings > Logo. Until then the header falls back to the store's name as a text wordmark, which only reads "Ocean Fish BH" once the actual Shopify store is named that.
- **Images:** the homepage's "Our market" and "Shop by type" sections use hand-drawn SVG placeholders (in `sections/our-market.liquid` and `sections/shop-by-species.liquid`) so the layout isn't empty. The real site has professional product photography (salmon fillets, market interior) — if you have the source image files, send them and I'll swap the placeholders and wire up real product images.

## Wholesale membership

The theme enforces membership gating, but **billing, tagging, and product data are all Shopify Admin/app configuration — not code.** Here's what's built vs. what you still need to set up.

### Built into the theme

- `snippets/buy-buttons.liquid`: any product tagged `wholesale` shows its price to everyone, but only checks out for customers tagged `member` — non-members see a "Join to order wholesale" card linking to `/pages/membership` instead of the add-to-cart button. Also shows a "5 lb minimum per order" note.
- `templates/page.membership.json`: a membership landing page (benefits, pricing, how it works) — publish it as a page with handle `membership` so it matches the links above.
- Homepage sections: hero (real copy, "Shop Our Catch" / "Our Story" buttons), trust badges (Next-Day Delivery / Wild Caught / 30+ Years Experience / Kosher Certified), "Shop by type" (salmon/tuna/whitefish/wholesale icons), "Our market" (illustrated scene + story teaser), and a membership CTA banner.
- `templates/page.our-story.json`: full founder story page — publish as a page with handle `our-story`.

## Navigation

Dawn's header pulls its menu from Shopify's own navigation data (Admin > Online Store > Navigation), not from this repo. To match the real site, create a menu named "Main menu" with: Home, Shop (→ `/collections/all`), Our Story (→ `/pages/our-story`), Shipping (→ a Shipping page you'll need to create), Contact (→ a Contact page you'll need to create). Shipping and Contact pages aren't built yet — send their content from the existing site and I'll add them the same way as Our Story.

### You'll need to do in Shopify Admin

1. **Enable payments**: Settings > Payments — enable Shopify Payments or another provider. Required before any checkout works; involves your bank/business details, so this has to be you.
2. **Install the free Shopify Subscriptions app** (Shopify App Store) and create the membership product:
   - Handle it as `ocean-fish-market-membership` (or update the links in `templates/page.membership.json` and `snippets/buy-buttons.liquid` to match whatever handle you use).
   - Add two selling plans: monthly at $3.00, annual at $36.00.
   - In the app's settings, turn on auto-tagging so an active subscriber gets tagged `member` on their customer profile — this is what the theme checks to unlock wholesale pricing.
3. **Create wholesale products** (whole fish): price at $9.99/lb (sold by weight, or list per-lb and let quantity = pounds), tag each `wholesale`, and set the variant's quantity rule to **minimum 5, increment 1** (Admin > product > variant > "This item has quantity rules") so 5 lb is enforced at checkout.
4. **Create a collection** with handle `wholesale` containing those products (so `/collections/wholesale` works — linked from the homepage and membership page).
5. **Free shipping for members**: Admin > Discounts > create an automatic discount, 100% off shipping, restricted to a customer segment filtered by the `member` tag.
6. **Create the membership page**: Online Store > Pages > Add page, handle `membership`, template = `page.membership`.
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
