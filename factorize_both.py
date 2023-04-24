from multiprocessing import cpu_count, Pool
from time import time


def factorize_number(number: int) -> list[int]:
    result = [i for i in range(1, number // 2 + 1) if number % i == 0]
    result.append(number)
    return result


def factorize(numbers: list[int]) -> list[list[int]]:
    result = []
    for number in numbers:
        result.append(
            factorize_number(number)
        )
    return result


def factorize_multy(numbers: list[[int]]) -> list[int]:
    with Pool(processes=cpu_count()) as pool:
        result = pool.map(func=factorize, iterable=numbers)
    pass


def main():
    numbers = [1280, 25500, 9999900, 106510600]
    start = time()
    list_result = factorize(numbers)
    # for i in range(len(list_result)):
    #     print(f'{numbers[i]} -- {list_result[i]}')
    print(f'without multiprocessing {time()-start}')
    start1 = time()
    with Pool(processes=cpu_count()) as pool:
        result = pool.map(func=factorize_number, iterable=numbers)
    # for i in range(len(list_result)):
    #     print(f'{numbers[i]} -- {result[i]}')
    print(f'with multiprocessing {time() - start1}')


if __name__ == '__main__':
    exit(main())

# result: without multiprocessing 7.599091291427612
# with multiprocessing 6.0660059452056885