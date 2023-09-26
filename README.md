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
This project is a Python program that guesses a randomly generated number with the fewest possible attempts.
> **Note**
> This is a learning experience. The primary purpose of this project is to explore GitHub environment and gain proficiency in formatting and meeting 'README' requirements.
 

### Project Description <a name="description"></a>   
\
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
\
Binary search looks through a sorted list to see if a desired element is in the list. It does this efficiently by halving the search space during each iteration of the program. Basically, binary search finds the middle of the list, asks “is the element I’m looking for larger or smaller than this?” Then it cuts the search space in the list in half and searches only in the left list if the element is smaller, and searches only in the right list if the element is bigger. It repeats this process until it finds the element it is looking for (or reports back that the element isn’t in the list at all). The algorithm uses a divide and conquer (or divide and reduce) approach to search. 

<details><summary><b>Implementation Example:</b></summary>

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

\
In simple terms, the algorithm works as follows:


The following assumes zero indexing, meaning that the left-most element of a list is the 
0<sup>th</sup> element.

1. Determine the middle element of a sorted list by taking the value of the floor of $\frac{low + high}{2}$, where low is the lowest index of the list, and high is the highest index in the list. So in the list [1,2,3,4],2 (since 2 occurs at index 1) would be the middle. In the list [1,2,3,4,5], 3 (since 3 occurs at index 2) is the middle.    

2. Compare the value of that middle element with the target value.
\
![Image](binary_search_depiction.png)


3. If the target value is equal to the middle element, return that it is true the element is in the list (if the position of the element in the list is desired, return the index as well).
4. If the target value is less than the middle element, eliminate all elements to the right of (and including) the middle element from the search, and return to step one with this smaller search space.
5. If the target value is greater than the middle element, eliminate all the elements to the left of (and including) the middle element from the search, and return to step one with this smaller search space.

### Results: <a name="results"></a>

The average number of attempts it took to guess the number was 5.


### Conclusions: <a name="conclusions"></a>

Based on the results, I can conclude that the binary search algorithm is an effective way to guess a randomly generated number with the fewest possible attempts. We also learned how to use GitHub and how to write efficient Python code.

### References: <a name="conclusions"></a>

Wikipedia: [Binary Search Algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm).

Youtube: [Binary Search Algorithm in 100 sec](https://www.youtube.com/watch?v=MFhxShGxHWc).

[Back to the Top](#contents)