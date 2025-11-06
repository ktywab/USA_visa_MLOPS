from USA_visa_MLOPS.logger import logging
from USA_visa_MLOPS.exception import USvisaException
import sys

logging.info("Demo of USA Visa MLOPS project.")

try:
    1 / 0  # Intentional error to test USvisaException
except Exception as e:
    raise USvisaException(e, sys) from e