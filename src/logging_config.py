import logging


def setup_logging(LOG_FILE=None, LOG_FILE_UTILS=None):
    #Создаем базовый логгер
    logging.basicConfig(
        level=logging.INFO,    #Уровень логирования
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=LOG_FILE,
        filemode='w'
    )
    logger = logging.getLogger(__name__)

    # Создаем логгеры для модулей masks, utils
    masks_logger = logging.getLogger('masks.log')
    masks_logger.setLevel(logging.INFO)

    utils_logger = logging.getLogger('utils.log')
    utils_logger.setLevel(logging.INFO)

    #Создаем обработчик для записи логов в файл для модулей masks, utils
    masks_file_handler = logging.FileHandler(LOG_FILE, mode='w', encoding='utf-8')

    utils_file_handler = logging.FileHandler(LOG_FILE_UTILS, mode='w', encoding='utf-8')

    #Создаем форматер для логов для модулей masks, utils
    masks_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    masks_file_handler.setFormatter(masks_formater)

    utils_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    utils_file_handler.setFormatter(utils_formater)

    #Добавляем обработчик к логгеру для модулей masks, utils
    masks_logger.addHandler(masks_file_handler)

    utils_logger.addHandler(utils_file_handler)

    return logger
