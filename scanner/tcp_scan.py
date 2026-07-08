from scanner.models import ScanResult
import socket
import time


class TCPScanner:

    def __init__(self, timeout=1):

        self.timeout = timeout

    def scan(self, host, port):

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(self.timeout)

        start = time.perf_counter()

        result = sock.connect_ex((host, port))

        latency = round(
            time.perf_counter() - start,
            4
        )

        service = ""

        try:
            service = socket.getservbyport(port)
        except OSError:
            service = "unknown"

        sock.close()

        if result == 0:

            return ScanResult(
                port=port,
                protocol="TCP",
                status="Open",
                service=service,
                latency=latency
            )

        return None