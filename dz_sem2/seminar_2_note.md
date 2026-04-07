# Семинар 2: Скользящее окно

## 1. Мотивация

**Проблема:** Найти максимальную сумму подмассива длины `k`.

```
Наивный подход: для каждой позиции считаем сумму заново → O(n*k)
Скользящее окно: «сдвигаем» окно, обновляя сумму за O(1) → O(n)
```

```
Массив: [2, 1, 5, 1, 3, 2], k = 3

Окно 1:  [2, 1, 5]  →  сумма = 8
Окно 2:     [1, 5, 1]  →  8 - 2 + 1 = 7    ← вычли левый, добавили правый
Окно 3:        [5, 1, 3]  →  7 - 1 + 3 = 9   найден максимум!
Окно 4:           [1, 3, 2]  →  9 - 5 + 2 = 6
```

> **Ключевая идея:** не пересчитывать то, что уже посчитано. Переиспользовать результат предыдущего шага.

## 2. Окно фиксированного размера

### Шаблон

```python
def fixed_window(arr, k):
    n = len(arr)
    if n < k:
        return None

    # 1. Инициализируем первое окно
    window_sum = sum(arr[:k])
    best = window_sum

    # 2. Сдвигаем окно: убираем левый элемент, добавляем правый
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        best = max(best, window_sum)

    return best
```

### Задача 1. Максимальная средняя подмассива

```python
# LeetCode 643. Maximum Average Subarray I
def findMaxAverage(nums: list[int], k: int) -> float:
    window = sum(nums[:k])
    best = window

    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)

    return best / k

# Пример
print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # 12.75
```

### Задача 2. Все анаграммы строки в строке

```python
# LeetCode 438. Find All Anagrams in a String
from collections import Counter

def findAnagrams(s: str, p: str) -> list[int]:
    k = len(p)
    if k > len(s):
        return []

    p_count = Counter(p)
    s_count = Counter(s[:k])
    result = []

    if s_count == p_count:
        result.append(0)

    for i in range(k, len(s)):
        # Добавляем правый символ
        s_count[s[i]] += 1
        # Убираем левый символ
        left = s[i - k]
        s_count[left] -= 1
        if s_count[left] == 0:
            del s_count[left]

        if s_count == p_count:
            result.append(i - k + 1)

    return result

print(findAnagrams("cbaebabacd", "abc"))  # [0, 6]
```

### Реальное применение

| Область | Пример |
|---------|--------|
| **Мониторинг** | Среднее время отклика сервера за последние 5 минут |
| **Финансы** | Скользящая средняя цены акций (SMA-20, SMA-50) |
| **Сети** | TCP sliding window — контроль потока данных |
| **IoT/сенсоры** | Сглаживание шума: среднее последних N показаний датчика |

## 3. Окно переменного размера

> Размер окна не задан. Мы **расширяем** окно вправо и **сужаем** слева, пока выполняется/нарушается условие.

### Шаблон

```python
def variable_window(arr, condition_param):
    left = 0
    best = 0
    state = ...  # то, что отслеживаем (сумма, множество, словарь...)

    for right in range(len(arr)):
        # 1. Расширяем окно: добавляем arr[right] в state
        ...

        # 2. Сужаем окно, пока условие нарушено
        while condition_is_broken(state, condition_param):
            # убираем arr[left] из state
            ...
            left += 1

        # 3. Обновляем ответ
        best = max(best, right - left + 1)

    return best
```

### Задача 3. Наибольшая подстрока без повторов

```python
# LeetCode 3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s: str) -> int:
    seen = {}          # символ → его последний индекс
    left = 0
    best = 0

    for right, char in enumerate(s):
        # Если символ уже в окне — сдвигаем левую границу
        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        seen[char] = right
        best = max(best, right - left + 1)

    return best

print(lengthOfLongestSubstring("abcabcbb"))  # 3 ("abc")
print(lengthOfLongestSubstring("pwwkew"))    # 3 ("wke")
```

### Задача 4. Минимальная подстрока, содержащая все символы

```python
# LeetCode 76. Minimum Window Substring
from collections import Counter

def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""

    need = Counter(t)           # сколько каждого символа нужно
    missing = len(t)            # сколько символов ещё не покрыто
    left = 0
    best = (float('inf'), 0, 0) # (длина, left, right)

    for right, char in enumerate(s):
        if need[char] > 0:      # этот символ нам нужен
            missing -= 1
        need[char] -= 1

        # Все символы покрыты — пробуем сузить
        while missing == 0:
            window_len = right - left + 1
            if window_len < best[0]:
                best = (window_len, left, right)

            # Убираем левый символ
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1

    return "" if best[0] == float('inf') else s[best[1]: best[2] + 1]

print(min_window("ADOBECODEBANC", "ABC"))  # "BANC"
```

### Задача 5. Подмассив с суммой ≥ target (минимальной длины)

```python
# LeetCode 209. Minimum Size Subarray Sum
def minSubArrayLen(target: int, nums: list[int]) -> int:
    left = 0
    curr_sum = 0
    best = float('inf')

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            best = min(best, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return best if best != float('inf') else 0

print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2 ([4,3])
```

```
Визуализация работы:

target = 7,  nums = [2, 3, 1, 2, 4, 3]

right=0: [2]                 sum=2  < 7
right=1: [2,3]               sum=5  < 7
right=2: [2,3,1]             sum=6  < 7
right=3: [2,3,1,2]           sum=8  ≥ 7 → best=4, сужаем
           [3,1,2]           sum=6  < 7
right=4:   [3,1,2,4]         sum=10 ≥ 7 → best=4, сужаем
             [1,2,4]         sum=7  ≥ 7 → best=3, сужаем
               [2,4]         sum=6  < 7
right=5:       [2,4,3]       sum=9  ≥ 7 → best=3, сужаем
                 [4,3]       sum=7  ≥ 7 → best=2, сужаем (результат)
                   [3]       sum=3  < 7

Ответ: 2
```

## 4. Два указателя (Two Pointers)

> Смежная техника. Скользящее окно — это **частный случай** двух указателей.

Отличие от скользящего окна:
- Скользящее окно: оба указателя двигаются в **одном** направлении(→ →).
- Два указателя: могут двигаться **навстречу** друг другу (→ ←).


### Задача 6. Пара с заданной суммой (отсортированный массив)

```python
# LeetCode 167. Two Sum II
def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]  # 1-indexed
        elif s < target:
            left += 1      # нужна сумма побольше
        else:
            right -= 1     # нужна сумма поменьше

    return []

print(twoSum([2, 7, 11, 15], 9))  # [1, 2]
```

### Задача 7. Контейнер с наибольшим количеством воды

```python
# LeetCode 11. Container With Most Water
def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        w = right - left
        h = min(height[left], height[right])
        best = max(best, w * h)

        # Двигаем указатель с меньшей высотой
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return best

print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
```

## 5. Префиксные суммы — Prefix Sum

> Ещё одна техника для задач на подмассивы. Дополняет скользящее окно.

```python
# Идея: prefix[i] = sum(arr[0:i])
# Сумма подмассива arr[l:r] = prefix[r] - prefix[l]

def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix
```

### Задача 8. Количество подмассивов с суммой = k

```python
# LeetCode 560. Subarray Sum Equals K
from collections import defaultdict

def subarraySum(nums: list[int], k: int) -> int:
    count = 0
    curr_sum = 0
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1  # пустой префикс

    for num in nums:
        curr_sum += num
        # Ищем: curr_sum - prefix = k  →  prefix = curr_sum - k
        count += prefix_counts[curr_sum - k]
        prefix_counts[curr_sum] += 1

    return count

print(subarraySum([1, 1, 1], 2))      # 2
print(subarraySum([1, 2, 3], 3))      # 2  ([1,2] и [3])
```

## Когда что использовать?

| Техника | Когда полезна | Ограничения |
|---|---|---|
| Скользящее окно | Непрерывные диапазоны, частые сдвиги окна | Не все задачи с отрицательными числами подходят |
| Два указателя | Отсортированные массивы, работа с двумя концами | Часто требует упорядоченности |
| Префиксные суммы | Быстрые суммы на диапазонах, есть отрицательные числа | Не всегда решают задачи на минимум/максимум без доп. структур |


## 6. Задачи для тренировки (LeetCode)

> Без ссылок, но легко ищется. Дайте фидбек кто ими пользовался🙂

### Скользящее окно — фиксированное

| # | Задача | Сложность |
|---|--------|-----------|
| 643 | Maximum Average Subarray I | Easy |
| 1456 | Max Vowels in Substring of Given Length | Medium |
| 438 | Find All Anagrams in a String | Medium |
| 567 | Permutation in String | Medium |
| 239 | Sliding Window Maximum | Hard |

### Скользящее окно — переменное

| # | Задача | Сложность |
|---|--------|-----------|
| 209 | Minimum Size Subarray Sum | Medium |
| 3 | Longest Substring Without Repeating Characters | Medium |
| 424 | Longest Repeating Character Replacement | Medium |
| 713 | Subarray Product Less Than K | Medium |
| 76 | Minimum Window Substring | Hard |
| 30 | Substring with Concatenation of All Words | Hard |

### Два указателя

| # | Задача | Сложность |
|---|--------|-----------|
| 125 | Valid Palindrome | Easy |
| 167 | Two Sum II – Sorted Array | Medium |
| 11 | Container With Most Water | Medium |
| 15 | 3Sum | Medium |
| 42 | Trapping Rain Water | Hard |

### Префиксные суммы

| # | Задача | Сложность |
|---|--------|-----------|
| 303 | Range Sum Query – Immutable | Easy |
| 560 | Subarray Sum Equals K | Medium |
| 523 | Continuous Subarray Sum | Medium |
| 974 | Subarray Sums Divisible by K | Medium |

## 7. Обобщение паттерна

1. Задача про **непрерывный** подмассив / подстроку?
   - Скорее всего, скользящее окно

2. Размер окна **фиксирован**?
   - Да → Инициализируйте окно, сдвигаете на 1
   - Нет → Расширяйте right, сужайте left по условию

3. Что хранить в «состоянии» окна?
   - Сумма / произведение  →  переменная
   - Частоты символов      →  dict / Counter
   - Уникальность          →  set

4. Сложность: O(n) — каждый элемент добавляется и удаляется из окна не более одного раза.
