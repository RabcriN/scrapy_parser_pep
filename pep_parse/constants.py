from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%dT%H-%M-%S'
DATETIME = datetime.now().strftime(DATETIME_FORMAT)
START_URLS = ['https://peps.python.org/']
