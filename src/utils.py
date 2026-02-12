import json
import os
from typing import Dict, List


def transactions_total(file_path: str) -> list[dict]:
    """Загружает транзакции из JSON-файла."""
    try:
        #Проверяем существование файла
        if not os.path.exists(file_path):
            return []
        #Открыть и прочитать файл
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            #Проверка форматирования
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                return data
            else:   #Иначе возвращается пустой список
                return []
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Файл JSON не корректен")
    except ValueError:
        raise ValueError("Не удалось преобразить сумму в число")
    except Exception as e:
        raise Exception(f"Это общее исключение{e}")
