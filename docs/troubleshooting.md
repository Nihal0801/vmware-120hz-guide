# Troubleshooting

[← README](../README.md)

| Symptom | What to check / do next |
| --- | --- |
| Windows still reports 60 Hz | Confirm you edited the correct VM, fully shut it down, quit VMware, and saved all five entries once. Boot again and change to another supported resolution and back. |
| Changes disappear | VMware may have still been open or you may have edited the wrong file. Repeat the shutdown/quit checks before editing again. |
| A `.lck` file or directory remains | Check whether the VM or VMware still owns it. Our lock cleared after quitting Fusion. Do not force-delete locks. |
| Guest uses Microsoft Basic Display Adapter | Check VMware Tools and the display driver through the normal supported installation/repair path. Our verified guest used VMware SVGA 3D. |
| VM fails to start after editing | Check for curly quotes, rich-text formatting, duplicate entries, or a changed filename extension. Restore the previous configuration if needed. |
| Windows looks enlarged or low resolution | Restore the original guest resolution. In Fusion, resize-to-fit can restore the guest view; then check Advanced display again. |
| 120 Hz appears, but motion still feels like 60 Hz | Confirm the physical display mode, then measure application rendering and physical frame delivery separately. A guest mode label is not a frame-rate measurement. |
| CPU usage, heat, or battery drain increases | Compare the same workload before/after. The original author reported higher Windows guest CPU use. Roll back if the tradeoff is unacceptable. |
| Guest VRR or dynamic refresh rate remains unavailable | That is consistent with the verified setup. This workaround did not enable VRR/DRR. |
| Result changes after suspend, reboot, or update | Those persistence cases are unverified here. Recheck the configuration and mode, try the resolution refresh, and document the trigger. |
| External display behaves differently | Record its actual host refresh rate and connection, and test it separately. Our verification used the built-in Mac display. |
| An encryption password is requested | Use the VM's supported unlock flow. Do not remove encryption or the TPM; the guest login password may be different. |

If the procedure is ineffective, stop adding unrelated speculative settings. Use [rollback](rollback.md) and submit a [problem report](https://github.com/Nihal0801/vmware-120hz-guide/issues/new?template=problem.yml) with versions, exact symptoms, and the five relevant values only.

Never attach a full `.vmx`, virtual disk, password, recovery key, serial number, or unredacted log. Crop future screenshots to the relevant settings and remove account identifiers.
