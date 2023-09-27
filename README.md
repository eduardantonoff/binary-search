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

The `binary_search()` function implements the binary search algorithm to guess a target number. The `num_generator()` function evaluates the performance of the `binary_search()` function by running it 1000 times with random numbers between 1 and 100. 

> **Note**
> This is a learning experience. The primary purpose of this project was to explore the GitHub environment, understand how to write an informative README, and enhance Python coding skills.

### Project Description <a name="description"></a>   
\
**Objective:**
Develop a program capable of guessing a number in the fewest possible attempts.

**Conditions:**

- The `np.random.randint` generates a random array of 1000 integers between 1 and 100. The next step is to select a random integer between 0 and 100, and the task is to find the quickest way to guess it.

- The algorithm takes into account whether the random number is greater or less than the desired number.

**Quality Metric:**

Results will be evaluated based on the average number of attempts over 1000 repetitions.

**Outcomes:**

- Gained a foundational understanding of the Binary Search Algorithm.
- Attained proficiency in using GitHub environmnet.
- Improved Python coding skills at a fundamental level.
- Developed documentation skills for README creation.
- Applied NumPy tools in practical tasks.

### Process & Findings <a name="process"></a>
\
The problem at hand was to efficiently guess a randomly generated number between 1 and 100. To accomplish this, I needed a strategy that could minimize the number of attempts.

After careful consideration, the binary search algorithm emerged as the most efficient solution. Binary search looks through a sorted list to see if a desired element is in the list. It does this efficiently by halving the search space during each iteration of the program. Basically, binary search finds the middle of the list, asks “is the element I’m looking for larger or smaller than this?” Then it cuts the search space in the list in half and searches only in the left list if the element is smaller, and searches only in the right list if the element is bigger. It repeats this process until it finds the element it is looking for (or reports back that the element isn’t in the list at all). The algorithm uses a divide and conquer (or divide and reduce) approach to search. 

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

The implementation of the binary search algorithm yielded an average of only 5 attempts to guess the randomly generated number over 1000 repetitions, demonstrating its effectiveness in minimizing the number of guesses required.



#### To Explore Further: 
- Binary Search vs. Other Schemes
- Linear Search
- Binary Search Trees
- Hashing
- Other Data Structures

### Results: <a name="results"></a>

The average number of attempts it took to guess the number was 5.


### Conclusions: <a name="conclusions"></a>

Based on the results, I can conclude that the binary search algorithm is an effective way to guess a randomly generated number with the fewest possible attempts. I also learned how to use GitHub and how to write efficient Python code.

### Requirements:

- Python 3.6 or higher
- NumPy 1.19.5

### References: <a name="references"></a>

Wikipedia: [Binary Search Algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm).

Wrtiitng on GitHub: [Basic writing and formatting](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

<!-- <details>
  <summary><b>&nbsp;
  requirements:
  </b></summary>

  - Python 3.x
  - NumPy 1.19.5

</details> -->

---

<center>[Back to the Top](#contents)</center>