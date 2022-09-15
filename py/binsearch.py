# binsearch.py
# Steve Sabaugh
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

def binary_search(value, array):
    high = len(data) - 1
    low = 0
    while high >= low:
        middle = (high + low) // 2

        if array[middle] == value:
            return middle

        elif array[middle] > value:
            high = middle - 1

        else:
            low = middle + 1

    return -1


data = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
        144, 233, 377, 610, 987, 1597, 2584, 4181,
        6765, 10946, 17711, 28657, 46368, 75025,
        121393, 196418, 317811]

value1 = 1
value2 = 987
value3 = 2000

print(f'the first occurrence of value {value1} was found at index {binary_search(value1, data)}')
print(f'the first occurrence of value {value2} was found at index {binary_search(value2, data)}')
print(f'the first occurrence of value {value3} was found at index {binary_search(value3, data)}')
