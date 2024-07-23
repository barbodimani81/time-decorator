import time
import logging


# defining time calculator decorator
def time_decorator(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        stop = time.time()
        print(f"It took {stop - start} seconds")
        return result

    return wrapper


# defining logger decorator
def logger_decorator(function):
    def wrapper(*args, **kwargs):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(message)s')
        logger = logging.getLogger()
        logger.info(f"Function started")
        result = function(*args, **kwargs)
        logger.info(f"Function finished")
        return result

    return wrapper


# using the decorators on functions
@logger_decorator
@time_decorator
def say_hi(name):
    print(f"Hi {name}")


def main():
    say_hi(name='barbod')


if __name__ == "__main__":
    main()
