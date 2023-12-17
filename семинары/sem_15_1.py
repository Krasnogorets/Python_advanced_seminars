"""
Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.
"""
import logging
from datetime import datetime

FORMAT = '{levelname:<8} - {asctime}.' \
         'в строке {lineno} функция "{funcName}()" ' \
         ' выдало сообщение: {msg}'

logging.basicConfig(filename='sem_15_1.log',
                    encoding='utf-8', level=logging.ERROR, format=FORMAT, style='{', datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)


def log_all():
    logger.error('Поймали ошибку деления на ноль')
    logger.critical('конец работы')


if __name__ == '__main__':
    log_all()
    print(10 / 5)
    print(10 / 0)
    print(5 / 5)
