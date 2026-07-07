import socket
from concurrent.futures import ThreadPoolExecutor


class ScannerEngine:

    def __init__(self, timeout=1):
        self.timeout = timeout

    def scan_port(self, target, port):
        """Scan a single TCP port."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)

            result = sock.connect_ex((target, port))
            sock.close()

            if result == 0:
                return {
                    "port": port,
                    "status": "Open"
                }

        except Exception:
            pass

        return None

    def scan_ports(self, target, ports, threads=100):
        """Scan multiple TCP ports."""
        results = []

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [
                executor.submit(self.scan_port, target, port)
                for port in ports
            ]

            for future in futures:
                result = future.result()

                if result:
                    results.append(result)

        return results