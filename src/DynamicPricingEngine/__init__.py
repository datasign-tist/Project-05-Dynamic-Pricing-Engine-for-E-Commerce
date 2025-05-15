import os
import sys
import logging
from logging.handlers import RotatingFileHandler

# Define log format
LOG_FORMAT = "[%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d] → %(message)s"

# Log directory and file path
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "running_logs.log")

# Log level
LOG_LEVEL = logging.INFO

# File handler with rotation
file_handler = RotatingFileHandler(
    LOG_FILE, maxBytes=5*1024*1024, backupCount=3
)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Stream handler (console)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Configure logger
logger = logging.getLogger("DynamicPricingEngineLogger")
logger.setLevel(LOG_LEVEL)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.propagate = False
