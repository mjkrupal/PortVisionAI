"""
PortVision AI Configuration
"""

from pathlib import Path

APP_NAME = "PortVision AI"
APP_VERSION = "1.0.0"

BASE_DIR = Path(__file__).resolve().parent

ASSETS_DIR = BASE_DIR / "assets"
ICON_DIR = BASE_DIR / "icons"
LOG_DIR = BASE_DIR / "logs"
DATABASE_DIR = BASE_DIR / "database"
REPORT_DIR = BASE_DIR / "reports"

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 850

DEFAULT_THEME = "dark"

ACCENT_COLOR = "#00FF66"

import os
from dotenv import load_dotenv

load_dotenv()

# -----------------------
# OpenAI
# -----------------------

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-5.5"
)

LOG_LEVEL = "INFO"

MAX_THREADS = 200

DEFAULT_TIMEOUT = 1.0

