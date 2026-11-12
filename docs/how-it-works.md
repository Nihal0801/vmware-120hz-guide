# Settings, reasoning, and algorithm

[← README](../README.md)

## What changed

The experiment changed **five entries in one existing VM's configuration**. It did not install a custom driver or modify the Mac's display firmware. The host already had ProMotion enabled, and the guest already used VMware's graphics driver.

| Entry | Tested value | Interpretation, not a verified internal specification |
| --- | --- | --- |
| `guestinfo.svga.wddm.vsyncDefaultHz` | `120` | Appears to set a default cadence for the Windows VMware display driver |
| `guestinfo.svga.wddm.vsyncMaxHz` | `120` | Appears to set an upper cadence for the same path |
| `guestinfo.svga.wddm.vsyncThread` | `TRUE` | Appears to enable a VSync-related driver thread/path |
| `mks.lowCompositingFPS` | `120` | Appears to affect VMware's lower compositing cadence |
| `mks.maxCompositingFPS` | `120` | Appears to affect VMware's maximum compositing cadence |

The names and [original firsthand experiment](https://www.reddit.com/r/vmware/comments/1x64h5x/vmware_workstation_refresh_rate_fix/) suggest these roles. We have not reverse-engineered their implementations or found official documentation guaranteeing those meanings. The result applies to the **combination**, and does not prove that every entry is necessary.

## Three different things to measure

1. **Guest display mode:** Windows' reported resolution and refresh rate. This is what we verified.
2. **Rendered/presented frames:** How often an application and the virtual graphics stack produce distinct frames. This was not measured.
3. **Physical display output:** How many distinct frames the host screen actually displays. This was not measured.

A 120 Hz label is evidence for item 1. It does not by itself prove items 2 or 3. Host refresh rate, application load, frame pacing, compositor behavior, and driver behavior all remain relevant.

## Reproducible algorithm

This is procedural pseudocode, not a command to paste into a terminal. The [manual walkthrough](../README.md#mac-walkthrough-vmware-fusion) implements it without requiring a script.

```text
INPUT: one explicitly selected existing VM, target = 120 Hz

record host mode, guest mode, product version, and driver version
save guest work
shut down the guest normally; wait for completion
quit VMware; confirm no process still owns this VM
if configuration remains locked:
    stop and investigate; do not delete locks

read the original configuration
make a separate backup and verify it matches the original
record the original entries (or absence) for each of the five keys

for each key in the tested snippet:
    replace its existing entries with one tested value
    or append one entry if it was absent

confirm the original did not change while preparing the edit
save the edited configuration
check the diff: only the five intended keys should differ

start VMware and the guest normally
allow any pending OS update to finish
inspect Advanced display
if still 60 Hz:
    change to another supported resolution
    restore the original resolution
inspect both mode fields and the selected refresh rate again

record exactly what was observed, including any failures
if unwanted behavior occurs:
    shut down and quit again
    restore only the five original entries
    recheck the original behavior
```

## Implementation used in the original session

A small local Python script performed the configuration edit after shutdown. It checked for lock files, checked the `cleanShutdown` flag, saved a byte-for-byte backup, compared SHA-256 hashes, recorded prior values, checked that the source had not changed, and updated only the five keys. A companion rollback script was prepared to restore those keys while retaining unrelated settings.

These checks complemented the observed shutdown; a flag or absent lock alone is not sufficient proof that an arbitrary VM is powered off. The first edit attempt stopped because Fusion still held a lock. Quitting Fusion allowed the guarded edit to proceed.

The machine-specific scripts, raw backup, and private configuration are intentionally not published. They contain local paths or VM data and are not portable installers. This repository publishes the complete method and sanitized five-line configuration. The only executable repository utility, [check_docs.py](../scripts/check_docs.py), validates documentation and never edits VMware files.

## Scope of the experiment

No individual-setting A/B test, automated frame benchmark, or long-duration stability test was performed. Pending Windows updates completed during startup, so the session was not a fully controlled benchmark with all other software state held constant. The evidence supports the observed configuration and display-mode result; it does not establish a universal cause for every VMware 60 Hz limitation.

The exact [test record](testing.md) is the source of this repository's verification claims.
