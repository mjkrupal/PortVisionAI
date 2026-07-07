import socket

from scanner.results import ScanResult

from scanner.port_database import COMMON_PORTS


class TCPScanner:

    def __init__(self, timeout=1):

        self.timeout = timeout

    def scan(self, target, port):

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(self.timeout)

        try:

            result = sock.connect_ex((target, port))

            if result == 0:

                service = COMMON_PORTS.get(
                    port,
                    "Unknown"
                )

                sock.close()

                return ScanResult(
                    port=port,
                    service=service,
                    protocol="TCP",
                    status="Open"
                )

        except Exception:

            pass

        finally:

            sock.close()

        return None