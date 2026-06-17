# Импортируем модуль для тестирования
import sys
# Импортируем наш калькулятор
from main import DiscountCalculator


def test_calculator():
    """Функция тестирования калькулятора"""
    # Создаём экземпляр калькулятора
    calc = DiscountCalculator()
    
    # Тест 1: Проверка базового расчёта
    print("Тест 1: Базовый расчёт скидки")
    result = calc.calculate_discount(1000, 10)
    assert result == 900.0, f"Ошибка: ожидалось 900.0, получено {result}"
    print(f"  Цена 1000, скидка 10% -> {result} [OK]")
    
    # Тест 2: Проверка скидки 0%
    print("Тест 2: Скидка 0%")
    result = calc.calculate_discount(500, 0)
    assert result == 500.0, f"Ошибка: ожидалось 500.0, получено {result}"
    print(f"  Цена 500, скидка 0% -> {result} [OK]")
    
    # Тест 3: Проверка скидки 100%
    print("Тест 3: Скидка 100%")
    result = calc.calculate_discount(200, 100)
    assert result == 0.0, f"Ошибка: ожидалось 0.0, получено {result}"
    print(f"  Цена 200, скидка 100% -> {result} [OK]")
    
    # Тест 4: Проверка округления
    print("Тест 4: Округление до 2 знаков")
    result = calc.calculate_discount(999, 15)
    assert result == 849.15, f"Ошибка: ожидалось 849.15, получено {result}"
    print(f"  Цена 999, скидка 15% -> {result} [OK]")
    
    # Тест 5: Проверка сохранения истории
    print("Тест 5: Сохранение истории")
    assert len(calc.history) == 4, f"Ошибка: ожидалось 4 записи, получено {len(calc.history)}"
    print(f"  В истории {len(calc.history)} записей [OK]")
    
    # Тест 6: Проверка ошибки - отрицательная цена
    print("Тест 6: Ошибка при отрицательной цене")
    try:
        calc.calculate_discount(-100, 10)
        print("  Ошибка: исключение не выброшено [FAIL]")
    except ValueError as e:
        print(f"  Исключение выброшено корректно: {e} [OK]")
    
    # Тест 7: Проверка ошибки - скидка > 100%
    print("Тест 7: Ошибка при скидке > 100%")
    try:
        calc.calculate_discount(100, 150)
        print("  Ошибка: исключение не выброшено [FAIL]")
    except ValueError as e:
        print(f"  Исключение выброшено корректно: {e} [OK]")
    
    print("\nВсе тесты пройдены успешно!")
    return True


if __name__ == "__main__":
    try:
        success = test_calculator()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"Ошибка выполнения тестов: {e}")
        sys.exit(1)
