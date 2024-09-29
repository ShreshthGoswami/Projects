import logging
import os
import sys
from datetime import datetime

# Create log file with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")  # Directory for log files
os.makedirs(logs_dir, exist_ok=True)  # Create directory if it doesn't exist
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)  # Complete log file path

# Setup logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO  # Corrected: removed parentheses
)
