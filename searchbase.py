import os
import pandas as pd
import csv
import xlrd
from colorama import init, Fore, Back, Style
import ctypes

ctypes.windll.kernel32.SetConsoleTitleA(b"by @pvpikeakiller")

init()  # Initialize colorama

# Function to get the total size of the 'bd' folder
def get_folder_size():
    total_size = 0
    for dirpath, dirnames, filenames in os.walk("bd"):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

# Function to search in CSV, XLS, and TXT files
def search_in_files(search_query):
    results = []
    for file in os.listdir("bd"):
        if file.endswith((".csv", ".xls", ".txt")):
            if file.endswith(".csv"):
                try:
                    with open(os.path.join("bd", file), 'r', encoding='utf-8', errors='ignore') as f:
                        reader = csv.reader(f)
                        for row in reader:
                            if search_query in str(row):
                                results.append(f"Найдено в  {file}: {', '.join(row)}")
                except Exception as e:
                    print(f"Error reading {file}: {e}")
            elif file.endswith(".xls"):
                try:
                    wb = xlrd.open_workbook(os.path.join("bd", file))
                    for sheet in wb.sheets():
                        for row in range(sheet.nrows):
                            if search_query in str(sheet.row_values(row)):
                                results.append(f"Found in {file} ({sheet.name}): {', '.join(map(str, sheet.row_values(row)))}")
                except Exception as e:
                    print(f"Error reading {file}: {e}")
            elif file.endswith(".txt"):
                try:
                    with open(os.path.join("bd", file), 'r', encoding='utf-8', errors='ignore') as f:
                        for line in f:
                            if search_query in line:
                                results.append(f"Found in {file}: {line.strip()}")
                except Exception as e:
                    print(f"Error reading {file}: {e}")
    return results

# Main program
while True:
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # Show the ASCII menu with a colorful gradient effect
    print(Fore.RED +"""
     
                                 ▄████████ ███    █▄   ▄█   ▄████████  ▄█  ████████▄     ▄████████ 
                                ███    ███ ███    ███ ███  ███    ███ ███  ███   ▀███   ███    ███ 
                                ███    █▀  ███    ███ ███▌ ███    █▀  ███▌ ███    ███   ███    █▀  
                                ███        ███    ███ ███▌ ███        ███▌ ███    ███  ▄███▄▄▄     
                              ▀███████████ ███    ███ ███▌ ███        ███▌ ███    ███ ▀▀███▀▀▀     
                                       ███ ███    ███ ███  ███    █▄  ███  ███    ███   ███    █▄  
                                 ▄█    ███ ███    ███ ███  ███    ███ ███  ███   ▄███   ███    ███ 
                               ▄████████▀  ████████▀  █▀   ████████▀  █▀   ████████▀    ██████████ 
                                               ╭──────────────────────────────────────╮
                                               │          примеры поиска:             │
                                               │      Telegram ID: 6991640260         │
                                               │     Phone number: +790909090         │
                                               │   Fio: Полякова Полина Мийхайловна   │
                                               │          Mail: osint@mail.ru         │
                                               │   Card Number: 1130597301313537787   │
                                               │     Address: улица пушкина дом 13    │
                                               │   VKontakte: https://vk.com/durov    │
                                               │         Username: @seedban           │
                                               ╰──────────────────────────────────────╯
""" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Поиск по базам" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Выход" + Style.RESET_ALL)

    # Show the total size of the 'bd' folder
    total_size = get_folder_size()
    print(Fore.CYAN + f"Общий вес баз данных: {total_size / 1024 / 1024:.2f} MB" + Style.RESET_ALL)

    # Get user input
    choice = input(Fore.WHITE + "Выберите функцию: " + Style.RESET_ALL)

    # Process user input
    if choice == "1":
        search_query = input(Fore.WHITE + "Введите поисковый запрос: " + Style.RESET_ALL)
        results = search_in_files(search_query)
        if results:
            # Clear the console
            os.system('cls' if os.name == 'nt' else 'clear')
            for result in results:
                print(Fore.GREEN + result + Style.RESET_ALL)
            input(Fore.WHITE + "Нажмите Enter для возврата в главное меню..." + Style.RESET_ALL)
        else:
            print(Fore.RED + "В базах данных не найдено результатов." + Style.RESET_ALL)
            input(Fore.WHITE + "Нажмите Enter для возврата в главное меню..." + Style.RESET_ALL)
    elif choice == "2":
        break
    else:
        print(Fore.RED + "Неверный выбор" + Style.RESET_ALL)
