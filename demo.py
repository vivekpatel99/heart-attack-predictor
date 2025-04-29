# # below code is to check the exception config
import sys

from src.exception import MyException
from src.logger import logging

try:
    a = 1 + "Z"
except Exception as e:
    logging.info(e)
    raise MyException(e, sys) from e
