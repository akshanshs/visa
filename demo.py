from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

from us_visa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()

print("Demo run was successful")

logging.info("Welcome to our custom log")