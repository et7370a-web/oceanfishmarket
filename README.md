# Ocean Fish Market

Shopify theme for Ocean Fish Market, built on top of [Shopify's Dawn theme](https://github.com/Shopify/dawn). Theme code (Liquid, CSS, JS) lives here in GitHub; Shopify pulls from this repo to deploy the storefront.

See [DAWN-REFERENCE.md](./DAWN-REFERENCE.md) for Dawn's original docs (theme structure, developer tools, staying in sync with upstream Dawn changes).

## Project setup status

- [x] Theme code initialized from Dawn
- [x] Branding pass: color palette (deep ocean blue `#0B3D5C` + coral accent `#FF6B4A`), header/footer/announcement bar, homepage hero copy
- [x] Wholesale membership theme logic: gated pricing/add-to-cart on wholesale products, membership landing page, homepage sections
- [ ] GitHub repo created and this local repo pushed to it
- [ ] Shopify store connected to this GitHub repo (Online Store > Themes > Add theme > Connect from GitHub)
- [ ] Node.js + Shopify CLI installed locally for `shopify theme dev` live preview (optional but recommended)
- [ ] Upload real logo (currently falls back to store name as text wordmark) and real product/market photos (currently illustrated placeholders)
- [ ] Review/replace placeholder copy: announcement bar text, homepage headline, footer tagline, contact page
- [ ] Admin-side setup for payments and membership — see below, none of this lives in the theme repo

## Branding

- **Colors:** deep ocean navy `#0B3D5C` (header/footer/dark sections), coral `#FF6B4A` (buttons, CTAs, sale badges, announcement bar), white/light-blue-tinted neutrals for content and cards. Defined in `config/settings_data.json` under `color_schemes` (scheme-1 through scheme-5) — adjustable live in the Shopify theme editor under Theme settings > Colors, no code changes needed.
- **Logo:** no image yet — header shows the store name as a text wordmark. Add a logo image via Theme settings > Logo in the Shopify editor once you have one; favicon can be set the same way.
- **Images:** the homepage's "Our market" and "Shop by type" sections use hand-drawn SVG placeholders (in `sections/our-market.liquid` and `sections/shop-by-species.liquid`) so the layout isn't empty. Swap them for real photos by editing those files, or ask to have them redone once you have photography — no theme-editor picker is wired up for these two, they're hardcoded illustrations by design so they render without any uploads.

## Wholesale membership

The theme enforces membership gating, but **billing, tagging, and product data are all Shopify Admin/app configuration — not code.** Here's what's built vs. what you still need to set up.

### Built into the theme

- `snippets/buy-buttons.liquid`: any product tagged `wholesale` shows its price to everyone, but only checks out for customers tagged `member` — non-members see a "Join to order wholesale" card linking to `/pages/membership` instead of the add-to-cart button. Also shows a "5 lb minimum per order" note.
- `templates/page.membership.json`: a membership landing page (benefits, pricing, how it works) — publish it as a page with handle `membership` so it matches the links above.
- Homepage sections: "Shop by type" (fish/salmon/shrimp/scallop icons), "Our market" (illustrated dockside scene + story), and a membership CTA banner.

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
