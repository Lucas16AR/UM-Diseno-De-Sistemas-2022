from abc import ABC
from abc import abstractmethod
from datetime import datetime
import os
from dotenv import load_dotenv

#Product
class Logger(ABC):
    
    @abstractmethod
    def error(self, msg):
        pass
    
    @abstractmethod
    def debug(self, msg):
        pass
    
    @abstractmethod
    def info(self, msg):
        pass

    @abstractmethod
    def warn(self, msg):
        pass

#Concrete Product
class FileLogger(Logger):

    __new_file = 'new_file.log'

    def __print(self,level,msg): #level hace referencia a error, debug, info
        with open(self.__new_file, 'a') as f:
            f.write(f'{datetime.now()}  {level}  {msg} \n')

    def error(self, msg):
        self.__print('ERROR', msg)

    def debug(self, msg):
        self.__print('DEBUG', msg)
    
    def info(self, msg):
        self.__print('INFO', msg)

    def warn(self, msg):
        self.__print('WARN', msg)


#Concrete Product
class ConsoleLogger(Logger):

    def __print(self,level,msg):
        print(f'{datetime.now()} {level} {msg}')
    
    def error(self, msg):
        self.__print('ERROR', msg)
    
    def debug(self, msg):
        self.__print('DEBUG', msg)
    
    def info(self, msg):
        self.__print('INFO', msg)
    
    def warn(self, msg):
        self.__print('WARN', msg)

#Concrete Product
class JsonLogger(Logger):

    __new_file = 'new_file.json'

    def __print(self,level,msg):
        with open(self.__new_file, 'a') as f:
            f.write(f'{{"time": "{datetime.now()}", "level": "{level}", "msg": "{msg}"}} \n')
    
    def error(self, msg):
        self.__print('ERROR', msg)
    
    def debug(self, msg):
        self.__print('DEBUG', msg)
    
    def info(self, msg):
        self.__print('INFO', msg)
    
    def warn(self, msg):
        self.__print('WARN', msg)

#Creator
class LoggerFactory(ABC):
    
    @abstractmethod
    def get_logger(self):
        pass
    
#Concrete Creator   
class LoggerFactoryImpl(LoggerFactory):
    
    def __init__(self, logger_type):
        self.__logger_type = logger_type
    
    def get_logger(self): 
        dict = {
            'file': FileLogger(),
            'console': ConsoleLogger(),
            'json': JsonLogger()
        }
        return dict[self.__logger_type]

if __name__ == '__main__':
    load_dotenv()
    logger_type = os.getenv('LOGGER_TYPE')
    logger = LoggerFactoryImpl(logger_type).get_logger()
    logger.error('Error')
    logger.debug('Debug')
    logger.info('Info')
    logger.warn('tengomiedo')
