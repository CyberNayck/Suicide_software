import random

# Списки городов, улиц и других элементов
cities = [
    "Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань",
    "Нижний Новгород", "Челябинск", "Омск", "Самара", "Ростов-на-Дону"
]

streets = [
    "Ленина", "Пушкина", "Гагарина", "Лермонтова", "Советская",
    "Кирова", "Тракторостроителей", "Свободы", "Калинина", "Свердлова"
]

regions = [
    "Центральный", "Северо-Западный", "Уральский", "Сибирский", "Приволжский",
    "Южный", "Дальневосточный"
]

def generate_random_address():
    """Генерирует случайный российский адрес."""
    city = random.choice(cities)
    street = random.choice(streets)
    house_number = random.randint(1, 100)
    apartment_number = random.randint(1, 100)
    region = random.choice(regions)
    
    return f"{city}, {street} ул., д. {house_number}, кв. {apartment_number}, Регион: {region}"

# Пример использования
if __name__ == "__main__":
    print("Генерация случайных русских адресов:")
    for _ in range(1000):  # Генерируем 10 адресов
        print(generate_random_address())
