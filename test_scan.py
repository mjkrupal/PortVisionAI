from scanner.scan_engine import ScanEngine

engine = ScanEngine()

ports = engine.scan(
    "127.0.0.1",
    "Top 100"
)

print(ports)