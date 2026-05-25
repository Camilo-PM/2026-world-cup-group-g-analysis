from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
HTML_DIR = RAW_DIR / "html"
PROCESSED_DIR = DATA_DIR / "processed"
FINAL_DIR = DATA_DIR / "final"

TEAMS = {
    "Japan": [
        HTML_DIR / "japan.html",
        HTML_DIR / "japan_2025.html",
    ],
    "Netherlands": [
        HTML_DIR / "netherlands.html",
        HTML_DIR / "netherlands_2024.html",
        HTML_DIR / "netherlands_2025.html",
    ],
    "Sweden": [
        HTML_DIR / "sweden.html",
        HTML_DIR / "sweden_2024.html",
        HTML_DIR / "sweden_2025.html",
    ],
    "Tunisia": [
        HTML_DIR / "tunisia.html",
        HTML_DIR / "tunisia_2025.html",
    ],
}

LAST_N_MATCHES = 10

