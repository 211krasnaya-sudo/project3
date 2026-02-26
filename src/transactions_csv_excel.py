from pathlib import Path
from typing import Union, List, Dict, Hashable, Any

import pandas as pd



file_csv = "transactions.csv"
excel_file = "transactions.excel.xlsx"

def reading_transaction_csv(file_csv: Union[str, Path]) -> List[Dict[Hashable, Any]]:
    """Функция считывает финансовые операции из CSV-файла."""
    try:
        with open(file_csv, encoding="utf-8") as file:
            reader = pd.read_csv(file_csv, sep=";")
            return reader.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_csv} не найден!")
        return []
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла {e}")
        return []


def reading_transaction_excel(excel_file: str) -> list[dict]:
    """Функция считывает финансовые операции из EXCEL-файла."""
    try:
        with open(file_csv, encoding="utf-8") as file:
            reader = pd.read_excel(excel_file)
            return reader.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_csv} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении EXCEL-файла {e}")
        return []


if __name__ == '__main__':
    print(reading_transaction_csv(file_csv))

if __name__ == '__main__':
    print(reading_transaction_excel(excel_file))
