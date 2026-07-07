from scanner.scanner_engine import ScannerEngine
from scanner.validator import TargetValidator


target = TargetValidator.validate(
    "scanme.nmap.org"
)

scanner = ScannerEngine()

results = scanner.scan_ports(
    target,
    [22, 80, 443],
    threads=10
)

print()

print("=" * 50)

print("Scan Results")

print("=" * 50)

for item in results:

    print(item)