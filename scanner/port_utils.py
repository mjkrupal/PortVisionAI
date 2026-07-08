"""
Port Utilities
"""

COMMON_PORTS = [
    20,21,22,23,25,53,80,110,135,139,
    143,443,445,465,587,993,995,
    1433,1521,3306,3389,5432,
    5900,6379,8080,8443
]


def parse_ports(port_text):

    if port_text == "Top 100":
        return COMMON_PORTS

    if "," in port_text:
        return [
            int(p.strip())
            for p in port_text.split(",")
        ]

    if "-" in port_text:

        start,end = port_text.split("-")

        return list(
            range(
                int(start),
                int(end)+1
            )
        )

    return COMMON_PORTS