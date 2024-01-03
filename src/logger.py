import logging 
import os 
from datetime import datetime 

#any execution that happens, need to be able to log the info into the logger 



LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) 
#the log created will be with respect to the current directory 
#the file will start with "log" and then the log file name that was created 

os.makedirs(logs_path, exist_ok=True) 
#even though there is a file, keep an appending the files inside that 

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

#whenever I use logging.INFO and write any print message, then it will use the following Config
#will create the file with LOG_FILE_PATH and print the message with that particular format 
logging.basicConfig(
    filename = LOG_FILE_PATH, 
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", #how my message will get printed 
    level = logging.INFO, 

)

