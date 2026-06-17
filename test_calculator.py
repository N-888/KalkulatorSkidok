# Импортируем модуль для тестирования
import sys
# Импортируем наш калькулятор и класс товара
from main import DiscountCalculator, DiscountItem


def test_calculator():
    """Функция тестирования калькулятора"""
    # Создаём экземпляр калькулятора
    calc = DiscountCalculator()
    
    # Тест 1: Проверка базового расчёта скидки
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
    
    # Тест 5: Проверка ошибки - отрицательная цена
    print("Тест 5: Ошибка при отрицательной цене")
    try:
        calc.calculate_discount(-100, 10)
        print("  Ошибка: исключение не выброшено [FAIL]")
    except ValueError as e:
        print(f"  Исключение выброшено: {e} [OK]")
    
    # Тест 6: Проверка ошибки - скидка > 100%
    print("Тест 6: Ошибка при скидке > 100%")
    try:
        calc.calculate_discount(100, 150)
        print("  Ошибка: исключение не выброшено [FAIL]")
    except ValueError as e:
        print(f"  Исключение выброшено: {e} [OK]")
    
    print("\n--- БИЗНЕС-ПРАВИЛА ---")
    
    # Тест 7: Проверка бизнес-правила - title не может быть пустым
    print("Тест 7: Title не может быть пустым")
    try:
        item = DiscountItem("", 1000, 10)
        print("  Ошибка: исключение не выброшено [FAIL]")
    except ValueError as e:
        print(f"  Исключение выброшено: {e} [OK]")
    
    # Тест 8: Проверка бизнес-правила - title не может быть пробелами
    print("Тест 8: Title не может быть только пробелами")
    try:
        item = DiscountItem("   ", 1000, 10)
        print("  Ошибка: исключение не выброшено [FAIL]")
    except ValueError as e:
        print(f"  Исключение выброшено: {e} [OK]")
    
    # Тест 9: Проверка бизнес-правила - attachments должен быть списком
    print("Тест 9: Attachments должен быть списком")
    try:
        item = DiscountItem("Товар", 1000, 10, "не список")
        print("  Ошибка: исключение не выброшено [FAIL]")
    except ValueError as e:
        print(f"  Исключение выброшено: {e} [OK]")
    
    # Тест 10: Проверка бизнес-правила - attachments список строк
    print("Тест 10: Attachments - список строк")
    try:
        item = DiscountItem("Товар", 1000, 10, [123, "строка"])
        print("  Ошибка: исключение не выброшено [FAIL]")
    except ValueError as e:
        print(f"  Исключение выброшено: {e} [OK]")
    
    # Тест 11: Успешное создание товара
    print("Тест 11: Успешное создание товара")
    item = DiscountItem("Куртка зимняя", 8500, 20, ["чек", "гарантия"])
    assert item.title == "Куртка зимняя"
    assert item.price == 8500
    assert item.discount_percent == 20
    assert item.attachments == ["чек", "гарантия"]
    print(f"  Товар создан: {item.title} [OK]")
    
    # Тест 12: Добавление товара в калькулятор
    print("Тест 12: Добавление товара в калькулятор")
    calc.add_item("Смартфон", 45000, 15)
    assert len(calc.items) == 1
    print(f"  Товар добавлен, всего: {len(calc.items)} [OK]")
    
    # Тест 13: Получение товара по индексу
    print("Тест 13: Получение товара по индексу")
    item = calc.get_item(0)
    assert item.title == "Смартфон"
    print(f"  Получен товар: {item.title} [OK]")
    
    # Тест 14: Редактирование товара
    print("Тест 14: Редактирование товара")
    calc.edit_item(0, title="Смартфон Pro", price=50000)
    item = calc.get_item(0)
    assert item.title == "Смартфон Pro"
    assert item.price == 50000
    print(f"  Товар отредактирован: {item.title} [OK]")
    
    # Тест 15: Удаление товара
    print("Тест 15: Удаление товара")
    calc.add_item("Наушники", 5000, 10)
    assert len(calc.items) == 2
    calc.remove_item(0)
    assert len(calc.items) == 1
    print(f"  Товар удалён, осталось: {len(calc.items)} [OK]")
    
    # Тест 16: Ошибка при удалении из пустого списка
    print("Тест 16: Ошибка удаления из пустого списка")
    calc.clear_items()
    try:
        calc.remove_item(0)
        print("  Ошибка: исключение не выброшено [FAIL]")
    except ValueError as e:
        print(f"  Исключение выброшено: {e} [OK]")
    
    # Тест 17: Ошибка при редактировании пустого списка
    print("Тест 17: Ошибка редактирования пустого списка")
    try:
        calc.edit_item(0, title="Новый")
        print("  Ошибка: исключение не выброшено [FAIL]")
    except ValueError as e:
        print(f"  Исключение выброшено: {e} [OK]")
    
    # Тест 18: Получение товара из пустого списка
    print("Тест 18: Ошибка получения из пустого списка")
    try:
        calc.get_item(0)
        print("  Ошибка: исключение не выброшено [FAIL]")
    except ValueError as e:
        print(f"  Исключение выброшено: {e} [OK]")
    
    # Тест 19: Проверка сохранения истории
    print("Тест 19: Сохранение истории")
    assert len(calc.history) >= 4, f"Ошибка: ожидалось >= 4 записей"
    print(f"  В истории {len(calc.history)} записей [OK]")
    
    # Тест 20: Проверка списка товаров
    print("Тест 20: Список товаров")
    calc.add_item("Товар 1", 1000, 10)
    calc.add_item("Товар 2", 2000, 20)
    items = calc.get_items()
    assert len(items) == 2
    print(f"  В списке {len(items)} товаров [OK]")
    
    print("\nВсе тесты пройдены успешно!")
    return True


if __name__ == "__main__":
    try:
        success = test_calculator()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"Ошибка выполнения тестов: {e}")
        sys.exit(1)
