# MIPT Project 1 : Number Guessing

### Contents <a name="contents"></a>

[1. About](#about)  
[2. Project Description](#description)  
[3. Process & Findings](#process)  
[4. Results](#results)    
[5. Summary](#conclusions)  
[6. References](#references)  


### About <a name="about"></a>         
> **Note**
> This is a learning experience. The primary purpose of this project is to explore GitHub environment and gain proficiency in formatting and meeting 'README' requirements.

This project is a Python program that guesses a randomly generated number with the fewest possible attempts. 

### Project Description <a name="description"></a>   

**Objective:**
Develop a program capable of guessing a number in the fewest possible attempts.

**Conditions:**
- The computer randomly selects an integer between 0 and 100, and your task is to guess it. By "guess," we mean "write a program that can guess the number."
- The algorithm takes into account whether the random number is greater or less than the desired number.

**Quality Metric:**
Results will be evaluated based on the average number of attempts over 1000 repetitions.

**What We Practice:**
- Gaining proficiency in writing efficient Python code.

The program employs a binary search algorithm to guess the number. This algorithm adjusts its guesses based on whether the randomly generated number is greater or less than the current guess. We conducted 1000 trials of the program and recorded the average number of attempts required to guess the number.



### Process & Findings <a name="process"></a>

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

The average number of attempts it took to guess the number was 5.


### Conclusions: <a name="conclusions"></a>

Based on the results, I can conclude that the binary search algorithm is an effective way to guess a randomly generated number with the fewest possible attempts. We also learned how to use GitHub and how to write efficient Python code.

### References: <a name="conclusions"></a>

Wikipedia: [Binary Search Algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm).

[Back to the ](#contents)