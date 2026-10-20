"""Read-only support checks. Python 3 standard library only."""
import argparse
import concurrent.futures
import datetime
import json
import platform
import shutil
import socket
from pathlib import Path


def disk_check(path):
    usage = shutil.disk_usage(path)
    percent = round(100 * usage.free / usage.total, 1)
    return {"free_gib": round(usage.free / 2**30, 2),
            "total_gib": round(usage.total / 2**30, 2),
            "free_percent": percent,
            "status": "REVIEW" if percent < 15 else "OK"}


def resolve_host(host, timeout=5):
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    future = pool.submit(socket.getaddrinfo, host, None)
    try:
        addresses = sorted({entry[4][0] for entry in future.result(timeout=timeout)})
        return {"host": host, "status": "RESOLVED", "addresses": addresses}
    except concurrent.futures.TimeoutError:
        return {"host": host, "status": "TIMEOUT", "detail": "Resolver exceeded timeout"}
    except OSError as error:
        return {"host": host, "status": "FAILED", "detail": str(error)}
    finally:
        pool.shutdown(wait=False, cancel_futures=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--disk", default=str(Path.home()), help="Existing path to check")
    parser.add_argument("--host", help="Optional hostname-resolution check")
    parser.add_argument("--output", help="New JSON report path; existing files are protected")
    args = parser.parse_args()
    report = {"timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "system": {"os": platform.system(), "release": platform.release(),
                         "architecture": platform.machine(), "python": platform.python_version()}}
    try:
        report["disk"] = disk_check(args.disk)
    except OSError as error:
        report["disk"] = {"status": "ERROR", "detail": str(error)}
    report["hostname_resolution"] = resolve_host(args.host) if args.host else {"status": "SKIPPED"}
    rendered = json.dumps(report, indent=2)
    print(rendered)
    if args.output:
        try:
            with open(args.output, "x", encoding="utf-8") as output:
                output.write(rendered + "\n")
        except OSError as error:
            parser.exit(1, f"Could not save report: {error}\n")


if __name__ == "__main__":
    main()
