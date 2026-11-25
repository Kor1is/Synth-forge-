# Third-Party Notices

Infinity Workbench is distributed under the MIT License. The source tree does
**not** vendor, copy, or redistribute third-party source code, artwork, sequence
records, or model files. Dependencies are installed separately through
`requirements.txt`; their licenses continue to apply.

The released source package contains no prebuilt runtime or bundled binaries.
Optional GPL tooling is never bundled.

## Direct runtime dependencies

| Package | Version | License | Upstream |
| --- | --- | --- | --- |
| Streamlit | 1.67.0 | Apache-2.0 | https://github.com/streamlit/streamlit |
| pandas | 3.1.1 | BSD-3-Clause | https://github.com/pandas-dev/pandas |
| NumPy | 2.4.6 | BSD-3-Clause | https://github.com/numpy/numpy |
| Matplotlib | 3.11.2 | PSF-based Matplotlib License | https://github.com/matplotlib/matplotlib |
| Biopython | 1.88 | BSD-3-Clause | https://github.com/biopython/biopython |
| Jinja2 | 3.1.6 | BSD-3-Clause | https://github.com/pallets/jinja |
| openpyxl | 3.1.5 | MIT | https://foss.heptapod.net/openpyxl/openpyxl |
| Pillow | 13.0.0 | HPND | https://github.com/python-pillow/Pillow |
| Biotite | 1.6.0 | BSD-3-Clause | https://github.com/biotite-dev/biotite |

Development dependency: pytest 8.4.2 (MIT). It is used only for the test suite
and is not required at runtime.

## Optional dependencies

These are deliberately excluded from the default MIT runtime bundle:

| Package / tool | License | Purpose |
| --- | --- | --- |
| COBRApy | GPL-3.0 | M4 SBML / flux analysis. Optional; M4 shows an install hint when absent. |
| WeasyPrint | BSD-3-Clause | Optional PDF export. Reports print from HTML without it. |
| ColabFold | MIT (upstream) | Optional external executable for M7. Not bundled or imported. |
| Cello | BSD-3-Clause (upstream) | Optional external Java tool for M12. Not bundled or imported. |
| DNA Weaver | MIT (upstream) | Optional M11 assembly library. A built-in overlap fallback is used when absent. |

Before installing an optional package, review its upstream license. In
particular, COBRApy is GPL-3.0 and may impose additional obligations on a
combined distribution. The default `requirements.txt` intentionally contains
only permissive dependencies.

## Data, fonts, and visual assets

- All sequences under `data/` are original synthetic strings generated for this
  project. They are not derived from Addgene, iGEM, GenBank, or any publication.
- The SBML model under `data/demo/m4/` is a toy model written for this project.
- PDB and GenBank fixtures are synthetic coordinates/records created by the
  project's own generator.
- `docs/assets/app-icon.png` and `docs/assets/app.ico` are original drawings.
- The UI requests system fonts (`-apple-system`, `SF Pro Text`, `PingFang SC`,
  `Microsoft YaHei`, `JetBrains Mono`) but does not bundle font files.
- No third-party screenshots, icons, illustrations, or datasets are included.

If you add a dependency or asset, record its origin and license here before
committing it.