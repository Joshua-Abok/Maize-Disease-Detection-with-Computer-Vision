import os
import sys
import logging
    
    # timestamp logging your project: which type of info you want to store: 
    #                                       module the code is running: mess of off the logging 
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"  #create log folder
log_filepath = os.path.join(log_dir,"running_logs.log")    # create running_logs.log file & store log info
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),  # create running_logs.log handler
        logging.StreamHandler(sys.stdout)   # output on the terminal
    ]
)

logger = logging.getLogger("maizeDiseaseDetectionLogger")  #create logger object