import requests
from bs4 import BeautifulSoup
import os

def download_image(image_url, folder_path):
    try:
        # Запрос на получение изображения
        response = requests.get(image_url)
        
        if response.status_code == 200:
            # Получаем имя файла из URL
            filename = os.path.join(folder_path, image_url.split("/")[-1].split("?")[0])
            
            # Сохраняем изображение
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Скачано: {filename}")
        else:
            print("Ошибка при скачивании изображения:", response.status_code)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def download_pinterest_image(pin_url, folder_path):
    try:
        # Запрос на получение страницы пина
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        response = requests.get(pin_url, headers=headers)
        
        if response.status_code == 200:
            # Парсим страницу
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Ищем все изображения
            image_tags = soup.find_all('img')
            for img in image_tags:
                img_url = img.get('src')
                if img_url:
                    download_image(img_url, folder_path)
        else:
            print("Ошибка при запросе страницы:", response.status_code)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    folder_name = "Pinterest_Images"
    
    # Создаем папку для изображений, если она не существует
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    while True:
        pin_url = input("Введите URL пина Pinterest (или '0' для выхода): ")
        
        if pin_url == '0':
            print("Выход из программы.")
            break
        
        download_pinterest_image(pin_url, folder_name)
