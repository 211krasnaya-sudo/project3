import logging
import os
from typing import Optional


def setup_logging(LOG_FILE: Optional[str] = None, LOG_FILE_UTILS: Optional[str] = None) -> logging.Logger:
    logging.basicConfig(      # Создаем базовый логгер
        level=logging.INFO,      # Уровень логирования
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=LOG_FILE,
        filemode='w'
    )
    if LOG_FILE is None:
        LOG_FILE = os.path.join('logs', 'masks.log')
    logger = logging.getLogger('logs')

    if LOG_FILE_UTILS is None:
        LOG_FILE_UTILS = os.path.join('logs', 'utils.log')
    logger = logging.getLogger('logs')

    # Создаем логгеры для модулей masks, utils
    masks_logger = logging.getLogger('masks.log')
    masks_logger.setLevel(logging.INFO)

    utils_logger = logging.getLogger('utils.log')
    utils_logger.setLevel(logging.INFO)

    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')
    logger.exception('Exception message')

    # Создаем обработчик для записи логов в файл для модулей masks, utils
    masks_file_handler = logging.FileHandler(LOG_FILE, mode='w', encoding='utf-8')
    utils_file_handler = logging.FileHandler(LOG_FILE_UTILS, mode='w', encoding='utf-8')

    # Создаем форматер для логов для модулей masks, utils
    masks_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    masks_file_handler.setFormatter(masks_formater)

    utils_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    utils_file_handler.setFormatter(utils_formater)

    # Добавляем обработчик к логгеру для модулей masks, utils
    masks_logger.addHandler(masks_file_handler)

    utils_logger.addHandler(utils_file_handler)

    return logger
