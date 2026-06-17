# Импортируем модуль tkinter для создания графического интерфейса
import tkinter as tk
# Импортируем виджеты для ввода текста и кнопок
from tkinter import ttk, messagebox
# Импортируем наш калькулятор
from main import DiscountCalculator
# Импортируем модуль для логирования
import logging


class DiscountApp:
    """Класс графического приложения калькулятора скидок"""
    
    def __init__(self):
        """Конструктор класса — создаёт главное окно"""
        # Создаём экземпляр калькулятора
        self.calculator = DiscountCalculator()
        
        # Создаём главное окно приложения
        self.root = tk.Tk()
        # Устанавливаем заголовок окна
        self.root.title("Калькулятор скидок для магазина")
        # Устанавливаем размер окна
        self.root.geometry("500x600")
        # Устанавливаем минимальный размер окна
        self.root.minsize(400, 500)
        # Устанавливаем цвет фона
        self.root.configure(bg="#f0f0f0")
        
        # Создаём стили для виджетов
        self.setup_styles()
        # Создаём элементы интерфейса
        self.create_widgets()
        
        # Логируем запуск приложения
        logging.info("GUI приложение запущено")
    
    def setup_styles(self):
        """Метод настройки стилей интерфейса"""
        # Создаём стиль для кнопок
        self.style = ttk.Style()
        # Настраиваем стиль кнопки
        self.style.configure("TButton", font=("Arial", 12), padding=10)
        # Настраиваем стиль заголовка
        self.style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")
        # Настраиваем стиль поля ввода
        self.style.configure("TEntry", font=("Arial", 12), padding=5)
    
    def create_widgets(self):
        """Метод создания элементов интерфейса"""
        # Создаём главный фрейм (контейнер) для размещения элементов
        main_frame = ttk.Frame(self.root, padding="20")
        # Размещаем фрейм с отступами
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # === ЗАГОЛОВОК ===
        # Создаём заголовок приложения
        title_label = ttk.Label(
            main_frame,
            text="Калькулятор скидок",
            font=("Arial", 20, "bold")
        )
        # Размещаем заголовок
        title_label.pack(pady=(0, 20))
        
        # === НАЗВАНИЕ ТОВАРА ===
        # Создаём подпись для названия товара
        ttk.Label(main_frame, text="Название товара:").pack(anchor=tk.W)
        # Создаём поле ввода для названия товара
        self.title_entry = ttk.Entry(main_frame, font=("Arial", 12))
        # Размещаем поле ввода
        self.title_entry.pack(fill=tk.X, pady=(0, 10))
        
        # === ЦЕНА ТОВАРА ===
        # Создаём подпись для цены товара
        ttk.Label(main_frame, text="Цена товара (руб.):").pack(anchor=tk.W)
        # Создаём поле ввода для цены товара
        self.price_entry = ttk.Entry(main_frame, font=("Arial", 12))
        # Размещаем поле ввода
        self.price_entry.pack(fill=tk.X, pady=(0, 10))
        
        # === ПРОЦЕНТ СКИДКИ ===
        # Создаём подпись для процента скидки
        ttk.Label(main_frame, text="Процент скидки (%):").pack(anchor=tk.W)
        # Создаём поле ввода для процента скидки
        self.discount_entry = ttk.Entry(main_frame, font=("Arial", 12))
        # Размещаем поле ввода
        self.discount_entry.pack(fill=tk.X, pady=(0, 10))
        
        # === ВЛОЖЕНИЯ ===
        # Создаём подпись для вложений
        ttk.Label(main_frame, text="Вложения (через запятую):").pack(anchor=tk.W)
        # Создаём поле ввода для вложений
        self.attachments_entry = ttk.Entry(main_frame, font=("Arial", 12))
        # Размещаем поле ввода
        self.attachments_entry.pack(fill=tk.X, pady=(0, 10))
        
        # === КНОПКИ ===
        # Создаём фрейм для кнопок
        buttons_frame = ttk.Frame(main_frame)
        # Размещаем фрейм для кнопок
        buttons_frame.pack(fill=tk.X, pady=(10, 10))
        
        # Создаём кнопку "Рассчитать"
        self.calculate_btn = ttk.Button(
            buttons_frame,
            text="Рассчитать скидку",
            command=self.calculate_discount
        )
        # Размещаем кнопку
        self.calculate_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
        
        # Создаём кнопку "Очистить"
        self.clear_btn = ttk.Button(
            buttons_frame,
            text="Очистить",
            command=self.clear_fields
        )
        # Размещаем кнопку
        self.clear_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 0))
        
        # === РЕЗУЛЬТАТ ===
        # Создаём фрейм для отображения результата
        self.result_frame = ttk.LabelFrame(
            main_frame,
            text="Результат",
            padding="15"
        )
        # Размещаем фрейм результата
        self.result_frame.pack(fill=tk.X, pady=(10, 10))
        
        # Создаём метку для отображения результата
        self.result_label = ttk.Label(
            self.result_frame,
            text="Введите данные и нажмите 'Рассчитать'",
            font=("Arial", 12),
            wraplength=400
        )
        # Размещаем метку результата
        self.result_label.pack()
        
        # === ИСТОРИЯ ===
        # Создаём фрейм для истории
        history_frame = ttk.LabelFrame(
            main_frame,
            text="История вычислений",
            padding="10"
        )
        # Размещаем фрейм истории
        history_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Создаём текстовое поле для истории с прокруткой
        self.history_text = tk.Text(
            history_frame,
            height=6,
            font=("Arial", 10),
            state=tk.DISABLED
        )
        # Размещаем текстовое поле
        self.history_text.pack(fill=tk.BOTH, expand=True)
        
        # Создаём скроллбар для истории
        scrollbar = ttk.Scrollbar(self.history_text, orient=tk.VERTICAL)
        # Размещаем скроллбар
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # Привязываем скроллбар к текстовому полю
        self.history_text.config(yscrollcommand=scrollbar.set)
        # Привязываем скроллбар к текстовому полю
        scrollbar.config(command=self.history_text.yview)
    
    def calculate_discount(self):
        """Метод расчёта скидки при нажатии кнопки"""
        try:
            # Получаем название товара из поля ввода
            title = self.title_entry.get().strip()
            
            # Проверяем бизнес-правило: title не может быть пустым
            if not title:
                messagebox.showerror(
                    "Ошибка",
                    "Название товара не может быть пустым!"
                )
                logging.error("Пользователь не ввёл название товара")
                return
            
            # Получаем цену товара из поля ввода
            price_text = self.price_entry.get().strip()
            
            # Проверяем что цена введена
            if not price_text:
                messagebox.showerror(
                    "Ошибка",
                    "Введите цену товара!"
                )
                logging.error("Пользователь не ввёл цену товара")
                return
            
            # Преобразуем цену в число
            price = float(price_text)
            
            # Проверяем что цена положительная
            if price <= 0:
                messagebox.showerror(
                    "Ошибка",
                    "Цена товара должна быть больше 0!"
                )
                logging.error(f"Пользователь ввёл некорректную цену: {price}")
                return
            
            # Получаем процент скидки из поля ввода
            discount_text = self.discount_entry.get().strip()
            
            # Проверяем что скидка введена
            if not discount_text:
                messagebox.showerror(
                    "Ошибка",
                    "Введите процент скидки!"
                )
                logging.error("Пользователь не ввёл процент скидки")
                return
            
            # Преобразуем процент скидки в число
            discount_percent = float(discount_text)
            
            # Проверяем что скидка от 0 до 100
            if discount_percent < 0 or discount_percent > 100:
                messagebox.showerror(
                    "Ошибка",
                    "Процент скидки должен быть от 0 до 100!"
                )
                logging.error(f"Пользователь ввёл некорректную скидку: {discount_percent}")
                return
            
            # Получаем вложения из поля ввода
            attachments_text = self.attachments_entry.get().strip()
            # Преобразуем вложения в список строк
            attachments = [a.strip() for a in attachments_text.split(",")] if attachments_text else []
            
            # Добавляем товар в калькулятор
            self.calculator.add_item(title, price, discount_percent, attachments)
            
            # Рассчитываем итоговую цену
            final_price = self.calculator.calculate_discount(price, discount_percent)
            
            # Вычисляем сумму экономии
            savings = price - final_price
            
            # Формируем текст результата
            result_text = (
                f"Товар: {title}\n"
                f"Исходная цена: {price:.2f} руб.\n"
                f"Скидка: {discount_percent:.1f}%\n"
                f"Итоговая цена: {final_price:.2f} руб.\n"
                f"Экономия: {savings:.2f} руб."
            )
            
            # Добавляем вложения если есть
            if attachments:
                result_text += f"\nВложения: {', '.join(attachments)}"
            
            # Обновляем метку результата
            self.result_label.config(text=result_text)
            
            # Добавляем запись в историю
            self.add_to_history(
                f"{title}: {price} -> {final_price} руб. "
                f"(скидка {discount_percent}%, экономия {savings:.2f} руб.)"
            )
            
            # Логируем успешный расчёт
            logging.info(f"Расчёт в GUI: {title} - {price} -> {final_price}")
            
            # Показываем сообщение об успехе
            messagebox.showinfo(
                "Успех",
                f"Расчёт выполнен!\nИтого: {final_price:.2f} руб.\nЭкономия: {savings:.2f} руб."
            )
            
        except ValueError:
            # Обрабатываем ошибку ввода числа
            messagebox.showerror(
                "Ошибка",
                "Проверьте правильность ввода числовых значений!"
            )
            logging.error("Ошибка ввода числовых значений в GUI")
        except Exception as e:
            # Обрабатываем все остальные ошибки
            messagebox.showerror(
                "Ошибка",
                f"Произошла ошибка: {str(e)}"
            )
            logging.error(f"Неожиданная ошибка в GUI: {e}")
    
    def clear_fields(self):
        """Метод очистки полей ввода"""
        # Очищаем поле названия товара
        self.title_entry.delete(0, tk.END)
        # Очищаем поле цены товара
        self.price_entry.delete(0, tk.END)
        # Очищаем поле процента скидки
        self.discount_entry.delete(0, tk.END)
        # Очищаем поле вложений
        self.attachments_entry.delete(0, tk.END)
        # Сбрасываем метку результата
        self.result_label.config(text="Введите данные и нажмите 'Рассчитать'")
        # Логируем очистку полей
        logging.info("Поля ввода очищены")
    
    def add_to_history(self, text):
        """Метод добавления записи в историю"""
        # Включаем редактирование текстового поля
        self.history_text.config(state=tk.NORMAL)
        # Вставляем новую запись в начало
        self.history_text.insert("1.0", text + "\n\n")
        # Отключаем редактирование текстового поля
        self.history_text.config(state=tk.DISABLED)
    
    def run(self):
        """Метод запуска приложения"""
        # Запускаем главный цикл обработки событий
        self.root.mainloop()
        # Логируем закрытие приложения
        logging.info("GUI приложение закрыто")


# Точка входа в программу
if __name__ == "__main__":
    # Создаём экземпляр приложения
    app = DiscountApp()
    # Запускаем приложение
    app.run()
