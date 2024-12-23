from src.logger import logging
from src.exception import USvisaException
import sys
from src.pipline.training_pipeline import *

abc=TrainPipeline()
a=abc.start_data_ingestion()
abc.start_data_validation(a)