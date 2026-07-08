"""
TCP Scanner
"""

import socket


class TCPScanner:

    def __init__(self, timeout=1):

        self.timeout = timeout

    def scan(self, host, port):

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(self.timeout)

        result = sock.connect_ex((host, port))

        sock.close()

        return result == 0