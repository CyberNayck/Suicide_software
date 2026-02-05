import random
import string

def generate_license(length=16):
    """Генерирует случайную лицензию заданной длины."""
    # Лицензия будет состоять из случайных букв и цифр
    characters = string.ascii_uppercase + string.digits  # Буквы и цифры
    license_key = ''.join(random.choice(characters) for _ in range(length))
    return license_key

def license_generator():
    print("Генератор лицензий")
    
    while True:
        num_licenses = input("\nСколько лицензий вы хотите сгенерировать? (Введите 0 для выхода): ")
        
        if num_licenses == '0':
            print("Выход из программы.")
            break
            
        try:
            num_licenses = int(num_licenses)
            if num_licenses < 0:
                print("Пожалуйста, введите положительное число или 0 для выхода.")
                continue
                
            print("\nСгенерированные лицензии:")
            for _ in range(num_licenses):
                print(generate_license())
                
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

# Запуск генератора
if __name__ == '__main__':
    license_generator()
