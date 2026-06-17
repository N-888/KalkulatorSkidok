# Импортируем наш калькулятор и класс товара
from main import DiscountCalculator, DiscountItem


def demo():
    """Демонстрационный запуск калькулятора"""
    # Создаём экземпляр калькулятора
    calc = DiscountCalculator()
    
    print("=" * 60)
    print("  ДЕМОНСТРАЦИЯ РАБОТЫ КАЛЬКУЛЯТОРА СКИДОК")
    print("  С бизнес-правилами")
    print("=" * 60)
    
    # Демонстрация бизнес-правил
    print("\n[Демонстрация 1] Бизнес-правила")
    print("-" * 40)
    
    # Попытка создать товар с пустым названием
    print("1. Попытка создать товар с пустым названием:")
    try:
        item = DiscountItem("", 1000, 10)
        print("   Ошибка: исключение не выброшено!")
    except ValueError as e:
        print(f"   Результат: {e}")
    
    # Попытка создать товар с некорректными вложениями
    print("\n2. Попытка создать товар с некорректными вложениями:")
    try:
        item = DiscountItem("Товар", 1000, 10, "не список")
        print("   Ошибка: исключение не выброшено!")
    except ValueError as e:
        print(f"   Результат: {e}")
    
    # Успешное создание товара
    print("\n3. Успешное создание товара с вложениями:")
    item1 = DiscountItem("Зимняя куртка", 8500, 20, ["чек", "гарантия на 1 год"])
    calc.add_item("Зимняя куртка", 8500, 20, ["чек", "гарантия на 1 год"])
    final_price = calc.calculate_discount(8500, 20)
    print(f"   Товар: {item1.title}")
    print(f"   Цена: {item1.price} руб.")
    print(f"   Скидка: {item1.discount_percent}%")
    print(f"   Итого: {final_price} руб.")
    print(f"   Вложения: {', '.join(item1.attachments)}")
    
    # Демонстрация добавления товаров
    print("\n[Демонстрация 2] Добавление товаров")
    print("-" * 40)
    
    # Добавляем ещё товары
    calc.add_item("Смартфон", 45000, 15, ["чек", "коробка"])
    calc.add_item("Наушники", 5000, 10)
    calc.add_item("Бытовая техника", 15000, 25, ["чек", "гарантия", "инструкция"])
    
    # Выводим список товаров
    print("Список товаров:")
    for i, item in enumerate(calc.get_items()):
        final_price = calc.calculate_discount(item.price, item.discount_percent)
        print(f"  {i+1}. {item.title}")
        print(f"     Цена: {item.price} руб. -> Итого: {final_price} руб. (скидка {item.discount_percent}%)")
        if item.attachments:
            print(f"     Вложения: {', '.join(item.attachments)}")
    
    # Демонстрация редактирования
    print("\n[Демонстрация 3] Редактирование товара")
    print("-" * 40)
    print("Редактируем товар 'Смартфон':")
    calc.edit_item(1, title="Смартфон Pro Max", price=55000, attachments=["чек", "коробка", "наушники в комплекте"])
    item = calc.get_item(1)
    print(f"  Новое название: {item.title}")
    print(f"  Новая цена: {item.price} руб.")
    print(f"  Новые вложения: {', '.join(item.attachments)}")
    
    # Демонстрация удаления
    print("\n[Демонстрация 4] Удаление товара")
    print("-" * 40)
    print(f"Товаров до удаления: {len(calc.get_items())}")
    calc.remove_item(2)  # Удаляем наушники
    print(f"Товаров после удаления: {len(calc.get_items())}")
    
    # Демонстрация ошибок
    print("\n[Демонстрация 5] Обработка ошибок")
    print("-" * 40)
    
    # Попытка удаления из пустого списка
    print("1. Попытка удаления из пустого списка:")
    calc_empty = DiscountCalculator()
    try:
        calc_empty.remove_item(0)
        print("   Ошибка: исключение не выброшено!")
    except ValueError as e:
        print(f"   Результат: {e}")
    
    # Попытка редактирования пустого списка
    print("\n2. Попытка редактирования пустого списка:")
    try:
        calc_empty.edit_item(0, title="Новый")
        print("   Ошибка: исключение не выброшено!")
    except ValueError as e:
        print(f"   Результат: {e}")
    
    # Сохраняем результаты
    calc.save_history("demo_history.txt")
    calc.save_items("demo_items.txt")
    
    print("\n" + "=" * 60)
    print("  Демонстрация завершена!")
    print("  Файлы сохранены: demo_history.txt, demo_items.txt")
    print("=" * 60)


# Запускаем демонстрацию
if __name__ == "__main__":
    demo()
