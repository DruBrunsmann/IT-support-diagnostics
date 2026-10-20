# Support Case LAB-002 — Low Disk Space

- Case ID / date: LAB-002 / October 20, 2026
- Lab simulation or real observation: Real observation on my own computer.
- Device / operating environment: Windows 11, Python, PowerShell in VS Code.
- Reported symptom: The diagnostics toolkit flagged low available disk space.
- Expected behavior: Show REVIEW when available disk space is below 10%.
- Exact command used:
  python "C:\Users\Dru\Downloads\Dru_IT_Support_Project\it-support-toolkit\diagnostics.py" --host example.com --output baseline-report.json
- Observed output: 12.08 GiB free out of 464.71 GiB; 2.6% free; status REVIEW.
- Possible causes: Files and installed applications are using most of the drive. Specific causes have not been investigated.
- Checks performed and reasoning: Compared the toolkit's reading with File Explorer, which showed approximately 12 GB free.
- Finding supported by the evidence: Available disk space is below the toolkit's 10% warning threshold.
- Action taken (or escalation needed): Documented the finding. No files were deleted or settings changed.
- Verification result: File Explorer showed approximately the same available space as the toolkit.
- Remaining limitations: The check does not identify which files consume space or establish whether low space is causing performance issues.
- Plain-language explanation for the user: Your drive has about 12 GB available. The program flagged it because less than 10% of its capacity is free.

