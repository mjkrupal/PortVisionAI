import ipaddress
import socket


def validate_target(target):
    """
    Validate an IP address or resolve a hostname.
    Returns the IP address.
    """
    try:
        ipaddress.ip_address(target)
        return target
    except ValueError:
        try:
            return socket.gethostbyname(target)
        except socket.gaierror:
            raise ValueError("Invalid IP address or hostname.")