from dataclasses import dataclass


@dataclass
class ScanResult:

    port: int

    protocol: str

    status: str

    service: str

    banner: str = ""

    version: str = ""

    latency: float = 0

    risk: str = "Unknown"