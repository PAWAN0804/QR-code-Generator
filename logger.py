import logging
from config import LOG_FOLDER

logging.basicConfig(
    filename=LOG_FOLDER / "qr_generator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)