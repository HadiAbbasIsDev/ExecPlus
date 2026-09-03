> **File use case:** Canonical delivery plan and phase-completion ledger.
> **What it does:** Defines scope, exit criteria, dependencies, and verified status for each professional delivery phase.

# ExecPlus Delivery Roadmap

Statuses are limited to `Complete`, `In progress`, `Planned`, and `Frozen`. A phase becomes complete only when its exit criteria are demonstrated by automated checks or an explicitly recorded operational review.

## Phase 0 — Engineering foundation

**Status:** Complete  
**Completed:** 2026-09-02

Delivered:

- Product invariants and system boundaries documented.
- Modular monorepo created for the API and web application.
- Domain-first backend dependency rules established.
- Replaceable language-model and embedding-store ports established.
- Local and hosted model routing expressed through validated configuration.
- PostgreSQL and S3-compatible local infrastructure defined.
- Health/readiness API and project-status UI implemented.
- Backend unit and architecture test foundations added.
- CI, linting, type checking, environment template, and developer commands added.
- Architecture decision records created for modularity, exact computation, and provider neutrality.

Exit evidence:

- Python modules compile.
- Baseline tests pass in an installed development environment.
- Frontend type and lint checks pass in an installed development environment.
- No runtime dependency points directly at a vector database vendor.

## Phase 1 — Secure ingestion and profiling

**Status:** Planned

Scope:

- Authentication and workspace membership.
- Configurable seat limits from 3 to 50.
- Workspace-isolated dataset metadata and object storage.
- Single-table CSV and single-sheet XLSX uploads up to 20 MB.
- Clear rejection of multi-sheet files, merged cells, unsafe formats, and size violations.
- Deterministic profiling for row count, column count, inferred types, ranges, metrics, dimensions, and semantic tags.
- Upload and profiling audit events.

Exit criteria:

- Cross-workspace access tests prove isolation.
- Parser fixtures cover valid, malformed, oversized, multi-sheet, and merged-cell inputs.
- Profiling results are reproducible for fixed fixtures.
- A non-technical user can upload a supported file and understand its profile.

## Phase 2 — Verified conversational analytics

**Status:** Planned

Scope:

- Curated semantic definitions and join-path representation.
- Intent router for numerical, textual, unsupported, and ambiguous questions.
- Read-only SQL planning, parsing, validation, cost limits, timeout limits, and DuckDB execution.
- Clarification guard for competing metric or dimension mappings.
- Multi-turn thread state using structured references rather than raw prompt history alone.
- Suggested questions derived from the profiled schema.
- Answer assembly from executed rows only.
- Calculation lineage and complete audit trail.

Exit criteria:

- Golden question suites return exact expected values.
- Prompt-injection tests cannot bypass read-only or tenant constraints.
- Ambiguous and unsupported questions never execute a query.
- Each numerical answer can be reconstructed from stored lineage.

## Phase 3 — Proactive insights and hybrid knowledge

**Status:** Planned

Scope:

- Three deterministic, ranked observations after profiling.
- Document ingestion and chunk metadata model.
- Embedding provider evaluation using representative customer corpora.
- Vector database benchmark and architecture decision record.
- Permission-first hybrid retrieval, reranking, and citations.
- Local and hosted model quality, latency, privacy, and cost evaluation.

Exit criteria:

- Selected vector provider passes isolation, filtering, backup, latency, and cost tests.
- Citations resolve to accessible source passages.
- Retrieval evaluation meets an agreed relevance threshold.
- No retrieval path can expose a passage before authorization filtering.

## Phase 4 — Forecasting, boards, and export

**Status:** Planned

Scope:

- Thirty-day statistical forecasts with uncertainty ranges and sufficiency checks.
- Persistent dashboard with a maximum of six pinned results.
- PNG chart export and CSV result export.
- Explainable forecast lineage, method, training window, and limitations.

Exit criteria:

- Forecast backtests and failure messages are validated on representative fixtures.
- Pin limits are enforced on the server.
- Exported values match executed query results exactly.

## Phase 5 — Production hardening and alpha

**Status:** Planned

Scope:

- Cloud deployment with isolated staging and production environments.
- Managed database, object storage, secrets, encryption, backups, and restoration drills.
- Observability, model and query tracing, rate limits, budgets, and incident runbooks.
- Load, security, privacy, accessibility, and browser testing.
- Manual provisioning for five to six alpha companies.

Exit criteria:

- Recovery objectives are documented and tested.
- Security and tenant-isolation review has no open critical findings.
- Service-level indicators and alerts cover the critical user journey.
- Alpha onboarding and rollback runbooks have been rehearsed.

## Post-alpha

**Status:** Frozen

- Live Shopify and PostgreSQL connectors.
- Email alerts.
- Built-in billing user interface.
- Advanced role-based access control.
- Native mobile applications.

