# Research documents

Source-linked public video guides for Lars, preserving the approved PE HTML layout.

Live target: https://larsklander.com/research-documents-pe/

The custom domain is owned by `larsklanderpe/agents-phone`. This repository is the canonical content and skill source; rendered `site/` files are published into that site's `research-documents-pe/` directory. Do not assign the root custom domain to this repository.

Add or update `content/*.json`, then run `python scripts/render.py`. The renderer rebuilds the library index and standalone guides. `skills/research-video-guide/SKILL.md` defines the workflow. `scripts/Publish-Research.ps1` prepares the domain-site publication PR; merge follows the active authorization rules.

Publish only public summaries and intentionally public material. Notes entered into the guides stay in browser storage and are not sent to GitHub. Save a PDF to carry completed notes across devices.
