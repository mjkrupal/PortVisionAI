"""
Main Scan Engine
"""

from concurrent.futures import ThreadPoolExecutor

from scanner.tcp_scan import TCPScanner
from scanner.port_utils import parse_ports


class ScanEngine:

    def __init__(self):

        self.scanner = TCPScanner()

    def scan(self, target, port_text):

        ports = parse_ports(port_text)

        open_ports = []

        with ThreadPoolExecutor(max_workers=200) as executor:

            futures = {
                executor.submit(
                    self.scanner.scan,
                    target,
                    port
                ): port

                for port in ports
            }

            for future in futures:

                if future.result():

                    open_ports.append(
                        futures[future]
                    )

        return sorted(open_ports)