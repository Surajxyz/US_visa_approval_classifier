from src.logger import logging
from src.exception import USvisaException
import sys
logging.info("log have been created")


try:
    a=3/0
except Exception as e:
    raise USvisaException(e,sys)