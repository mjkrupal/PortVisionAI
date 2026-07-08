"""
Simple Prompt Parser
"""

import re


class PromptParser:

    @staticmethod
    def parse(prompt: str):

        prompt = prompt.lower()

        plan = {
            "target": "",
            "scan_type": "TCP Connect",
            "ports": "Top 100",
            "threads": 200,
            "timeout": 1.0,
        }

        ip = re.search(r"(\d+\.\d+\.\d+\.\d+)", prompt)

        if ip:
            plan["target"] = ip.group()

        if "localhost" in prompt:
            plan["target"] = "127.0.0.1"

        if "full" in prompt:
            plan["ports"] = "1-65535"

        if "web" in prompt:
            plan["ports"] = "80,443,8080,8443"

        if "udp" in prompt:
            plan["scan_type"] = "UDP"

        if "syn" in prompt:
            plan["scan_type"] = "SYN"

        if "quick" in prompt:
            plan["threads"] = 300

        return plan