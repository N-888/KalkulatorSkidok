# Импортируем наш калькулятор
from main import DiscountCalculator


def demo():
    """Демонстрационный запуск калькулятора"""
    # Создаём экземпляр калькулятора
    calc = DiscountCalculator()
    
    print("=" * 50)
    print("  ДЕМОНСТРАЦИЯ РАБОТЫ КАЛЬКУЛЯТОРА СКИДОК")
    print("=" * 50)
    
    # Пример 1: Скидка на одежду
    print("\n[Пример 1] Скидка на зимнюю куртку")
    price1 = 8500  # Цена куртки
    discount1 = 20  # Скидка 20%
    result1 = calc.calculate_discount(price1, discount1)
    print(f"  Цена: {price1} руб.")
    print(f"  Скидка: {discount1}%")
    print(f"  Итого: {result1} руб.")
    print(f"  Экономия: {price1 - result1} руб.")
    
    # Пример 2: Скидка на электронику
    print("\n[Пример 2] Скидка на смартфон")
    price2 = 45000  # Цена смартфона
    discount2 = 15  # Скидка 15%
    result2 = calc.calculate_discount(price2, discount2)
    print(f"  Цена: {price2} руб.")
    print(f"  Скидка: {discount2}%")
    print(f"  Итого: {result2} руб.")
    print(f"  Экономия: {price2 - result2} руб.")
    
    # Пример 3: Скидка на продукты
    print("\n[Пример 3] Скидка на продукты")
    price3 = 2500  # Сумма покупки
    discount3 = 5  # Скидка 5%
    result3 = calc.calculate_discount(price3, discount3)
    print(f"  Сумма покупки: {price3} руб.")
    print(f"  Скидка: {discount3}%")
    print(f"  Итого: {result3} руб.")
    print(f"  Экономия: {price3 - result3} руб.")
    
    # Сохраняем историю
    calc.save_history("demo_history.txt")
    
    print("\n" + "=" * 50)
    print("  История сохранена в файл demo_history.txt")
    print("=" * 50)


# Запускаем демонстрацию
if __name__ == "__main__":
    demo()
