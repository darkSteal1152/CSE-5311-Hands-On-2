import time
import matplotlib.pyplot as plt
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

def benchmark_selection_sort(input_sizes):
    times = []

    for size in input_sizes:
        arr = np.random.randint(0, 10000, size=size)

        start_time = time.time()

        selection_sort(arr)

        end_time = time.time()
        duration = end_time - start_time

        times.append(duration)
        print(f"Size: {size}, Time: {duration:.6f} seconds")

    return times

input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
times = benchmark_selection_sort(input_sizes)

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, times, marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Selection Sort Benchmark')
plt.grid(True)
plt.show()
