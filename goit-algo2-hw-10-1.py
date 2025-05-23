import random
import time
import matplotlib.pyplot as plt


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]
    return (
        deterministic_quick_sort(less)
        + [pivot]
        + deterministic_quick_sort(greater)
    )


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    arr_copy = arr.copy()
    arr_copy.remove(pivot)
    less = [x for x in arr_copy if x <= pivot]
    greater = [x for x in arr_copy if x > pivot]
    return (
        randomized_quick_sort(less)
        + [pivot]
        + randomized_quick_sort(greater)
    )


sizes = [10_000, 50_000, 100_000, 500_000]
rand_times = []
det_times = []

print("\n📊 Порівняння часу виконання алгоритмів:\n")

for size in sizes:
    arr = [random.randint(0, 1_000_000) for _ in range(size)]

    # Рандомізований QuickSort
    rand_total = 0
    for _ in range(5):
        test = arr.copy()
        start = time.time()
        randomized_quick_sort(test)
        rand_total += time.time() - start
    rand_avg = rand_total / 5
    rand_times.append(rand_avg)

    # Детермінований QuickSort
    det_total = 0
    for _ in range(5):
        test = arr.copy()
        start = time.time()
        deterministic_quick_sort(test)
        det_total += time.time() - start
    det_avg = det_total / 5
    det_times.append(det_avg)

    # Виведення результатів
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {rand_avg:.4f} секунд")
    print(f"   Детермінований QuickSort: {det_avg:.4f} секунд\n")

plt.plot(sizes, rand_times, label="Рандомізований QuickSort")
plt.plot(sizes, det_times, label="Детермінований QuickSort")
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
