# Support Case LAB-001 — Failed Hostname Lookup

- Case ID / date: LAB-001 / October 20, 2026
- Lab simulation or real observation: Lab simulation
- Device / operating environment: Windows 11, Python 3.13.14, PowerShell terminal in Visual Studio Code
- Reported symptom: The toolkit could not resolve intentional-test.invalid to an IP address.
- Expected behavior: Report FAILED with an error message and continues without crashing.
- Exact command used:
  python "C:\Users\Dru\Downloads\Dru_IT_Support_Project\it-support-toolkit\diagnostics.py" --host intentional-test.invalid --output failed-lookup-report.json
- Observed output (redact sensitive details): Hostname status was FAILED, with detail "[Errno 11001] getaddrinfo failed".
- Possible causes: In general, failed lookups can involve invalid hostnames, resolver issues, or network problems. This test deliberately used an invalid hostname.
- Checks performed and reasoning: First tested example.com, which resolved successfully. Then tested intentional-test.invalid to check how the toolkit handles an unsuccessful lookup.
- Finding supported by the evidence: The intentionally invalid hostname failed to resolve as expected. This result does not establish a DNS configuration problem.
- Action taken (or escalation needed): No repair or escalation needed. Recorded the expected failure in a JSON report.
- Verification result: The toolkit displayed the failure, saved the report, and returned to the terminal without crashing.
- Remaining limitations: This test checks hostname resolution and error handling. It does not test website access or diagnose every possible network issue.
- Plain-language explanation for the user: The test address was intentionally invalid. The program correctly reported that it could not find an IP address for it.                                        