import os


ROOT_DIR = os.path.dirname(__file__)  # корневой каталог
DATA_DIR = os.path.join(ROOT_DIR, "data")


PATH_JSON = os.path.join(DATA_DIR, "operations.json")     # путь json

PATH_CSV = os.path.join(DATA_DIR, "transactions.csv")     # путь csv
PATH_XLSX = os.path.join(DATA_DIR, "transactions_excel.xlsx")     # путь excel
