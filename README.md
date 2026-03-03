# DiveNET: Sealink-OEM

Repository landing page and navigation.

## Where to start

- Product docs and source bundle: [product/](product/)
- Main product overview: [product/README.md](product/README.md)
- Requirements and options: [product/Sealink-OEM_Requirements_and_Options.md](product/Sealink-OEM_Requirements_and_Options.md)
- Integrator/testing process guide: [product/integrations/PLATFORM_INTEGRATOR_GUIDE.md](product/integrations/PLATFORM_INTEGRATOR_GUIDE.md)

## Repository layout

- `product/` contains the current documentation and integration content.
- Root-level build/release scripts (`*.bat`, `*.spec`, `VERSION.txt`) are packaging utilities.
- `release/` and `release_assets/` hold generated/customer-facing distribution assets.

## Testing release policy

- Do not resend a new tester app for GitHub sync-only or documentation-only updates.
- Resend the Operator Package only when candidate runtime behavior changes.
- Keep one published test baseline until a new candidate is intentionally announced.

Questions: support@divenetgps.com
