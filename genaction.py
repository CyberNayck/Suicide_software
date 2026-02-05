import random

# Списки для генерации акций
products = [
    "смартфон", "ноутбук", "планшет", "телевизор", 
    "наушники", "умные часы", "фотоаппарат", 
    "гаджет", "консоль", "принтер", "беспроводной маршрутизатор", 
    "игровая клавиатура", "монитор", "вакуумный очиститель", 
    "робот-пылесос", "умный дом", "внешний жесткий диск", 
    "акустическая система", "проектор", "геймпад"
]

discounts = [5, 10, 15, 20, 25, 30, 35, 40, 50]

def generate_offer():
    """Генерирует случайную акцию."""
    product = random.choice(products)
    discount = random.choice(discounts)
    days_valid = random.randint(1, 30)  # Срок действия акции от 1 до 30 дней
    offer = f"Акция: {discount}% скидка на {product} (срок действия: {days_valid} дней)"
    return offer

def offer_generator():
    print("Генератор акций")

    while True:
        num_offers = input("\nСколько акций вы хотите сгенерировать? (Введите 0 для выхода): ")

        if num_offers == '0':
            print("Выход из программы.")
            break

        try:
            num_offers = int(num_offers)
            if num_offers < 0:
                print("Пожалуйста, введите положительное число или 0 для выхода.")
                continue

            print("\nСгенерированные акции:")
            for _ in range(num_offers):
                print(generate_offer())

        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

# Запуск генератора
if __name__ == '__main__':
    offer_generator()
