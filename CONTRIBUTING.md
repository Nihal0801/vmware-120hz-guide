# Contributing

Thanks for helping make the guide reproducible. Both successful and unsuccessful results are useful.

## Report a test

Use the [compatibility form](https://github.com/Nihal0801/vmware-120hz-guide/issues/new?template=compatibility.yml). Include host OS/hardware, VMware version, guest OS/architecture, display driver if known, host display mode, before/after guest mode, whether a resolution refresh was needed, and any CPU or stability observations.

Distinguish a reported display mode from measured application FPS and physical frame delivery. Include the method and duration for any performance measurement. Do not label a platform verified merely because the settings saved successfully.

## Improve the documentation

1. Fork and clone the repository.
2. Make a focused change, preserving the distinction between direct verification, external reports, and hypotheses.
3. Run `python3 scripts/check_docs.py` from the repository root (on Windows, `py -3 scripts/check_docs.py` is also suitable).
4. Open a pull request describing the correction and its evidence.

Do not add automatic VM modification, downloadable drivers, or unsupported safety claims without a separately reviewed design. Screenshots are deferred for the initial release; follow [the evidence plan](docs/screenshots.md) when contributing them later.

## Protect private data

Share the five relevant key/value pairs rather than a complete VM configuration. Do not upload VM bundles, virtual disks, raw logs, configuration backups, passwords, encryption material, or personal paths. Review screenshots before posting.

Original contributions use the repository's [MIT License](LICENSE). Credit outside sources and link to them instead of copying their articles.
