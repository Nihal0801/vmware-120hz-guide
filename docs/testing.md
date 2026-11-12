# Verification record

[← README](../README.md)

**Session date:** November 12, 2026

**Maintainer:** [Nihal Patel](https://github.com/Nihal0801)

**Status:** 120 Hz guest display mode verified on one Mac; performance unmeasured.

## Environment

| Component | Observed configuration |
| --- | --- |
| Host GPU/chip | Apple M5 Pro, 16 GPU cores |
| Host OS | macOS 27.0.1 |
| Host display | Built-in display; ProMotion already enabled |
| Fusion version | `26.0.0`, read from the installed application's bundle metadata |
| Guest | Windows 11 Home, ARM64 |
| Virtual hardware version | `22` |
| vCPU / guest RAM | 4 vCPUs / 8192 MB |
| 3D acceleration | Enabled |
| Retina support | Enabled |
| Renderer | Metal, confirmed in the session's VMware log |
| Graphics adapter | VMware SVGA 3D |
| Graphics driver observed during investigation | `9.17.11.0003`, build `25171296` |
| VMware Tools internal version observed | `13344` |
| Final guest resolution | 3600 × 2260 |

These are test conditions, not minimum system requirements. The host OS, Fusion version, chip, and five persisted entries were rechecked while preparing this repository. Driver and Tools values are the observations from the investigation, not a claim that they were re-enumerated after every update.

## Evidence and sequence

1. The initial Windows Advanced display page showed the VMware adapter and a 60 Hz setup; 120 Hz was not available there.
2. macOS already used ProMotion. Enabling it was therefore not the missing step in this session.
3. The five-entry combination was identified in the credited community experiment.
4. Windows was shut down normally. The investigation observed a clean VM exit before editing.
5. A remaining Fusion lock caused the first guarded edit attempt to stop. Fusion was quit; no lock was forcibly deleted.
6. The original configuration was copied and its hash checked. None of the five entries existed beforehand.
7. The five entries were added at 120 Hz. Other configuration entries were retained.
8. The VM started normally. Pending Windows updates completed; the VM was not interrupted during that process.
9. A resolution refresh occurred, and Fusion's resize-to-fit command restored the full guest resolution.
10. The maintainer reported 120 Hz. A subsequent visual inspection of Windows Advanced display confirmed **Desktop mode: 3600 × 2260, 120 Hz**, **Active signal mode: 3600 × 2260, 120 Hz**, and **selected refresh rate: 120 Hz**.

The final page also showed 8-bit RGB SDR output and no guest VRR/DRR support. Those features were not changed by this experiment.

## Verification levels

| Level | What it establishes | This project |
| --- | --- | --- |
| Configuration | Five intended entries are present | Confirmed |
| Guest display mode | Windows reports 120 Hz in both mode fields | Visually confirmed |
| Application rendering | A named app renders at a measured rate | Not tested |
| Physical frame delivery | Distinct frames reach the physical screen at 120 per second | Not tested |
| Persistence | Behavior survives repeated cold starts, suspend/resume, and display changes | Not tested |
| Performance and endurance | CPU, power, latency, stability over a defined workload and duration | Not tested |

For future performance claims, record the test tool/version, host refresh setting, guest resolution, application, workload, duration, and measurement method. A browser animation counter can be useful context but is not conclusive proof of physical frame delivery through a VM. State what the measurement actually measures.

## Evidence not included

- Screenshots will be considered in a later update; **none are published yet**.
- Raw VM configurations, backups, log files, machine identifiers, and credentials are excluded.
- No synthetic benchmark numbers or reconstructed proof screenshots are supplied.

The current record is a written account of an observed session, not a public performance dataset. See the [screenshot plan](screenshots.md) for the later evidence update.

## Other platforms

The [original author](https://www.reddit.com/r/vmware/comments/1x64h5x/vmware_workstation_refresh_rate_fix/) reports testing Windows 11 and Ubuntu guests in Workstation 17.5.1 on Windows 11. A commenter reports success at 120 Hz on macOS without detailed version information. These remain **external reports**, separate from this project's direct verification.

Submit additional results through the [compatibility form](https://github.com/Nihal0801/vmware-120hz-guide/issues/new?template=compatibility.yml). A successful report should describe its measurement level; a failure is useful evidence too.
