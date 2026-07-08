"""
Creates a readable scan plan.
"""


class ScanPlanner:

    @staticmethod
    def generate(plan):

        return f"""
Target       : {plan['target']}

Scan Type    : {plan['scan_type']}

Ports        : {plan['ports']}

Threads      : {plan['threads']}

Timeout      : {plan['timeout']} sec

Ready to start scan.
"""