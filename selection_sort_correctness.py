import numpy as np

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def correct(arr):
    cor = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            cor = False

    if cor:
        print("Selection Sort returns a sorted array correctly")
    else:
        print("Selection sort failed to return a sorted array")


size = 100
array = np.random.randint(0, 1000, size=size)
print(array)
sorted_array = selection_sort(array)
print(sorted_array)
correct(sorted_array)
