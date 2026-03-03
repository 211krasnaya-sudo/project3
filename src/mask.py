import logging
import os
from typing import Optional

from src.logging_config import setup_logging

logger = setup_logging()

LOG_DIR = 'logs'
LOS_FILE = os.path.join(LOG_DIR, 'masks.log')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


def get_mask_card_number(card_number: str, masks_logger=None) -> str:
    """ Маскирует номер карты, оставляя первые 6 и последние 4 цифры видимыми."""
    if masks_logger is None:
        masks_logger = logging.getLogger(__name__)
    masks_logger.info(f"Вызвана функция get_mask_card_number с card_number: {card_number}")
    # Преобразуем число в строку
    card_str = str(card_number)
    try:
        # Проверяем корректность длины номера карты
        if len(card_str) != 16:
            masks_logger.error(f"Неверный номер карты: {card_number}. Номер карты должен содержать 16 цифр.")
            raise ValueError("Номер карты должен содержать 16 цифр")
        # Фотмируем маску
        masked = (card_str[:4] + " " + card_str[4:6] + "**" + " " + "****" + " " + card_str[-4:])
        masks_logger.info(f"Номер карты успешно замаскирован. Результат: {card_number}.")
        return masked
    except ValueError as e:
        masks_logger.exception(f"Ошибка при маскировании номера карты: {e}")
        raise ValueError("Ошибка при маскировании номера карты")


def get_mask_account(account_number: int, masks_logger=None) -> str:
    """ Маскирует номер счёта по шаблону **xxxx"""
    if masks_logger is None:
        masks_logger = logging.getLogger(__name__)
    masks_logger.info(f"Вызвана функция get_mask_account с card_number: {account_number}")
    # Преобразуем число в строку
    account_str = str(account_number)
    try:
        # Проверяем минимальную длину номера счета
        if len(account_str) < 20:
            masks_logger.error(f"Неверный номер карты: {account_number}. Номер карты должен содержать 20 цифр.")
            raise ValueError("Номер счета должен содержать минимум 20 цифр")
        # Формируем маску
        masked = "**" + account_str[-4:]
        masks_logger.info(f"Номер карты успешно замаскирован. Результат: {account_number}.")
        return masked
    except ValueError as e:
        masks_logger.exception(f"Ошибка при маскировании номера счёта: {e}")
        raise ValueError("Ошибка при маскировании номера счёта")
