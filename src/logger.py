import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
LOG_PATH = os.path.join(os.getcwd(),"logs",datetime.now().strftime('%d_%m_%Y'))
os.makedirs(LOG_PATH, exist_ok= True)

LOG_FILE_PATH = os.path.join(LOG_PATH,LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(levelname)s %(message)s",
    datefmt= "%Y-%m-%d %H:%M:%S",
    level= logging.INFO
)
