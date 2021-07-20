import numpy as np


def score(num):
    """Угадываем число, учитываем кол-во попыток"""
    count = 1   # счётчик попыток
    predict = 50  # предпологаемое число
    mediator = 25  # дельта числа, для сужения диапазона
    while True:
        if num == predict:
            break
        elif num > predict:
            predict = predict + mediator
        elif num < predict:
            predict = predict - mediator
        count = count + 1
        mediator = mediator//2
        if mediator < 1:
            mediator = 1
    return count

count_ = []
s = 0
for i in range(1, 1001):
    number = np.random.randint(1, 101)      # загадали число
    count_.append(score(number))            # за сколько угадывается число

s = sum(count_) / 1000                     # среднее значение за 1000 попыток
print(f'В среднем за {s} попыток угадывается число')




