from datetime import datetime

def my_logger(original_function):
    import logging
    logging.basicConfig(filename=f'{original_function.__name__}.log',level=logging.INFO)
    def wrapper(*args,**kwargs):
        logging.info(f"Ran with args:{args} and kwargs:{kwargs}")
        return original_function(*args,**kwargs)
    return wrapper

def my_timer(original_function):
    from time import perf_counter
    def wrapper(*args,**kwargs):
        start_time=perf_counter()
        return_value=original_function(*args,**kwargs)
        end_time=perf_counter()
        print(f"Time taken by {original_function.__name__} is {end_time-start_time}")


class DecoratorClass(object):
    def __init__(self,original_function):
        self.original_function=original_function
    def __call__(self,*args,**kwargs):
        print(f"call method executed this before {self.original_function.__name__}")
        return self.original_function(*args,**kwargs)

def decorator_function(original_function):
    def wrapper():
        print("hello")
        original_function()
        print("hi")
    return wrapper

def main_decorator_function(original_function):
    def wrapper(*args,**kwargs):
        print(f"Inside wrapper function and calling: {original_function.__name__}")
        original_function(*args,**kwargs)
        print("exiting execution")
    return wrapper

def not_during_the_night(func):
    def wrapper():
        if 7<=datetime.now().hour <22:
            func()
        else:
            pass
    return wrapper

def my_decorator(func):
    def wrapper():
        print("Somethins is to be printed before function call")
        func()
        print("Somethins is to be printed after function call")
    return wrapper

def say_whee():
    print("Whee!")

@decorator_function
def say_yo():
    print("yo")

@DecoratorClass
def display_info(name,id):
    print(f"Person with name:{name} and id: {id}")

@my_logger
@my_timer
def check_logging():
    print("testing....")

if __name__=="__main__":
    # say_whee=my_decorator(say_whee)
    # say_whee=not_during_the_night(say_whee)
    # say_whee()
    # say_yo()
    # display_info("alex","1234")
    check_logging()