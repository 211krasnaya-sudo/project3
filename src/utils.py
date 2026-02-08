import json
import os
from typing import Dict, List


def load_transactions(file_path: str) -> List[Dict]:
    """Загружает транзакции из JSON-файла."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
        except json.JSONDecodeError:
            return []
