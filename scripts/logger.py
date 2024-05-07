__author__ = "Kaya Arkin"
__date__ = "21/04/2024"

import logging
from datetime import datetime
from typing import TypeVar

T = TypeVar('T')

class Logger:
    """Class used for logging script info. Includes methods for raising 
    exceptions.
    """    
    
    ## Log file output variables.
    __LOG_OUT_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    __LOG_PRINT_FORMAT = "{log_time} - {level} - {msg}"
    __DATE_TIME_OUT_FORMAT = '%m/%d/%Y %H:%M:%S'
    __START_TEXT = "Log started as '{filename}'."
    
    ## Level Names
    __INFO = "INFO"
    __WARNING = "WARNING"
    __ERROR = "ERROR"
    __CRITICAL = "CRITICAL"
    
    ## Error types
    TYPE_ERROR = 0
    KEY_ERROR = 1
    
    ##Exception Error Msgs
    __INCORRECT_TYPE = "'{value}' is of type {value_type}, expected {expected_type}."
    __INCORRECT_LEN = "'{data}' is of length {data_length}, expected {expected_length}."
    __INCORRECT_KEY = "'{key}' wasn't found in dictonary."
    
    
    
    def __init__(self, 
                 filename: str, 
                 level: int = logging.INFO):
        """Sets up logger file & adds a log stating the log has started.

        Args:
            filename (str): filename of the log file.
            level (int, optional): Level of logs recorded. Defaults to 
            logging.INFO.
        """         
        
        log_start_time = datetime.now().strftime('%m%d%y_%H%M%S')

        log_filename = f"{filename}_{log_start_time}.log"    
        
        logging.basicConfig(
            filename = log_filename, 
            format = self.__LOG_OUT_FORMAT,
            datefmt = self.__DATE_TIME_OUT_FORMAT,
            level = level)
        
        log_start_text = self.__START_TEXT.format(filename = log_filename)
        
        Logger.log_info(log_start_text)
        
        
    def __print_log(level: str, msg:str):
        """Prints a log to the terminal.

        Args:
            level (str): Level of the log.
            msg (str): Log message.
        """        
        
        log_time = datetime.now().strftime(Logger.__DATE_TIME_OUT_FORMAT)
        
        print(Logger.__LOG_PRINT_FORMAT.format(log_time = log_time, 
                                               level = level,
                                               msg = msg))
        
    def log_info(msg: str):
        """Creates a log with the level INFO.

        Args:
            msg (str): Log message.
        """        
   
        Logger.__print_log(Logger.__INFO, msg)
        
        logging.info(msg)
        
    
    def log_warning(msg: str):
        """Creates a log with the level WARNING.

        Args:
            msg (str): Log message.
        """        
        
        Logger.__print_log(Logger.__WARNING, msg)
        
        logging.warning(msg)
        
        
    def log_error(msg: str):
        """Creates a log with the level ERROR.

        Args:
            msg (str): Log message.
        """        
        
        Logger.__print_log(Logger.__ERROR, msg)
        
        logging.error(msg)
        
        
    def log_critical(msg: str):
        """Creates a log with the level CRITICAL.

        Args:
            msg (str): Log message.
        """        
        
        Logger.__print_log(Logger.__CRITICAL, msg)
        
        logging.critical(msg)
    
    
    def raise_exception(error_msg: str, 
                        error_type: int = 0, 
                        additional_text: str = None):
        """Raises an exception & adding it to the log.

        Args:
            error_msg (str): Message describing the exception.
            error_type (int, optional): Error message type. Logger contains
            variables defining the error numbers. Defaults to 0.
            additional_text (str, optional): Additional text to be added to the 
            error msg. Defaults to None.
        """        
        
        if additional_text != None:
            error_msg = additional_text + " " + error_msg
        
        logging.critical(error_msg)
        
        if error_type == Logger.TYPE_ERROR:
            raise TypeError(error_msg)
        
        elif error_type == Logger.KEY_ERROR:
            raise KeyError(error_msg)

        
    def raise_incorrect_type(value: any, 
                             expected_type: T, 
                             additional_text: str = None) -> bool:
        """Returns False if the value is of the correct object type, otherwise 
        raises an exception for values being the incorrect object type.

        Args:
            value (any): Value.
            expected_type (T): Expected type for the value.
            additional_text (str, optional): Additional text to be added to the 
            error msg. Defaults to None.

        Returns:
            bool: Returns False if the data is of correct object type.
        """          
        
        if type(value) == expected_type or type(value).__bases__[0] == expected_type:
            return False
        
        else:  
            error_msg = Logger.__INCORRECT_TYPE.format(
                value = value, 
                value_type = type(value),
                expected_type = expected_type)
            
            Logger.raise_exception(error_msg, Logger.TYPE_ERROR, additional_text)
            
            
    def raise_incorrect_len(data: any,
                            expected_length: int,
                            additional_text: str = None) -> bool:
        """Returns False if the data is the correct length, otherwise raises an 
        exception for data being the incorrect length.

        Args:
            data (any): Data.
            expected_length (int): Expected length of the data.
            additional_text (str, optional): Additional text to be added to the 
            error msg. Defaults to None.

        Returns:
            bool: Returns False if the data is of correct length.
        """        
        
        if len(data) == expected_length:
            return False
        
        else:
            error_msg = Logger.__INCORRECT_LEN.format(
                data = data, 
                data_length = len(data),
                expected_length = expected_length)
            
            Logger.raise_exception(error_msg, Logger.TYPE_ERROR, additional_text)
        

    def raise_key_error(dictonary: dict,
                        key: any,
                        additional_text: str = None) -> bool:
        """Returns False if the key is found within the dict, otherwise raises a
        key error.

        Args:
            dictonary (dict): Dictonary.
            key (any): Expected key.
            additional_text (str, optional): Additional text to be added to the 
            error msg. Defaults to None. Defaults to None.

        Returns:
            bool: Returns False if the key is valid within the dict.
        """        
        
        
        if key in dictonary:
            return False
        
        else:
            error_msg = Logger.__INCORRECT_KEY.format(key = key)
            
            Logger.raise_exception(error_msg, Logger.KEY_ERROR, additional_text)
        
        
