import threading
from time import sleep, perf_counter
import requests

def wite_words(word_count, file_name):
    for i in range(word_count):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f'Какое-то слово № {i}')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start = perf_counter()
wite_words(10, 'M10_1_example1.txt')
wite_words(30, 'M10_1_example2.txt')
wite_words(200, 'M10_1_example3.txt')
wite_words(100, 'M10_1_example4.txt')
finish = perf_counter()
print(f'{finish - start} сек без потока')

thread1 = threading.Thread(target = wite_words, args = (10, "M10_1_example5.txt"))
thread2 = threading.Thread(target = wite_words, args = (30, "M10_1_example6.txt"))
thread3 = threading.Thread(target = wite_words, args = (200, "M10_1_example7.txt"))
thread4 = threading.Thread(target = wite_words, args = (100, "M10_1_example8.txt"))

start = perf_counter()
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
finish = perf_counter()

print(f'{finish - start} сек c потоками')
