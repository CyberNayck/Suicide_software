import random

# Список прилагательных
adjectives = [
    "Смелый", "Умный", "Сладкий", "Быстрый", 
    "Творческий", "Злой", "Милый", "Смешной", 
    "Тайный", "Энергичный", "Хитрый", "Доброжелательный", 
    "Счастливый", "Тихий", "Мудрый", "Кромешный",
    "Огромный", "Легендарный", "Яркий", "Спокойный",
    "Беспокойный", "Солнечный", "Темный", "Летучий"
]

# Список никнеймов
nicknames = [
    "Лев", "Сокот", "Волк", "Феникс", 
    "Тигр", "Дракон", "Заяц", "Панда", 
    "Кот", "Енот", "Сова", "Лиса", 
    "Краб", "Рыба", "Орел", "Крокодил", 
    "Кабан", "Слон", "Попугай", "Медведь"
]

def generate_nicknames(number):
    """Генерирует заданное количество никнеймов."""
    generated_nicknames = []
    for _ in range(number):
        adjective = random.choice(adjectives)
        nickname = random.choice(nicknames)
        generated_nicknames.append(f"{adjective}_{nickname}")
    return generated_nicknames

def main():
    while True:
        try:
            count = int(input("Сколько никнеймов сгенерировать? (введите число, 0 для выхода) "))
            if count == 0:
                print("Выход из программы.")
                break
            elif count < 0:
                print("Пожалуйста, введите положительное число или 0 для выхода.")
                continue
            
            result = generate_nicknames(count)
            print("\nСгенерированные никнеймы:")
            for nick in result:
                print(nick)
            print()  # Просто для добавления пустой строки после списка
        except ValueError:
            print("Пожалуйста, введите корректное число.")

if __name__ == "__main__":
    main()
