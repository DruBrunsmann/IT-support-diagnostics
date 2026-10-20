# IT Support Diagnostics Toolkit

A personal IT support project using Python to collect system information, check disk space, and troubleshoot hostname resolution. Tested and customized on Windows 11.

## What it does

Collects OS/version/architecture, measures free disk space, flags available disk space below 15%, optionally resolves a hostname, and exports a JSON report. Uses Python's standard library; no packages or administrator rights required. It does not change settings or fix problems automatically.

## Run on Windows

Extract the ZIP. Open the extracted folder in File Explorer, type `powershell` in the address bar, and press Enter. With Python 3 installed:

```powershell
python diagnostics.py
python diagnostics.py --host example.com --output my-report.json
python diagnostics.py --disk C:\ --output disk-report.json
```

On WSL/Linux, use `python3` instead of `python`. In WSL, the default disk check describes the Linux home filesystem; use `--disk /mnt/c` to inspect the mounted Windows drive. System details describe WSL, not native Windows.

The program prints a report even if you do not save it. Use a new output filename on each run; it deliberately refuses to overwrite files. Host lookup is optional and requires a working local resolver. A timed-out lookup returns a status after five seconds, but Python may remain running until the operating system's resolver finishes.

## Customization and testing

How to run: python test_threshold.py

Changed the low-disk-space warning threshold from 10% to 15%
to provide an earlier warning.

Verified the change using test_threshold.py, which simulates
12% free disk space and confirms that the result is REVIEW.
The test does not modify actual disk space.

## Troubleshooting guide

| Symptom | First checks | Interpretation / next step |
|---|---|---|
| One website will not open | Confirm spelling, try another site, run optional host lookup | Lookup failure can involve spelling, DNS, or network configuration. Do not assume DNS is the root cause. |
| Disk warning | Check filesystem and available space in OS storage settings | Review large files with the owner; do not delete data without authorization. |
| Check returns ERROR | Check that the supplied disk path exists and is accessible | Correct the path or document access limitations. |
| Lookup succeeds but site fails | Inspect browser error, proxy/VPN and service status | This tool does not test HTTPS, routing, firewall rules, or application availability. |

## Limits and privacy

No ticketing platform, remote support, Active Directory, network scanning, malware detection, or automatic repair is implemented. Reports may contain IP addresses and error paths. Review and redact before publishing. Do not publish another person's device information.
