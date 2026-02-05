import random

def generate_random_color():
    """Генерирует случайный цвет в формате RGB и шестнадцатеричном."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    # Формат RGB
    rgb_color = (r, g, b)

    # Формат Hex
    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    
    return rgb_color, hex_color

def main():
    while True:
        try:
            count = int(input("Сколько цветов сгенерировать? (введите число, 0 для выхода) "))
            if count == 0:
                print("Выход из программы.")
                break
            elif count < 0:
                print("Пожалуйста, введите положительное число или 0 для выхода.")
                continue
            
            print("\nСгенерированные цвета:")
            for i in range(count):
                rgb, hex_color = generate_random_color()
                print(f"{i + 1}: RGB: {rgb}, HEX: {hex_color}")

            print()  # Пустая строка для удобства
        except ValueError:
            print("Пожалуйста, введите корректное число.")

if __name__ == "__main__":
    main()
