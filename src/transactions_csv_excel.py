from pathlib import Path
from typing import Dict, List

import pandas as pd


def reading_transaction_csv(file_path: str) -> List[Dict]:
    """Функция считывает финансовые операции из CSV-файла."""
    try:
        # with open(file_csv, encoding="utf-8") as file:
        reader = pd.read_csv(file_path)
        return reader.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден!")
        return []
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла {e}")
        return []


def reading_transaction_excel(file_path: str) -> list[dict]:
    """Функция считывает финансовые операции из EXCEL-файла."""
    try:
        reader = pd.read_excel(file_path)
        return reader.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении EXCEL-файла {e}")
        return []


if __name__ == '__main__':
    print(reading_transaction_csv)
