import time
import multiprocessing
from multiprocessing import Pool

def read_info(name):
    all_data = []
    # file = open(name, 'r', encoding='utf-8')
    # for line in file:
    #     #print(line)
    #     all_data.append(line.splitlines())
    # return all_data

    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line.splitlines())
    return all_data


if __name__ == '__main__':
    filenames = [f'./file {numbers}.txt' for numbers in range(1, 5)]
    print(f'Список файлов: {filenames}')
    time_start = round(time.time(), 2)
    for filename in filenames:
        all_data = read_info(filename)
        #print(f'Длина списка данных {filename}: {len(all_data)}')
    time_end = round(time.time(), 2)
    #print(f'Время выполнения: {time_end} - {time_start} = {time_end - time_start}')
    print(f'Время выполнения линейного вызова :  {round(time_end - time_start, 2)}')

    with Pool(len(filenames)) as pool:
        time_start = round(time.time(), 2)
        pool.map(read_info, filenames)
        time_end = round(time.time(), 2)
        #print(f'Время выполнения multiprocessing: {time_end} - {time_start} = {time_end - time_start}')
        print(f'Время выполнения многопроцессорного вызова: {round(time_end - time_start)}')




