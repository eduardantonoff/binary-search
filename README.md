# MIPT Project 1 : Number Guessing


### Contents <a name="contents"></a>

[1. About](#about)  
[2. Project Description](#description)  
[3. Process & Findings](#process)  
[4. Results](#results)    
[5. Summary](#conclusions)  
[6. References](#references)  

### About <a name="about"></a> 
\
This project contains a Python implementation of the binary search algorithm for guessing a target number between 1 and 100. The `binary_search_algorithm.py` file contains two functions: `binary_search()` and `num_generator()`.

The `binary_search()` function implements the binary search algorithm to guess a target number. 

The `num_generator()` function evaluates the performance of the `binary_search()` function by running it 1000 times with random numbers between 1 and 100. 

> **Note**
> This is a learning experience. The primary purpose of this project is to explore GitHub environment and gain proficiency in formatting and meeting 'README' requirements.

### Project Description <a name="description"></a>   
\
**Objective:**
Develop a program capable of guessing a number in the fewest possible attempts.

**Conditions:**

- The `np.random.randint` generates a random array of 1000 integers between 1 and 100. Next an integer a random integer between 0 and 100 is selected, and out task is to find quickesat way to guess it.

- The algorithm takes into account whether the random number is greater or less than the desired number.

**Quality Metric:**

Results will be evaluated based on the average number of attempts over 1000 repetitions.

**Outcomes:**

- Gaining proficiency in writing efficient Python code.
- Getting familiar with GitHub environment.
- Learning README functionality and desgin.
- Applying NumPy knowlegde aquired on SF.


<!-- The program employs a binary search algorithm to guess the number. This algorithm adjusts its guesses based on whether the randomly generated number is greater or less than the current guess. We conducted 1000 trials of the program and recorded the average number of attempts required to guess the number. -->

### Process & Findings <a name="process"></a>
\
Binary search looks through a sorted list to see if a desired element is in the list. It does this efficiently by halving the search space during each iteration of the program. Basically, binary search finds the middle of the list, asks “is the element I’m looking for larger or smaller than this?” Then it cuts the search space in the list in half and searches only in the left list if the element is smaller, and searches only in the right list if the element is bigger. It repeats this process until it finds the element it is looking for (or reports back that the element isn’t in the list at all). The algorithm uses a divide and conquer (or divide and reduce) approach to search. 

#### Implementation Example:

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

\
_In simple terms, the algorithm works as follows:_


The following assumes zero indexing, meaning that the left-most element of a list is the 
0<sup>th</sup> element.

1. Determine the middle element of a sorted list by taking the value of the floor of `low + high // 2`, where low is the lowest index of the list, and high is the highest index in the list. So in the list `[ 1,2,3,4 ]`, 2 (since 2 occurs at index 1) would be the middle. In the list `[ 1,2,3,4,5 ]`, 3 (since 3 occurs at index 2) is the middle.    

2. Compare the value of that middle element with the target value.

![Image](binary_search_depiction.png)

3. If the target value is equal to the middle element, return that it is true the element is in the list (if the position of the element in the list is desired, return the index as well).

4. If the target value is less than the middle element, eliminate all elements to the right of (and including) the middle element from the search, and return to step one with this smaller search space.

5. If the target value is greater than the middle element, eliminate all the elements to the left of (and including) the middle element from the search, and return to step one with this smaller search space.

### Results: <a name="results"></a>

The average number of attempts it took to guess the number was 5.


### Conclusions: <a name="conclusions"></a>

Based on the results, I can conclude that the binary search algorithm is an effective way to guess a randomly generated number with the fewest possible attempts. We also learned how to use GitHub and how to write efficient Python code.

### References: <a name="references"></a>

Wikipedia: [Binary Search Algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm).

<!-- <details>
  <summary><b>&nbsp;
  requirements:
  </b></summary>

  - Python 3.x
  - NumPy 1.19.5

</details> -->


[Back to the Top](#contents)