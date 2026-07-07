from dataclasses import dataclass


@dataclass
class ScanResult:

    port: int

    service: str

    protocol: str

    status: str

    banner: str = ""

    version: str = ""