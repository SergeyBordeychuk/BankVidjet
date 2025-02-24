import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transaction_list(path: str) -> list:
    """Функция возвращает транзакции из файла"""
    logger.info("Начало работы функции")
    try:
        logger.info(f"Попытка открыть файл по пути: {path}")
        with open(path, encoding="utf-8") as file_in:
            try:
                logger.info("Распаковка файла")
                data = json.load(file_in)
                if not isinstance(data, list):
                    logger.error("В файле нет списка")
                    return []
            except json.JSONDecodeError:
                logger.error("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return []
    logger.info("Конец работы функции")
    return data
