# Changelog

All notable changes to this project are documented here. The format follows
Keep a Changelog, and versions use semantic versioning.

## [1.0.0] - 2026-11-24

### Added

- Sixteen local modules: sequence analysis, codon optimization, primer design,
  metabolic analysis, lab calculations, design-rule checks, structure prediction,
  structure evaluation, sequencing verification, plasmid maps, assembly planning,
  circuit design, RBS candidates, resource library, construct diff, and batch runs.
- SQLite-backed projects, parts, constructs, strains, resources, runs, and
  artifacts, with an idempotent additive migration.
- Asynchronous run queue with queued/running/done/failed/partial/cancelled
  states, cancellation, retry, per-run logs, and SHA-256 artifact checksums.
- Streamlit interface with grouped Chinese navigation, twelve fixed components,
  seven interface states, light/dark CSS-variable themes, and a collapsible task
  rail.
- D1 multi-run HTML reports with embedded figures and D2 A4 protocol cards.
- Original synthetic demo fixtures for every demo-capable module and an
  idempotent demo project loader.
- pytest coverage for adapters, database, task lifecycle, and a Streamlit AppTest
  smoke path.
- MIT license, third-party notices, CI workflow, setup script, and usage guide.
- Windows launcher (`启动 Infinity Workbench.cmd`) that starts a loopback-only
  local server on port 8501 and opens the app page in the default browser; the
  app data stays under `workspace/`.
- Detailed dependency remediation guide and a biosafety/data-privacy disclaimer.

### Security / licensing

- No network calls at runtime, no user accounts, no telemetry.
- ColabFold and Cello are invoked only as external subprocesses and are not
  imported by the application.
- Optional GPL tooling (COBRApy) is excluded from the default runtime bundle and
  documented separately.