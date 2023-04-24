from multiprocessing import cpu_count, Pool
from time import time


def factorize_number(number: int) -> list[int]:
    result = [i for i in range(1, number // 2 + 1) if number % i == 0]
    result.append(number)
    return result


def factorize(numbers: list[[int]]) -> list[int]:
    with Pool(processes=cpu_count()) as pool:
        result = pool.map(func=factorize_number, iterable=numbers)
        print(cpu_count())
    return result


def main():
    numbers = [1280, 2550, 999990, 106510600]
    start = time()
    list_result = factorize(numbers)
    for i in range(len(list_result)):
        print(f'{numbers[i]} -- {list_result[i]}')
    print(f'with multiprocessing {time()-start}')
    #start1 = time()

    # for i in range(len(list_result)):
    #     print(f'{numbers[i]} -- {result[i]}')
    #print(f'with multiprocessing {time() - start1}')


if __name__ == '__main__':
    exit(main())

