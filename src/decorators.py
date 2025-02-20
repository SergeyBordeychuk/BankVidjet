import logging
from functools import wraps


def log(filename=None):
    def my_decorator(func):
        """Выводит логи функции с названием"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            global result_func
            if filename != None:
                logging.basicConfig(level=logging.INFO, filename=filename, filemode="a")
                logging.info(f"Name function: {str(func)[10:-23]}")
                try:
                    func(*args, **kwargs)
                    return logging.info(f"ok")
                except Exception as e:
                    return logging.error(f"error: {e}. Inputs: {args} {kwargs}")
            else:
                result = ""
                result += f"Name func: {str(func)[10:-23]}\n"
                try:
                    result_func = func(*args, **kwargs)
                    result += f"ok"
                except Exception as e:
                    result += f"error: {e}. Inputs: {args} {kwargs}"
                print(result)
                return result_func

        return wrapper

    return my_decorator
