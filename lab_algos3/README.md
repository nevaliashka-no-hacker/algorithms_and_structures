# Сортировки

## 1. Простые сортировки $O(n²)$

### Пузырьковая сортировка (Bubble Sort)

**Применение:** когда данные почти отсортированы.

```python
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
```

### Сортировка выбором (Selection Sort)

**Применение:** минимизация количества перестановок.

Полезно когда запись данных дорогая операция.

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### Сортировка вставками (Insertion Sort)

**Применение:** малые массивы, почти отсортированные данные.

Используется в TimSort как часть гибридного алгоритма.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

## 2. Эффективные сортировки $O(n log n)$

### Быстрая сортировка (Quick Sort)

**Применение:** общего назначения, средний случай $O(n log n)$.

Используется в стандартных библиотеках (C++ std::sort).

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Оптимизированная версия (in-place)
def quick_sort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

### Сортировка слиянием (Merge Sort)

**Применение:** стабильная сортировка, внешняя сортировка. Сортировка связного списка (удобно делить пополам + слияние).

Гарантированная $O(n log n)$, но требует $O(n)$ памяти.


```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Пирамидальная сортировка (Heap Sort)

**Применение:** гарантированная $O(n log n)$, $O(1)$ памяти.

Используется когда важна предсказуемость времени, топ‑K товаров по продажам, топ‑K запросов по частоте, рейтинг.

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr
```

## 3. Специальные сортировки

### Подсчётом (Counting Sort)

**Применение:** $O(n + k)$, когда диапазон $k$ небольшой.

Пример: сортировка оценок студентов (0-100), возраста, категории, цвета (см. Sort Colors), частоты.

```python
def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1

    count = [0] * range_size
    output = [0] * len(arr)

    # Подсчёт элементов
    for num in arr:
        count[num - min_val] += 1

    # Кумулятивный подсчёт
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Построение выходного массива
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output
```

### Поразрядная (Radix Sort)

**Применение:** $O(d * n)$, где $d$ - количество разрядов.

Пример: Сортировка IP-адресов, дат, номеров.

```python
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr
```

## 4. Реальные применения

### Сортировка объектов по нескольким критериям

```python
students = [
    {'name': 'Alice', 'grade': 85, 'age': 20},
    {'name': 'Bob', 'grade': 90, 'age': 19},
    {'name': 'Charlie', 'grade': 85, 'age': 21}
]

# Сортировка по оценке (убыв.), затем по возрасту (возр.)
sorted_students = sorted(students, key=lambda x: (-x['grade'], x['age']))
```

### K наибольших элементов (используя heap)

```python
import heapq

def k_largest(arr, k):
    return heapq.nlargest(k, arr)
```

### Медиана массива

```python
def find_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
    return sorted_arr[n//2]
```

### Слияние отсортированных файлов (внешняя сортировка)

```python
def merge_k_sorted_arrays(arrays):
    import heapq
    result = []
    heap = []

    # Инициализация heap
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))

    return result
```

### Примеры постановки задач

1. **Логи**: требуется отсортировать события по времени, затем сгруппировать по пользователю.
2. **Планирование**: есть встречи (start, end), требуется слить пересекающиеся/найти минимальное число переговорок.
3. **Топ‑K**: найти 10 самых частых запросов.
4. **Дедупликация**: отсортировать записи по (id, timestamp) и удалить повторы.
5. **Сложная сортировка**: список товаров сортировать по (price asc, rating desc, name asc).

## Сравнительная таблица

| Алгоритм | Лучший | Средний | Худший | Память | Стабильность |
|----------|---------|---------|---------|---------|--------------|
| Bubble Sort | $O(n)$ | $O(n²)$ | $O(n²)$ | $O(1)$ | Да |
| Selection Sort | $O(n²)$ | $O(n²)$ | $O(n²)$ | $O(1)$ | Нет |
| Insertion Sort | $O(n)$ | $O(n²)$ | $O(n²)$ | $O(1)$ | Да |
| Quick Sort | $O(n log n)$ | $O(n log n)$ | $O(n²)$ | $O(log n)$ | Нет |
| Merge Sort | $O(n log n)$ | $O(n log n)$ | $O(n log n)$ | $O(n)$ | Да |
| Heap Sort | $O(n log n)$ | $O(n log n)$ | $O(n log n)$ | $O(1)$ | Нет |
| Counting Sort | $O(n+k)$ | $O(n+k)$ | $O(n+k)$ | $O(k)$ | Да |
| Radix Sort | $O(d*n)$ | $O(d*n)$ | $O(d*n)$ | $O(n+k)$ | Да |
