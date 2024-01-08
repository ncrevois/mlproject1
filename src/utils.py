# all the common things we are going want to import and use 

import os 
import sys 
import numpy as np 
import pandas as pd 
import dill 
from sklearn.metrics import r2_score

from src.exception import CustomException

def save_object(file_path, obj):
    try: 
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True) 

        with open(file_path, "wb") as file_obj: 
            dill.dump(obj, file_obj) 

    except Exception as e: 
        raise CustomException(e,sys)
    

def evaluate_models(X_train,y_train, X_test, y_test ,models):
    try:
        report = {}

        for i in range(len(list(models))):  #go through each model 
            model = list(models.values())[i]  #get the model 

            model.fit(X_train,y_train) #Train model 

            y_train_pred = model.predict(X_train) #use trained model to predict 
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred) #compute the r2 score on training data 
            test_model_score = r2_score(y_test, y_test_pred)   #compute the r2 score on test data 

            report[list(models.keys())[i]] = test_model_score #store values of score for that model
        
        return report 
    except Exception as e:
            raise CustomException(e,sys)