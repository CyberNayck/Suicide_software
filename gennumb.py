import random
import string

def generate_plate(region_code):
    # Генерация 3 случайных букв
    letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    # Генерация 3 случайных цифр
    numbers = ''.join(random.choice(string.digits) for _ in range(3))
    # Формирование номера
    plate_number = f"{letters}{numbers} {region_code}"
    return plate_number

def car_plate_generator():
    print("Генератор номерных знаков автомобилей")
    
    # Предопределенные коды регионов (можно добавить больше)
    region_codes = [f"{i:02}" for i in range(1, 100)]  # От 01 до 99

    while True:
        num_plates = input("\nСколько номерных знаков вы хотите сгенерировать? (Введите 0 для выхода): ")

        if num_plates == '0':
            print("Выход из программы.")
            break

        try:
            num_plates = int(num_plates)
            if num_plates < 0:
                print("Пожалуйста, введите положительное число или 0 для выхода.")
                continue

            print("\nСгенерированные номерные знаки:")
            for _ in range(num_plates):
                # Случайный выбор кода региона
                region_code = random.choice(region_codes)
                print(generate_plate(region_code))
        
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

# Запуск генератора
if __name__ == "__main__":
    car_plate_generator()
