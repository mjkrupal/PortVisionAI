"""
Global Application State
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ScanSummary:

    target: str = ""

    scan_type: str = ""

    ports: str = ""

    duration: float = 0.0

    open_ports: int = 0

    closed_ports: int = 0

    filtered_ports: int = 0

    risk_score: str = "Unknown"

    completed: bool = False

    summary: str = ""

    recommendations: list = field(default_factory=list)


@dataclass
class AppState:

    ai_model: str = "llama3.2"

    ollama_connected: bool = False

    current_scan: ScanSummary = field(default_factory=ScanSummary)

    last_results: List = field(default_factory=list)

    activity_log: List[str] = field(default_factory=list)

    last_prompt: str = ""


state = AppState()