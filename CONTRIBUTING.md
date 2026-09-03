> **File use case:** Contribution workflow for developers.
> **What it does:** Defines branch, quality, review, and documentation expectations for changes.

# Contributing

Create a focused branch, keep changes small, and include tests that demonstrate acceptance criteria. Run `make check` before requesting review.

Commits should state the user-visible or architectural outcome. Pull requests should include purpose, scope, verification evidence, security and tenant-isolation impact, migration or rollback notes, and screenshots for visible changes.

Changes to system boundaries, persisted schemas, external providers, or security posture require an architecture decision record in `docs/decisions`.

Never add secrets, customer datasets, generated model artifacts, or copied production data. Use synthetic fixtures.

