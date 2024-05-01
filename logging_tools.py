### TO_DO
# 1) Explore caching - https://realpython.com/lru-cache-python/ 
#2) Pickle over logging

import os, sys

#######################################
## Prepare the Environment
#######################################
try:
    import logging
except:
    os.system('pip install logging')
    import logging

#######################################
## Functions
#######################################
#--------------------------------------
def get_kwarg_count(**kwargs):
#--------------------------------------
    for k, v in kwargs.items():
        print(f'get_kwarg_count keyword argument: {k} = {v}')
    
    print(f"locals = {locals()} len(locals()) = {len(locals())}")  ## This is really cool for debugging!
    

#--------------------------------------
def set_basicConfig(**kwargs):
#--------------------------------------

    assert (len(kwargs) > 0 and isinstance(len(kwargs), int)), f"Func set_basicConfig expected some input (len>0), instead got {len(kwargs)}"    
    ## First, verify **kwargs HAS data using "assert"
    try:                               ## Now try applying the parameters sent to us
        my_logger.warning(**kwargs) #basicConfig(**kwargs)
        #my_logger.setLevel(logging.DEBUG)  ## This is important to the whole logging process
    except Exception as e:
        print("ERROR:", str(e))

#======================================
# Functions: Decorators
#======================================
def my_logger(orig_func):
#--------------------------------------
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.DEBUG)
    def my_logger_wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args}, kwargs:{kwargs}')
        return orig_func(*args, **kwargs)
    return my_logger_wrapper
#--------------------------------------
def my_timer(orig_func):
#--------------------------------------
    import time

    def my_timer_wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in {t2} sec')
        return result
    return my_timer_wrapper

#======================================
# Functions: TESTING
#======================================
# (Funtion test_simple_logger() will not show INFO and DEBUG by default)
#--------------------------------------
@my_logger
@my_timer
def test_simple_logger():
#--------------------------------------
    logging.debug('This is a logging debug message')
    logging.info('This is an logging info message')
    logging.warning('This is a logging warning message')
    logging.error('This is an logging error message')
    logging.critical('This is a logging critical message')

    my_logger.debug('This is a my_logger debug message')
    my_logger.info('This is a my_logger info message')
    my_logger.warning('This is a my_logger warning message')
    my_logger.error('This is a my_logger error message')
    my_logger.critical('This is a my_logger critical message')
#######################################
## Methods
#######################################


#######################################
## Counters and Initializations
#######################################
my_logger = logging.getLogger(__name__)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(f'{sys.argv[0]}.log')
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.DEBUG)

c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

my_logger.addHandler(c_handler)
my_logger.addHandler(f_handler)

my_logger.warning('This is a warning')
my_logger.error('This is an error')
my_logger.debug('This is a DEBUG msg')
#######################################
## Begin MAIN LOGIC Here.
#######################################
# #logging.basicConfig(level=logging.DEBUG,filename='C:\\Users\\User\\Desktop\\python\\tools\\logging\\app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
set_basicConfig(level=logging.DEBUG, filename='C:\\Users\\User\\Desktop\\python\\tools\\logging\\app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
my_logger.setLevel(logging.DEBUG)
my_logger.debug('This is a DEBUG msg')
test_simple_logger()



