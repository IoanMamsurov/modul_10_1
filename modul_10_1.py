from time import sleep
import datetime
import threading


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


time_start = datetime.datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_stop = datetime.datetime.now()
time = time_stop - time_start
print(f'Время работы функций {time}')
time_start_2 = datetime.datetime.now()
thread_1 = threading.Thread(target=write_words, args=(10, 'example1.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example1.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example1.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example1.txt'))
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
time_stop_2 = datetime.datetime.now()
time_2 = time_stop_2 - time_start_2
print(f'Время работы функций {time_2}')
