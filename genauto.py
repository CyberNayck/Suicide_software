import random

# Справочник марок и моделей автомобилей
cars = {
    "Toyota": ["Camry", "Corolla", "RAV4", "Highlander", "Tacoma"],
    "Honda": ["Civic", "Accord", "CR-V", "Pilot", "Fit"],
    "Ford": ["F-150", "Escape", "Mustang", "Explorer", "Focus"],
    "Chevrolet": ["Silverado", "Malibu", "Equinox", "Camaro", "Trax"],
    "Nissan": ["Altima", "Sentra", "Rogue", "370Z", "Murano"],
    "Volkswagen": ["Jetta", "Golf", "Tiguan", "Passat", "Atlas"],
    "BMW": ["3 Series", "5 Series", "X3", "X5", "Z4"],
    "Mercedes-Benz": ["C-Class", "E-Class", "GLC", "GLE", "A-Class"],
    "Kia": ["Forte", "Sorento", "Sportage", "Soul", "Cadenza"],
    "Hyundai": ["Elantra", "Sonata", "Tucson", "Santa Fe", "Kona"],
}

def generate_random_car():
    # Выбор случайной марки
    brand = random.choice(list(cars.keys()))
    # Выбор случайной модели из выбранной марки
    model = random.choice(cars[brand])
    return f"{brand} {model}"

def car_generator():
    while True:
        num_cars = input("\nСколько автомобилей вы хотите сгенерировать? (Введите 0 для выхода): ")
        
        # Прерывание циклов, если введено 0
        if num_cars == '0':
            print("Выход из программы.")
            break

        try:
            num_cars = int(num_cars)
            if num_cars < 0:
                print("Пожалуйста, введите положительное число или 0 для выхода.")
                continue

            print("\nСгенерированные автомобили:")
            for _ in range(num_cars):
                print(generate_random_car())
        
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

# Запуск генератора
if __name__ == "__main__":
    car_generator()
