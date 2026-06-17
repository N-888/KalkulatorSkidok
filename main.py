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

class DiscountCalculator:
    """Класс для расчёта скидок"""
    
    def __init__(self):
        """Конструктор класса — создаёт пустой список для истории"""
        self.history = []  # Список для хранения истории вычислений
        logging.info("Калькулятор скидок создан")  # Логируем создание
    
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
    
    def get_history(self):
        """Метод получения всей истории"""
        return self.history  # Возвращаем список записей


def main():
    """Основная функция программы"""
    # Создаём экземпляр калькулятора
    calculator = DiscountCalculator()
    
    print("=" * 40)  # Печатаем разделитель
    print("   КАЛЬКУЛЯТОР СКИДОК ДЛЯ МАГАЗИНА")
    print("=" * 40)  # Печатаем разделитель
    
    while True:  # Бесконечный цикл для повторного использования
        try:
            # Запрашиваем цену товара у пользователя
            price_input = input("\nВведите цену товара (или 'выход' для завершения): ")
            
            # Проверяем, хочет ли пользователь выйти
            if price_input.lower() == 'выход':
                # Сохраняем историю перед выходом
                calculator.save_history()
                print("Спасибо за использование! История сохранена.")
                break  # Выходим из цикла
            
            # Преобразуем введённую цену в число
            price = float(price_input)
            
            # Запрашиваем процент скидки
            discount_input = input("Введите процент скидки: ")
            # Преобразуем введённый процент в число
            discount_percent = float(discount_input)
            
            # Вычисляем итоговую цену
            final_price = calculator.calculate_discount(price, discount_percent)
            
            # Выводим результат пользователю
            print(f"\n--- РЕЗУЛЬТАТ ---")
            print(f"Исходная цена: {price} руб.")
            print(f"Скидка: {discount_percent}%")
            print(f"Итоговая цена: {final_price} руб.")
            print(f"Вы экономите: {price - final_price} руб.")
            print("-----------------")
            
        except EOFError:
            # Обрабатываем случай, когда нет ввода (программа запущена без консоли)
            print("\nНет ввода. Завершение программы.")
            logging.info("Программа завершена из-за отсутствия ввода")
            calculator.save_history()  # Сохраняем историю перед выходом
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
            break  # Выходим из цикла
        except Exception as e:
            # Обрабатываем все остальные ошибки
            print(f"Произошла ошибка: {e}")
            logging.error(f"Неожиданная ошибка: {e}")


# Проверяем, что файл запущен напрямую, а не импортирован
if __name__ == "__main__":
    main()  # Запускаем основную функцию
