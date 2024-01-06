#read data from a main data source 
#split the data into train and test 

import sys
sys.path.insert(0, '/Users/nathaliecrevoisier/Documents/DataScience/mlproject1')


import os 
print("Current Working Directory:", os.getcwd())
import sys  #we will be using our CustomException
import pandas as pd 
from sklearn.model_selection import train_test_split 
from dataclasses import dataclass 
from src.logger import logging
from src.exception import CustomException


@dataclass
class DataIngestionConfig: 
    #inputs 
    project_root = '/Users/nathaliecrevoisier/Documents/DataScience/mlproject1'
    train_data_path: str = os.path.join(project_root, 'artifacts', "train.csv")  #later on, the data ingestion will save the train.csv file in this path
    test_data_path: str = os.path.join(project_root,'artifacts', "test.csv")
    raw_data_path: str = os.path.join(project_root,'artifacts', "data.csv")

class DataIngestion: 
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try: 
            df = pd.read_csv('/Users/nathaliecrevoisier/Documents/DataScience/mlproject1/notebook/data/stud.csv') 
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True) #get the directory name of this path, if it already exists we keep the folder don't have to delete and re-create 
        
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state = 42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
            )

        except Exception as e:  
            raise CustomException(e,sys)

if __name__ =="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
