import qrcode

def generate_qr_code(data, filename):
    """Генерирует QR-код из данных и сохраняет в файл."""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

def main():
    while True:
        try:
            count = int(input("Сколько QR-кодов сгенерировать? (введите число, 0 для выхода) "))
            if count == 0:
                print("Выход из программы.")
                break
            elif count < 0:
                print("Пожалуйста, введите положительное число или 0 для выхода.")
                continue
            
            for i in range(count):
                data = input(f"Введите данные для QR-кода {i + 1}: ")
                filename = f"qr_code_{i + 1}.png"
                generate_qr_code(data, filename)
                print(f"Сгенерирован QR-код: {filename}")

        except ValueError:
            print("Пожалуйста, введите корректное число.")

if __name__ == "__main__":
    main()
