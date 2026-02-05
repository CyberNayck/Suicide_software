import os
from TikTokApi import TikTokApi

def download_video(user_url):
    try:
        api = TikTokApi.get_instance()
        
        # Получаем информацию о видео из предоставленной ссылки
        video = api.video(url=user_url)

        # Определяем, где сохранить видео
        path = os.path.join(os.getcwd(), 'tiktok_video.mp4')

        # Скачиваем видео
        with open(path, 'wb') as out_file:
            out_file.write(video.bytes())

        print(f'Видео успешно загружено и сохранено по пути: {path}')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

if __name__ == "__main__":
    while True:
        # Ссылка на видео TikTok для скачивания
        video_url = input("Введите URL видео TikTok (или '0' для выхода): ")
        
        if video_url == '0':
            print("Выход из программы.")
            break
        
        download_video(video_url)
