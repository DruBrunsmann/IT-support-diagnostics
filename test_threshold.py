from collections import namedtuple
from unittest.mock import patch
from diagnostics import disk_check

Usage = namedtuple("Usage", "total used free")

# Simulate 12% free space without changing the real disk.
with patch("diagnostics.shutil.disk_usage",
           return_value=Usage(1000, 880, 120)):
    result = disk_check(".")
    print(result)
    assert result["status"] == "REVIEW"

print("Threshold test passed.")