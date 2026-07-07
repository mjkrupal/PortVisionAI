from scanner.scanner_engine import ScannerEngine
from scanner.utils import validate_target


target = validate_target("scanme.nmap.org")

scanner = ScannerEngine(timeout=1)

results = scanner.scan_ports(
    target,
    [22, 80, 443],
    threads=10
)

for result in results:
    print(result)