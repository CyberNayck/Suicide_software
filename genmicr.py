import random
import string
import os

# Файл для хранения общего количества сгенерированных записей
count_file = "total_microsoft_records_generated.txt"

def read_total_count():
    """Читает общее количество сгенерированных записей из файла."""
    if os.path.exists(count_file):
        with open(count_file, 'r') as file:
            return int(file.read().strip())
    return 0

def write_total_count(count):
    """Записывает общее количество сгенерированных записей в файл."""
    with open(count_file, 'w') as file:
        file.write(str(count))

def generate_random_password(length=12):
    """Генерирует случайный пароль заданной длины."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def generate_record(record_number):
    """Генерирует запись с логином и паролем."""
    email = f"user{record_number}@example.com"
    password = generate_random_password()
    return f"Email: {email}, Password: {password}"

def main():
    total_count = read_total_count()  # Чтение общего количества записей из файла

    while True:
        try:
            count = int(input("Сколько записей Microsoft с паролем сгенерировать? (введите число, 0 для выхода) "))
            if count == 0:
                print("Выход из программы.")
                break
            elif count < 0:
                print("Пожалуйста, введите положительное число или 0 для выхода.")
                continue

            # Генерация записей и сохранение
            with open("microsoft_records.txt", "a") as file:
                for i in range(1, count + 1):
                    record = generate_record(total_count + i)
                    file.write(record + "\n")
                    print(record)  # Выводим запись на экран

            total_count += count  # Увеличиваем общее количество сгенерированных записей
            write_total_count(total_count)  # Записываем новое общее количество в файл
            print(f"\nСгенерировано всего {total_count} записей Microsoft.")

        except ValueError:
            print("Пожалуйста, введите корректное число.")

if __name__ == "__main__":
    main()
