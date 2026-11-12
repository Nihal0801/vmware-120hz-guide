# VMware Workstation: Windows and Linux hosts

[← README](../README.md)

**Experimental adaptation.** This project's direct verification was on macOS with Fusion. The [original firsthand report](https://www.reddit.com/r/vmware/comments/1x64h5x/vmware_workstation_refresh_rate_fix/) describes success with Windows 11 and Ubuntu guests in Workstation 17.5.1 on a Windows 11 host. Workstation on a Linux host has not been tested here.

## Procedure

1. Confirm your physical monitor and host display settings support 120 Hz. Save your guest work and record its current resolution and refresh rate.
2. Identify the target VM's directory through Workstation. Note the path before closing it.
3. Shut down the guest normally, wait until it is off, and exit Workstation. Do not edit a running or suspended VM or delete locks to bypass ownership.
4. Back up the VM's data and separately copy its `.vmx` configuration to a safe location. Configuration backup alone does not protect virtual-disk contents.
5. Open the original `.vmx` using a plain-text editor on the host. On Windows, enable filename extensions to avoid accidentally saving `.vmx.txt`.
6. Add or update the five entries from the [120 Hz snippet](../examples/120hz.vmx.txt). Record old values, keep one entry per key, and preserve unrelated content.
7. Save, close the editor, reopen Workstation, and start the same VM.
8. For a Windows guest, inspect **Settings → System → Display → Advanced display**. If still at 60 Hz, switch to another supported resolution and then back to the original resolution.
9. Check both desktop and active signal mode, plus the selected refresh rate. Record your result and any performance change.

Broadcom documents the general [Workstation/Player configuration-editing procedure](https://knowledge.broadcom.com/external/article/311480/editing-the-vmx-file-of-a-vmware-worksta.html). That reference does not endorse the five refresh-rate entries.

## Linux guests and other combinations

The original report includes an Ubuntu guest, but this project has not established which entries affect Linux graphics drivers. The `wddm` names specifically refer to a Windows graphics-driver model, so do not assume identical behavior on Linux. Inspect your desktop environment's display settings and report the actual result, including the guest display server and driver if known.

For other VMware versions or guest operating systems, treat this as an experiment. Do not extrapolate it to Parallels, VirtualBox, Hyper-V, UTM, or ESXi. Other numeric refresh-rate targets have not been verified here.

If performance worsens or the result is absent, use [troubleshooting](troubleshooting.md) and [rollback](rollback.md). Share a [compatibility report](https://github.com/Nihal0801/vmware-120hz-guide/issues/new?template=compatibility.yml) with versions and measurements rather than a full VM configuration.
