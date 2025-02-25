import logging
from functools import wraps


def log(filename=None):
    def my_decorator(func):
        """Выводит логи функции с названием"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            if filename != None:
                logging.basicConfig(level=logging.INFO, filename=filename, filemode="a")
                logging.info(f"Name function: {str(func)[10:-23]}")
                try:
                    result_func = func(*args, **kwargs)
                    logging.info(f"ok")
                    return result_func
                except Exception as e:
                    logging.error(f"error: {e}. Inputs: {args} {kwargs}")
                    return
            else:
                result = ""
                result += f"Name func: {str(func)[10:-23]}\n"
                try:
                    result_func = func(*args, **kwargs)
                    result += f"ok"
                    print(result)
                    return result_func
                except Exception as e:
                    result += f"error: {e}. Inputs: {args} {kwargs}"
                    print(result)
                    return

        return wrapper

    return my_decorator
