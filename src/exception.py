import sys 
import logging

def error_message_detail(error, error_detail:sys):
    '''when an error is raised, 
    I want to push my own custom message'''
    _,_,exc_tb = error_detail.exc_info()  #gives you info on which file and line number the exception has occured 
    file_name = exc_tb.tb_frame.f_code.co_filename 
    error_message = "Error occured in python script name [{0}], line number [{1}], error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message 


class CustomException(Exception):   #CustomException class is inheriting the parent Exception 
    def __init__(self, error_message, error_detail:sys):  #over-riding the init from Exception 
        super().__init__(error_message) 
        self.error_message = error_message_detail(error_message, error_detail = error_detail) 
    
    def __str__(self): #when you print this, it will print the error_message
        return self.error_message
