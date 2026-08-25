# Ocean Fish Market

Shopify theme for Ocean Fish Market, built on top of [Shopify's Dawn theme](https://github.com/Shopify/dawn). Theme code (Liquid, CSS, JS) lives here in GitHub; Shopify pulls from this repo to deploy the storefront.

See [DAWN-REFERENCE.md](./DAWN-REFERENCE.md) for Dawn's original docs (theme structure, developer tools, staying in sync with upstream Dawn changes).

## Project setup status

- [x] Theme code initialized from Dawn
- [x] Branding pass: color palette (deep ocean blue `#0B3D5C` + coral accent `#FF6B4A`), header/footer/announcement bar, homepage hero copy
- [ ] GitHub repo created and this local repo pushed to it
- [ ] Shopify store connected to this GitHub repo (Online Store > Themes > Add theme > Connect from GitHub)
- [ ] Node.js + Shopify CLI installed locally for `shopify theme dev` live preview (optional but recommended)
- [ ] Upload real logo (currently falls back to store name as text wordmark) and a homepage hero image (currently blank placeholder)
- [ ] Review/replace placeholder copy: announcement bar text, homepage headline, footer tagline, contact page

## Branding

- **Colors:** deep ocean navy `#0B3D5C` (header/footer/dark sections), coral `#FF6B4A` (buttons, CTAs, sale badges, announcement bar), white/light-blue-tinted neutrals for content and cards. Defined in `config/settings_data.json` under `color_schemes` (scheme-1 through scheme-5) — adjustable live in the Shopify theme editor under Theme settings > Colors, no code changes needed.
- **Logo:** no image yet — header shows the store name as a text wordmark. Add a logo image via Theme settings > Logo in the Shopify editor once you have one; favicon can be set the same way.

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
