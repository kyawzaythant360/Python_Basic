import random

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

numbers = [3, 1, 4, 1, 5]
print("Sorted array:", bogo_sort(numbers))

# Time Complexity is O((n+1)!) and Space Complexity is O(1)