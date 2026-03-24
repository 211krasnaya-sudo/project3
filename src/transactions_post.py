import re
from typing import List, Dict, Any


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """Ищет транзакции по строке поиска в описании."""
    pattern = re.compile(re.escape(search), re.IGNORECASE)  # Игнорирует регистр
    return [transaction for transaction in data if pattern.search(transaction['description'])]

def process_bank_operations(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Считает количество операций по категориям."""
    count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction['description'].lower()
        for category in categories:
            if category in description.lower():
                count[category] += 1
    return count
