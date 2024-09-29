from sensors.exception import SensorException
import os
import sys
from sensors.logger import logging

def test_execption():
    try:
        logging.info("my code")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)


if __name__=="__main__":
    try:
        test_execption()
    except Exception as e:
        print(e)
