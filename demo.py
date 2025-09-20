from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

try:
    2/0
except Exception as e:
    raise USvisaException(e, sys)

logging.info("Welcome to our custom log")