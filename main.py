import time
import matplotlib.pyplot as plt
import numpy as np

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def benchmark_sort(sort_function, array):
    start_time = time.time()
    sort_function(array.copy())
    end_time = time.time()
    print(f"Size: {size}, Time: {end_time - start_time:.6f} seconds")
    return end_time - start_time

input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

insertion_sort_times = []
selection_sort_times = []
bubble_sort_times = []

for size in input_sizes:
    array = np.random.randint(0, 10000, size=size)

    insertion_sort_times.append(benchmark_sort(insertion_sort, array))
    selection_sort_times.append(benchmark_sort(selection_sort, array))
    bubble_sort_times.append(benchmark_sort(bubble_sort, array))

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, insertion_sort_times, label='Insertion Sort', marker='o')
plt.plot(input_sizes, selection_sort_times, label='Selection Sort', marker='o')
plt.plot(input_sizes, bubble_sort_times, label='Bubble Sort', marker='o')

plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Benchmarking Sorting Algorithms')
plt.legend()
plt.grid(True)

plt.show()
