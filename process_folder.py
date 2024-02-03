import os
from multiprocessing.pool import ThreadPool

def process_folder(folder):
    # Функція для обробки кожного підкаталогу в окремому потоці
    # Ваш код обробки каталогу тут

def process_file(file):
    # Функція для обробки кожного файлу в окремому потоці
    # Ваш код обробки файлу тут

def main(folder_path):
    # Отримання списку усіх файлів у папці та підкаталогах
    all_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path)]

    # Створення пулу потоків
    pool = ThreadPool()

    # Запуск обробки кожного підкаталогу та файлу в окремому потоці
    pool.map(process_folder, [file for file in all_files if os.path.isdir(file)])
    pool.map(process_file, [file for file in all_files if os.path.isfile(file)])

if __name__ == "__main__":
    folder_path = "шлях/до/папки/Хлам"
    main(folder_path)
