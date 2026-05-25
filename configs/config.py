from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
HTML_DIR = RAW_DIR / "html"
PROCESSED_DIR = DATA_DIR / "processed"
FINAL_DIR = DATA_DIR / "final"

TEAMS = {
    "Belgium": [
        HTML_DIR / "belgium.html",
        HTML_DIR / "belgium_2025.html",
    ],
    "Egypt": [
        HTML_DIR / "egypt.html",
        HTML_DIR / "egypt_2025.html",
    ],
    "Iran": [
        HTML_DIR / "iran.html",
        HTML_DIR / "iran_2025.html",
    ],
    "New Zealand": [
        HTML_DIR / "new_zealand.html",
        HTML_DIR / "new_zealand_2025.html",
    ],
}

LAST_N_MATCHES = 10

