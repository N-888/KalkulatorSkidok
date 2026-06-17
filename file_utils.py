# Импортируем модуль для работы с файлами и папками
import os
# Импортируем модуль для логирования
import logging


class FileManager:
    """Класс для работы с файловой системой"""
    
    def __init__(self, base_dir="."):
        """
        Конструктор класса
        base_dir — базовая директория для работы с файлами
        """
        self.base_dir = base_dir  # Сохраняем базовую директорию
        # Логируем создание менеджера файлов
        logging.info(f"FileManager создан в директории: {base_dir}")
    
    def create_file(self, filename, content=""):
        """
        Метод создания файла
        filename — имя файла
        content — содержимое файла (по умолчанию пустое)
        """
        try:
            # Формируем полный путь к файлу
            filepath = os.path.join(self.base_dir, filename)
            # Открываем файл для записи
            with open(filepath, 'w', encoding='utf-8') as file:
                # Записываем содержимое
                file.write(content)
            # Логируем успешное создание файла
            logging.info(f"Файл создан: {filepath}")
            return True  # Возвращаем успех
        except Exception as e:
            # Логируем ошибку
            logging.error(f"Ошибка создания файла {filename}: {e}")
            return False  # Возвращаем неудачу
    
    def read_file(self, filename):
        """
        Метод чтения файла
        filename — имя файла для чтения
        Возвращает содержимое файла или None при ошибке
        """
        try:
            # Формируем полный путь к файлу
            filepath = os.path.join(self.base_dir, filename)
            # Открываем файл для чтения
            with open(filepath, 'r', encoding='utf-8') as file:
                # Читаем содержимое
                content = file.read()
            # Логируем успешное чтение
            logging.info(f"Файл прочитан: {filepath}")
            return content  # Возвращаем содержимое
        except FileNotFoundError:
            # Логируем ошибку — файл не найден
            logging.error(f"Файл не найден: {filename}")
            return None  # Возвращаем None
        except Exception as e:
            # Логируем другие ошибки
            logging.error(f"Ошибка чтения файла {filename}: {e}")
            return None  # Возвращаем None
    
    def delete_file(self, filename):
        """
        Метод удаления файла
        filename — имя файла для удаления
        """
        try:
            # Формируем полный путь к файлу
            filepath = os.path.join(self.base_dir, filename)
            # Удаляем файл
            os.remove(filepath)
            # Логируем успешное удаление
            logging.info(f"Файл удалён: {filepath}")
            return True  # Возвращаем успех
        except FileNotFoundError:
            # Логируем ошибку — файл не найден
            logging.error(f"Файл не найден для удаления: {filename}")
            return False  # Возвращаем неудачу
        except Exception as e:
            # Логируем другие ошибки
            logging.error(f"Ошибка удаления файла {filename}: {e}")
            return False  # Возвращаем неудачу
    
    def file_exists(self, filename):
        """
        Метод проверки существования файла
        filename — имя файла для проверки
        Возвращает True если файл существует, False если нет
        """
        # Формируем полный путь к файлу
        filepath = os.path.join(self.base_dir, filename)
        # Проверяем существование файла
        exists = os.path.exists(filepath)
        # Логируем результат проверки
        logging.info(f"Проверка файла {filename}: {'существует' if exists else 'не найден'}")
        return exists  # Возвращаем результат
    
    def create_directory(self, dir_name):
        """
        Метод создания папки
        dir_name — имя папки для создания
        """
        try:
            # Формируем полный путь к папке
            dirpath = os.path.join(self.base_dir, dir_name)
            # Создаём папку (если она не существует)
            os.makedirs(dirpath, exist_ok=True)
            # Логируем успешное создание папки
            logging.info(f"Папка создана: {dirpath}")
            return True  # Возвращаем успех
        except Exception as e:
            # Логируем ошибку
            logging.error(f"Ошибка создания папки {dir_name}: {e}")
            return False  # Возвращаем неудачу
    
    def list_files(self):
        """
        Метод получения списка файлов в директории
        Возвращает список имён файлов
        """
        try:
            # Получаем список файлов в директории
            files = os.listdir(self.base_dir)
            # Логируем получение списка
            logging.info(f"Получен список файлов: {len(files)} файлов")
            return files  # Возвращаем список
        except Exception as e:
            # Логируем ошибку
            logging.error(f"Ошибка получения списка файлов: {e}")
            return []  # Возвращаем пустой список
