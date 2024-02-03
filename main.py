from process_folder import main as process_folder_main
from factorize import synchronous_factorize, parallel_factorize
import time

if __name__ == "__main__":
    # Частина для потоків
    folder_path = "шлях/до/папки/Хлам"
    process_folder_main(folder_path)

    # Частина для процесів
    numbers = [128, 255, 99999, 10651060]

    # Синхронна версія
    start_time = time.time()
    synchronous_result = synchronous_factorize(numbers)
    end_time = time.time()
    print("Synchronous result:", synchronous_result)
    print("Synchronous execution time:", end_time - start_time, "seconds")

