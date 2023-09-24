"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def binary_predict(number: int = 1) -> int:
    """Угадываем число методом бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100

    while True:
        count += 1
        predict_number = (low + high) // 2  # предполагаемое число как середина текущего диапазона
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number < predict_number:
            high = predict_number - 1  # сужаем диапазон до [low, predict_number - 1]
        else:
            low = predict_number + 1  # сужаем диапазон до [predict_number + 1, high]

    return count

def score_game(binary_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(binary_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score



if __name__ == "__main__":
    # RUN
    score_game(binary_predict)