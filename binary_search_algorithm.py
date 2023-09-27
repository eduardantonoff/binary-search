import numpy as np

def binary_search(number: int = 1) -> int:

    '''
    Guess a randomly generated number using the binary search method.

    Args:
        number (int, optional): The target number to guess. Defaults to 1.
    Returns:
        int: The number of attempts it took to guess the target number.
    '''

    # 1. Initialize variables for the search range and the number of attempts.
    count = 0
    low = 1
    high = 100

    # 2. Loop until the target number is guessed.
    while True:

        # 2.1 Count the number of attempts.
        count += 1
        # 2.2 Calculate the midpoint of the current search range. 
        mid_point = (low + high) // 2

        # 2.3 Check if the predicted number matches the target number.
        if number == mid_point: 
            break

        # 2.4 Adjust the search range based on the comparison.
        elif number < mid_point: 
            high = mid_point - 1
        else:
            low = mid_point + 1

    # 3. Return the number of attempts it took to guess the target number.
    return count

def num_generator(binary_search) -> int:

    '''
    Calculate the average number of attempts it takes for the algorithm to guess a number over 1000 trials.

    Args:
        binary_search (function): The guessing algorithm to evaluate.
    Returns:
        int: The average number of attempts over 1000 trials.
    '''

    # 1. Initialize an empty list to store the number of attempts for each trial.
    count_lst = []

    # 2. Generate an array of 1000 random numbers between 1 and 100.
    random_array = np.random.randint(1, 101, size=(1000))

    # 3. Loop over each random number and run the binary_search function to guess the number.
    for number in random_array:
        count_lst.append(binary_search(number))

    # 4. Calculate the average number of attempts over all trials.
    score = int(np.mean(count_lst))

    # 5. Print the average number of attempts to the console.
    print(f"The algorithm guesses the number in an average of {score} attempts.")

    # 6. Return the average number of attempts over all trials.
    return score

if __name__ == "__main__":
    # Run
    num_generator(binary_search)