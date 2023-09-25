# MIPT Project 1 : Number Guessing & Binary Search

### Contents <a name="contents"></a>
[1. About](#about)  
[2. Why?](#why)  
[3. Process](#process)  
[4. Results](#results)    
[5. Conclusions](#conclusions) 

### About <a name="about"></a>
> **Note**
> This is a learning experience.

  
*Угадать загаданное компьютером число за минимальное число попыток.*

### Why? <a name="why"></a>   
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
- Учимся писать хороший код на Python


### Process <a name="process"></a>

<mark>Двоичный (бинарный)</mark> поиск (также известен как метод деления пополам или дихотомия) — классический алгоритм поиска элемента в отсортированном массиве (векторе), использующий дробление массива на половины. 

![Image](binary_search_depiction.png)

<p align="center">Визуализация бинарного поиска по массиву.</p>

<details><summary><b>Пример реализации:</b></summary>

```py
def binary_search(list, key):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        midVal = list[mid]
        if midVal == key:
            return mid
        if midVal > key:
            high = mid - 1
        else:
            low = mid + 1

    return 'not found'
```
</details>



### Results: <a name="results"></a>

The results of the project are...


### Conclusions: <a name="conclusions"></a>

In conclusion, we have learned...


[To begining](#contents)