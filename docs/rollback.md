# Restore the previous configuration

[← README](../README.md)

## Preferred: restore just the five entries

1. Save guest work, shut down normally, and wait until the VM is fully off.
2. Quit Fusion or Workstation completely. Investigate remaining locks; never delete them simply to force access.
3. Make a separate copy of the current configuration before reversing anything.
4. Compare the original backup with the current file for these keys:

   - `guestinfo.svga.wddm.vsyncDefaultHz`
   - `guestinfo.svga.wddm.vsyncMaxHz`
   - `guestinfo.svga.wddm.vsyncThread`
   - `mks.lowCompositingFPS`
   - `mks.maxCompositingFPS`

5. Restore each original value. If a key was absent originally, remove that entry. Preserve all unrelated settings.
6. Save as plain text, restart VMware and the VM, and inspect the display mode again. Refresh the resolution if necessary.

In the documented Mac session, all five entries were originally absent. Removing exactly those five entries restores their original state for that VM. Do not assume the same for another VM.

## Full configuration restoration

If the VM fails to start because the configuration was malformed, restoring the original `.vmx` may be appropriate. First quit VMware and preserve the current file separately. Copy the known-good backup to its original location and original filename.

Restoring an old full configuration also reverses unrelated configuration changes made since that backup. If virtual disks, snapshots, encryption, or virtual hardware have changed in the meantime, do not blindly substitute an old configuration; resolve those differences first. Never replace the `.vmwarevm` package or delete virtual disks as part of this display rollback.

## No backup available

If you know the five keys were absent before the experiment, removing them reverses the addition. If you do not know their previous values, stop and establish the prior configuration rather than guessing. Setting every value to 60 is not necessarily equivalent to restoring the defaults.
