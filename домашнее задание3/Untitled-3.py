import random
import time
import matplotlib.pyplot as plt

def bubble_sort(lst):
    result = lst.copy()
    n = len(result)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result

def selection_sort(lst):
    result = lst.copy()
    n = len(result)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        if min_idx != i:
            result[i], result[min_idx] = result[min_idx], result[i]
    return result

def insertion_sort(lst):
    result = lst.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result

sizes = [10, 100, 200, 500, 1000]
reps = 5
results = {}

for name, fn in [("Пузырёк", bubble_sort),
                 ("Выбором", selection_sort),
                 ("Вставками", insertion_sort)]:
    times = []
    for n in sizes:
        elapsed = 0.0
        for _ in range(reps):
            data = [random.randint(1, 10000) for _ in range(n)]
            start = time.perf_counter()
            fn(data)
            elapsed += time.perf_counter() - start
        times.append(elapsed / reps * 1000)
    results[name] = times
    for n, t in zip(sizes, times):
        print(f"{name}, размер {n}: {t:.2f} мс")

for name in results:
    plt.plot(sizes, results[name], 'o-', label=name)

plt.xlabel('Размер списка, элементов')
plt.ylabel('Время сортировки, мс')
plt.title('Сравнение алгоритмов сортировки')
plt.legend()
plt.grid(True, alpha=0.4)
plt.savefig('sort_compare.png', dpi=150)
plt.show()