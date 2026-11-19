
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

OUTPUT_FOLDER = BASE_DIR / "generated_qr"
LOG_FOLDER = BASE_DIR / "logs"

DEFAULT_FILL_COLOR = "black"
DEFAULT_BACK_COLOR = "white"

BOX_SIZE = 10
BORDER_SIZE = 4

OUTPUT_FOLDER.mkdir(exist_ok=True)
LOG_FOLDER.mkdir(exist_ok=True)
