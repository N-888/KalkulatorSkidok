# Импортируем модуль для работы с датой и временем
from datetime import datetime
# Импортируем модуль для логирования
import logging
# Импортируем Path для удобной работы с путями файлов
from pathlib import Path

# Настраиваем логирование в файл и консоль
logging.basicConfig(
    level=logging.INFO,  # Устанавливаем уровень логирования
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщений
    handlers=[
        logging.FileHandler('logs.txt', encoding='utf-8'),  # Логи в файл
        logging.StreamHandler()  # Логи в консоль
    ]
)


class DiscountItem:
    """Класс для хранения информации о товаре со скидкой"""
    
    def __init__(self, title, price, discount_percent, attachments=None):
        """
        Конструктор товара
        title — название товара (не может быть пустым)
        price — цена товара
        discount_percent — процент скидки
        attachments — список вложений (строки)
        """
        # Проверяем бизнес-правило: title не может быть пустым
        if not title or not title.strip():
            logging.error("Ошибка: название товара не может быть пустым")
            raise ValueError("Название товара (title) не может быть пустым!")
        
        # Устанавливаем название товара
        self.title = title.strip()
        # Устанавливаем цену товара
        self.price = price
        # Устанавливаем процент скидки
        self.discount_percent = discount_percent
        
        # Проверяем бизнес-правило: attachments должен быть списком строк
        if attachments is not None:
            # Если attachments передан, проверяем что это список
            if not isinstance(attachments, list):
                logging.error("Ошибка: вложения должны быть списком")
                raise ValueError("Вложения (attachments) должны быть списком строк!")
            # Проверяем что каждый элемент — строка
            for item in attachments:
                if not isinstance(item, str):
                    logging.error(f"Ошибка: вложение '{item}' не является строкой")
                    raise ValueError("Каждое вложение должно быть строкой!")
            self.attachments = attachments
        else:
            # Если attachments не передан, создаём пустой список
            self.attachments = []
        
        # Логируем создание товара
        logging.info(f"Создан товар: {self.title}, цена: {self.price}, скидка: {self.discount_percent}%")
    
    def to_dict(self):
        """Метод преобразования товара в словарь"""
        return {
            "title": self.title,
            "price": self.price,
            "discount_percent": self.discount_percent,
            "attachments": self.attachments
        }


class DiscountCalculator:
    """Класс для расчёта скидок с бизнес-правилами"""
    
    def __init__(self):
        """Конструктор класса — создаёт пустой список для истории"""
        self.history = []  # Список для хранения истории вычислений
        self.items = []  # Список для хранения товаров
        logging.info("Калькулятор скидок создан")  # Логируем создание
    
    def add_item(self, title, price, discount_percent, attachments=None):
        """
        Метод добавления товара
        title — название товара (не может быть пустым)
        price — цена товара
        discount_percent — процент скидки
        attachments — список вложений (строки)
        """
        # Создаём объект товара с проверкой бизнес-правил
        item = DiscountItem(title, price, discount_percent, attachments)
        # Добавляем товар в список
        self.items.append(item)
        # Логируем добавление товара
        logging.info(f"Товар добавлен: {item.title}")
        return item
    
    def get_item(self, index):
        """
        Метод получения товара по индексу
        index — индекс товара в списке
        """
        # Проверяем что список не пустой (бизнес-правило)
        if not self.items:
            logging.error("Ошибка: список товаров пуст")
            raise ValueError("Нельзя получить товар: список товаров пуст!")
        # Проверяем корректность индекса
        if index < 0 or index >= len(self.items):
            logging.error(f"Ошибка: индекс {index} вне диапазона")
            raise ValueError(f"Индекс {index} вне диапазона (0-{len(self.items)-1})")
        # Возвращаем товар
        return self.items[index]
    
    def remove_item(self, index):
        """
        Метод удаления товара по индексу
        index — индекс товара для удаления
        """
        # Проверяем что список не пустой (бизнес-правило)
        if not self.items:
            logging.error("Ошибка: нельзя удалять из пустого списка")
            raise ValueError("Нельзя удалять товары: список товаров пуст!")
        # Проверяем корректность индекса
        if index < 0 or index >= len(self.items):
            logging.error(f"Ошибка: индекс {index} вне диапазона")
            raise ValueError(f"Индекс {index} вне диапазона (0-{len(self.items)-1})")
        # Сохраняем удаляемый товар для логирования
        removed_item = self.items[index]
        # Удаляем товар из списка
        del self.items[index]
        # Логируем удаление товара
        logging.info(f"Товар удалён: {removed_item.title}")
    
    def edit_item(self, index, title=None, price=None, discount_percent=None, attachments=None):
        """
        Метод редактирования товара
        index — индекс товара для редактирования
        title — новое название (не может быть пустым)
        price — новая цена
        discount_percent — новый процент скидки
        attachments — новый список вложений
        """
        # Проверяем что список не пустой (бизнес-правило)
        if not self.items:
            logging.error("Ошибка: нельзя редактировать в пустом списке")
            raise ValueError("Нельзя редактировать: список товаров пуст!")
        # Проверяем корректность индекса
        if index < 0 or index >= len(self.items):
            logging.error(f"Ошибка: индекс {index} вне диапазона")
            raise ValueError(f"Индекс {index} вне диапазона (0-{len(self.items)-1})")
        
        # Получаем товар для редактирования
        item = self.items[index]
        
        # Обновляем название если передано (с проверкой бизнес-правила)
        if title is not None:
            if not title or not title.strip():
                logging.error("Ошибка: название товара не может быть пустым")
                raise ValueError("Название товара (title) не может быть пустым!")
            item.title = title.strip()
        
        # Обновляем цену если передана
        if price is not None:
            item.price = price
        
        # Обновляем процент скидки если передан
        if discount_percent is not None:
            item.discount_percent = discount_percent
        
        # Обновляем вложения если переданы (с проверкой бизнес-правила)
        if attachments is not None:
            if not isinstance(attachments, list):
                logging.error("Ошибка: вложения должны быть списком")
                raise ValueError("Вложения (attachments) должны быть списком строк!")
            for att in attachments:
                if not isinstance(att, str):
                    logging.error(f"Ошибка: вложение '{att}' не является строкой")
                    raise ValueError("Каждое вложение должно быть строкой!")
            item.attachments = attachments
        
        # Логируем редактирование товара
        logging.info(f"Товар отредактирован: {item.title}")
    
    def calculate_discount(self, price, discount_percent):
        """
        Метод расчёта скидки
        price — цена товара
        discount_percent — процент скидки
        Возвращает итоговую цену
        """
        # Проверяем, что цена положительная
        if price <= 0:
            logging.error(f"Ошибка: цена {price} должна быть больше 0")
            raise ValueError("Цена должна быть больше 0")
        
        # Проверяем, что скидка от 0 до 100 процентов
        if discount_percent < 0 or discount_percent > 100:
            logging.error(f"Ошибка: скидка {discount_percent}% недопустима")
            raise ValueError("Скидка должна быть от 0 до 100 процентов")
        
        # Вычисляем сумму скидки
        discount_amount = price * (discount_percent / 100)
        # Вычисляем итоговую цену
        final_price = price - discount_amount
        # Округляем до 2 знаков после запятой
        final_price = round(final_price, 2)
        
        # Формируем запись для истории
        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Текущая дата
            "price": price,  # Исходная цена
            "discount_percent": discount_percent,  # Процент скидки
            "final_price": final_price  # Итоговая цена
        }
        
        # Добавляем запись в историю
        self.history.append(record)
        # Логируем успешный расчёт
        logging.info(f"Расчёт выполнен: {price} - {discount_percent}% = {final_price}")
        
        return final_price  # Возвращаем результат
    
    def save_history(self, filename="history.txt"):
        """
        Метод сохранения истории в файл
        filename — имя файла для сохранения
        """
        # Открываем файл для записи (создаём новый или перезаписываем)
        with open(filename, 'w', encoding='utf-8') as file:
            # Проходим по каждой записи в истории
            for record in self.history:
                # Формируем строку для записи
                line = (f"Дата: {record['date']}, "
                       f"Цена: {record['price']}, "
                       f"Скидка: {record['discount_percent']}%, "
                       f"Итог: {record['final_price']}\n")
                # Записываем строку в файл
                file.write(line)
        
        # Логируем успешное сохранение
        logging.info(f"История сохранена в файл {filename}")
    
    def save_items(self, filename="items.txt"):
        """
        Метод сохранения списка товаров в файл
        filename — имя файла для сохранения
        """
        # Открываем файл для записи
        with open(filename, 'w', encoding='utf-8') as file:
            # Проходим по каждому товару
            for i, item in enumerate(self.items):
                # Рассчитываем итоговую цену для товара
                final_price = self.calculate_discount(item.price, item.discount_percent)
                # Формируем строку для записи
                line = (f"{i+1}. {item.title} | "
                       f"Цена: {item.price} руб. | "
                       f"Скидка: {item.discount_percent}% | "
                       f"Итого: {final_price} руб.")
                # Добавляем вложения если есть
                if item.attachments:
                    line += f" | Вложения: {', '.join(item.attachments)}"
                # Добавляем перенос строки
                line += "\n"
                # Записываем строку в файл
                file.write(line)
        
        # Логируем успешное сохранение
        logging.info(f"Список товаров сохранён в файл {filename}")
    
    def get_history(self):
        """Метод получения всей истории"""
        return self.history  # Возвращаем список записей
    
    def get_items(self):
        """Метод получения списка всех товаров"""
        return self.items  # Возвращаем список товаров
    
    def clear_items(self):
        """Метод очистки списка товаров"""
        # Проверяем бизнес-правило: нельзя редактировать/удалять при пустом списке
        if not self.items:
            logging.warning("Попытка очистить уже пустой список")
            print("Список товаров уже пуст!")
            return False
        
        # Сохраняем количество удаляемых товаров
        count = len(self.items)
        # Очищаем список товаров
        self.items.clear()
        # Логируем очистку списка
        logging.info(f"Список товаров очищен. Удалено {count} товаров")
        return True


def main():
    """Основная функция программы"""
    # Создаём экземпляр калькулятора
    calculator = DiscountCalculator()
    
    print("=" * 50)  # Печатаем разделитель
    print("   КАЛЬКУЛЯТОР СКИДОК ДЛЯ МАГАЗИНА")
    print("=" * 50)  # Печатаем разделитель
    print("Доступные команды:")
    print("  'выход' — завершить работу")
    print("  'список' — показать все товары")
    print("  'удалить' — удалить товар из списка")
    print("  'очистить' — очистить весь список")
    print("=" * 50)  # Печатаем разделитель
    
    while True:  # Бесконечный цикл для повторного использования
        try:
            # Запрашиваем действие у пользователя
            command = input("\nВведите название товара (или команду): ")
            
            # Проверяем команду выхода
            if command.lower() == 'выход':
                # Сохраняем историю перед выходом
                calculator.save_history()
                # Сохраняем список товаров перед выходом
                if calculator.items:
                    calculator.save_items()
                print("Спасибо за использование! Данные сохранены.")
                break  # Выходим из цикла
            
            # Проверяем команду просмотра списка
            if command.lower() == 'список':
                # Проверяем есть ли товары в списке
                if not calculator.items:
                    print("Список товаров пуст!")
                    logging.info("Пользователь запросил пустой список товаров")
                else:
                    print("\n--- СПИСОК ТОВАРОВ ---")
                    # Выводим каждый товар
                    for i, item in enumerate(calculator.items):
                        # Рассчитываем итоговую цену
                        final_price = calculator.calculate_discount(item.price, item.discount_percent)
                        # Выводим информацию о товаре
                        print(f"{i+1}. {item.title}")
                        print(f"   Цена: {item.price} руб. -> Итого: {final_price} руб. (скидка {item.discount_percent}%)")
                        # Выводим вложения если есть
                        if item.attachments:
                            print(f"   Вложения: {', '.join(item.attachments)}")
                    print("-" * 30)
                    logging.info(f"Пользователь просмотрел список из {len(calculator.items)} товаров")
                continue  # Возвращаемся к началу цикла
            
            # Проверяем команду удаления товара
            if command.lower() == 'удалить':
                # Проверяем бизнес-правило: нельзя удалять при пустом списке
                if not calculator.items:
                    print("Ошибка: список товаров пуст! Нечего удалять.")
                    logging.error("Попытка удаления из пустого списка")
                    continue  # Возвращаемся к началу цикла
                # Просим пользователя указать номер товара для удаления
                try:
                    index_input = input("Введите номер товара для удаления: ")
                    index = int(index_input) - 1  # Преобразуем в индекс (с 0)
                    # Удаляем товар
                    calculator.remove_item(index)
                    print("Товар успешно удалён!")
                except ValueError as e:
                    print(f"Ошибка: {e}")
                    logging.error(f"Ошибка удаления товара: {e}")
                continue  # Возвращаемся к началу цикла
            
            # Проверяем команду очистки списка
            if command.lower() == 'очистить':
                # Проверяем бизнес-правило: нельзя удалять при пустом списке
                if not calculator.items:
                    print("Список товаров уже пуст!")
                    logging.info("Пользователь пытался очистить уже пустой список")
                    continue  # Возвращаемся к началу цикла
                # Запрашиваем подтверждение
                confirm = input(f"Вы уверены? Вы удалите {len(calculator.items)} товаров (да/нет): ")
                if confirm.lower() == 'да':
                    # Очищаем список
                    calculator.clear_items()
                    print("Список товаров очищен!")
                else:
                    print("Отмена операции.")
                continue  # Возвращаемся к началу цикла
            
            # Если команда не распознана, считаем её названием товара
            title = command  # Сохраняем название товара
            
            # Запрашиваем цену товара
            price_input = input("Введите цену товара: ")
            # Преобразуем введённую цену в число
            price = float(price_input)
            
            # Запрашиваем процент скидки
            discount_input = input("Введите процент скидки: ")
            # Преобразуем введённый процент в число
            discount_percent = float(discount_input)
            
            # Запрашиваем вложения (необязательно)
            attachments_input = input("Введите вложения через запятую (или нажмите Enter для пропуска): ")
            # Преобразуем введённые вложения в список строк
            attachments = [a.strip() for a in attachments_input.split(",")] if attachments_input.strip() else []
            
            # Добавляем товар в список (с проверкой бизнес-правил)
            calculator.add_item(title, price, discount_percent, attachments)
            
            # Вычисляем итоговую цену
            final_price = calculator.calculate_discount(price, discount_percent)
            
            # Выводим результат пользователю
            print(f"\n--- РЕЗУЛЬТАТ ---")
            print(f"Товар: {title}")
            print(f"Исходная цена: {price} руб.")
            print(f"Скидка: {discount_percent}%")
            print(f"Итоговая цена: {final_price} руб.")
            print(f"Вы экономите: {price - final_price} руб.")
            if attachments:
                print(f"Вложения: {', '.join(attachments)}")
            print("-----------------")
            
        except EOFError:
            # Обрабатываем случай, когда нет ввода (программа запущена без консоли)
            print("\nНет ввода. Завершение программы.")
            logging.info("Программа завершена из-за отсутствия ввода")
            calculator.save_history()  # Сохраняем историю перед выходом
            if calculator.items:
                calculator.save_items()  # Сохраняем список товаров
            break  # Выходим из цикла
        except ValueError as e:
            # Обрабатываем ошибки ввода
            print(f"Ошибка ввода: {e}")
            logging.error(f"Ошибка ввода: {e}")
        except KeyboardInterrupt:
            # Обрабатываем нажатие Ctrl+C
            print("\nПрограмма прервана пользователем.")
            logging.info("Программа прервана пользователем (Ctrl+C)")
            calculator.save_history()  # Сохраняем историю перед выходом
            if calculator.items:
                calculator.save_items()  # Сохраняем список товаров
            break  # Выходим из цикла
        except Exception as e:
            # Обрабатываем все остальные ошибки
            print(f"Произошла ошибка: {e}")
            logging.error(f"Неожиданная ошибка: {e}")


# Проверяем, что файл запущен напрямую, а не импортирован
if __name__ == "__main__":
    main()  # Запускаем основную функцию
