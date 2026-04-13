import time
import random
import bisect
import matplotlib.pyplot as plt

def linear_search(arr, x):
    for i, val in enumerate(arr):
        if val == x:
            return i
    return -1

sizes = [100, 1000, 10000, 100000, 500000, 1000000]
linear_times = []
binary_times = []

for n in sizes:
    arr = list(range(n))
    x = random.choice(arr)

    # Линейный
    start = time.time()
    linear_search(arr, x)
    linear_times.append(time.time() - start)

    # Бинарный
    start = time.time()
    bisect.bisect_left(arr, x)
    binary_times.append(time.time() - start)

plt.plot(sizes, linear_times, label="Linear")
plt.plot(sizes, binary_times, label="Binary")
plt.legend()
plt.xscale("log")
plt.show()