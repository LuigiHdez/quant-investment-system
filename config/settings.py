import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
REPORTS_DIR = BASE_DIR / "reports"
LOGS_DIR = BASE_DIR / "logs"

for d in [DATA_DIR, MODELS_DIR, REPORTS_DIR, LOGS_DIR]:
    d.mkdir(exist_ok=True)

SYMBOLS = [s.strip() for s in os.getenv("SYMBOLS", "AAPL").split(",")]
DATA_SOURCE = os.getenv("DATA_SOURCE", "yfinance")
TRAIN_START_DATE = os.getenv("TRAIN_START_DATE", "2015-01-01")
RETRAIN_FREQ_DAYS = int(os.getenv("RETRAIN_FREQ_DAYS", "7"))
