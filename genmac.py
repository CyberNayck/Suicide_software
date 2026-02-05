import random

def generate_mac_address():
    """Генерирует случайный MAC-адрес."""
    mac = [random.randint(0x00, 0x7F) for _ in range(6)]  # С Генерацией из 00-7F, чтобы MAC был уникальным
    return ':'.join(f'{x:02x}' for x in mac)

# Пример использования
if __name__ == "__main__":
    print("Генерация случайных MAC-адресов:")
    for _ in range(1000):  # Генерировать 5 MAC-адресов
        print(generate_mac_address())
