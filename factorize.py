from multiprocessing import Pool, cpu_count

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def synchronous_factorize(numbers):
    result = [factorize(number) for number in numbers]
    return result

def parallel_factorize(numbers):
    with Pool(cpu_count()) as pool:
        result = pool.map(factorize, numbers)
    return result

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    # Синхронна версія
    synchronous_result = synchronous_factorize(numbers)
    print("Synchronous result:", synchronous_result)
