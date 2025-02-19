import logging

def log(filename=None):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            if filename != None:
                logging.basicConfig(level=logging.INFO, filename=filename, filemode="w")
                logging.info(f"Name function: {func}")
                try:
                    func(*args, **kwargs)
                    logging.info(f"ok")
                except Exception as e:
                    logging.error(f"error: {e}.")
            else:
                logging.info(f"Name function: {func}")
                try:
                    func(*args, **kwargs)
                    logging.info(f"ok")
                except Exception as e:
                    logging.error(f"error: {e}.")
        return wrapper
    return my_decorator
