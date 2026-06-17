# Импортируем модуль для логирования
import logging
# Импортируем Path для работы с путями файлов
from pathlib import Path


def setup_logger(log_file="logs.txt"):
    """
    Функция настройки логирования
    log_file — имя файла для записи логов
    """
    # Создаём форматтер — формат сообщений в логах
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Создаём обработчик для записи в файл
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    # Устанавливаем формат для файлового обработчика
    file_handler.setFormatter(formatter)
    
    # Создаём обработчик для вывода в консоль
    console_handler = logging.StreamHandler()
    # Устанавливаем формат для консольного обработчика
    console_handler.setFormatter(formatter)
    
    # Получаем корневой логгер
    logger = logging.getLogger()
    # Устанавливаем уровень логирования
    logger.setLevel(logging.INFO)
    
    # Добавляем обработчики к логгеру
    logger.addHandler(file_handler)  # Файловый обработчик
    logger.addHandler(console_handler)  # Консольный обработчик
    
    # Логируем успешную настройку
    logging.info("Логирование настроено успешно")
    
    return logger  # Возвращаем настроенный логгер
