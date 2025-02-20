import logging
from functools import wraps


def log(filename=None):
    def my_decorator(func):
        '''Выводит логи функции с названием'''
        @wraps(func)
        def wrapper(*args, **kwargs):
            if filename != None:
                logging.basicConfig(level=logging.INFO, filename=filename, filemode="w")
                logging.info(f"Name function: {str(func)[10:-23]}")
                try:
                    func(*args, **kwargs)
                    logging.info(f"ok")
                except Exception as e:
                    logging.error(f"error: {e}.")
            else:
                result = ''
                result += f'Name func: {str(func)[10:-23]}\n'
                try:
                    func(*args, **kwargs)
                    result += f"ok"
                except Exception as e:
                    result += f"error: {e}. Inputs: {args}"
                return print(result)
        return wrapper
    return my_decorator
