import time
import matplotlib.pyplot as plt
import numpy as np

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

def benchmark_bubble_sort(input_sizes):
    times = []

    for size in input_sizes:
        arr = np.random.randint(0, 10000, size=size)

        start_time = time.time()

        bubble_sort(arr)

        end_time = time.time()
        duration = end_time - start_time

        times.append(duration)
        print(f"Size: {size}, Time: {duration:.6f} seconds")

    return times

input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
times = benchmark_bubble_sort(input_sizes)

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, times, marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Bubble Sort Benchmark')
plt.grid(True)
plt.show()
