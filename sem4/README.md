# Семинар 4: MapReduce

## 1. Теория

### Проблема

Как обрабатывать большие объемы данных:
- подсчёт слов
- агрегация логов
- статистика продаж
- анализ поведения пользователей

### Решение

Модель обработки данных в два этапа:

Данные → `MAP` → (ключ, значение) → `REDUCE` → агрегированный результат

- **Map** — преобразует элементы в пары (key, value)
- **Reduce** — агрегирует значения по ключу в одно значение

```
Map:    [1, 2, 3] → [2, 4, 6]
Reduce: [1, 2, 3] → 6
```

```
Пример: подсчёт суммы квадратов массива чисел
Решение: цепочка из Map и Reduce

Map:    [1, 2, 3, 4]  → [1, 4, 9, 16]
Reduce: [1, 4, 9, 16] → 30
```

### Функциональное программирование

- Чистые функции (без побочных эффектов)
- Иммутабельность данных
- Декларативный стиль


## 2. Реализация

### 2.1 MAP - Базовые примеры

#### Пример 1: Удвоение чисел

```python
numbers = [1, 2, 3, 4, 5]

# Императивный подход
result = []
for n in numbers:
    result.append(n * 2)

# Функциональный подход
result = list(map(lambda x: x * 2, numbers))
# [2, 4, 6, 8, 10]
```

#### Пример 2: Преобразование строк
```python
names = ['alice', 'bob', 'charlie']
capitalized = list(map(str.upper, names))
# ['ALICE', 'BOB', 'CHARLIE']
```

#### Пример 3: Извлечение атрибутов
```python
users = [
    {'name': 'Anna', 'age': 25},
    {'name': 'Boris', 'age': 30},
    {'name': 'Clara', 'age': 28}
]
ages = list(map(lambda u: u['age'], users))
# [25, 30, 28]
```

### 2.2 REDUCE - Базовые примеры

> [!NOTE]
> В отличие от `map`, функция `reduce` должна быть импортирована из модуля `functools`.
> ```python
> from functools import reduce
> ```

#### Пример 1: Сумма элементов
```python
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, numbers)
# 15
```

#### Пример 2: Произведение
```python
product = reduce(lambda acc, x: acc * x, numbers)
# 120
```

#### Пример 3: Максимум
```python
maximum = reduce(lambda acc, x: x if x > acc else acc, numbers)
# 5
```

#### Пример 4: Конкатенация строк
```python
words = ['Hello', 'World', 'Python']
sentence = reduce(lambda acc, word: acc + ' ' + word, words)
# 'Hello World Python'
```

#### Пример 5: Подсчет элементов
```python
fruits = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
count = reduce(
    lambda acc, fruit: {**acc, fruit: acc.get(fruit, 0) + 1},
    fruits,
    {}
)
# {'apple': 3, 'banana': 2, 'cherry': 1}
```

### 2.3 FILTER + MAP + REDUCE

#### Пример: Обработка транзакций

Найти сумму всех **дебетовых** транзакций с `amount` > 50.

```python
transactions = [
    {'id': 1, 'amount': 100, 'type': 'debit'},
    {'id': 2, 'amount': 50, 'type': 'credit'},
    {'id': 3, 'amount': 200, 'type': 'debit'},
    {'id': 4, 'amount': 75, 'type': 'credit'},
]

# Шаг 1: Фильтруем дебетовые
debits = filter(lambda t: t['type'] == 'debit', transactions)

# Шаг 2: Извлекаем суммы
amounts = map(lambda t: t['amount'], debits)

# Шаг 3: Фильтруем > 50
large = filter(lambda a: a > 50, amounts)

# Шаг 4: Суммируем
total = reduce(lambda acc, x: acc + x, large, 0)
# 300

# Цепочка в одну строку
total = reduce(
    lambda acc, x: acc + x,
    filter(
        lambda a: a > 50,
        map(
            lambda t: t['amount'],
            filter(lambda t: t['type'] == 'debit', transactions)
        )
    ),
    0
)
```

### 2.4 Собственные реализации

```python
# Своя реализация map
def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

# Своя реализация reduce
def my_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        accumulator = next(it)
    else:
        accumulator = initializer

    for item in it:
        accumulator = func(accumulator, item)
    return accumulator

# Тестирование

print(my_map(lambda x: x**2, [1, 2, 3, 4]))
# [1, 4, 9, 16]

print(my_reduce(lambda acc, x: acc + x, [1, 2, 3, 4], 0))
# 10
```


## 3. Реальные применения

### 3.1 Анализ логов

```python
logs = [
    "2024-01-15 ERROR Database connection failed",
    "2024-01-15 INFO User logged in",
    "2024-01-15 ERROR Timeout occurred",
    "2024-01-15 WARNING Low memory",
    "2024-01-15 ERROR File not found"
]

# Подсчет ошибок по типам
error_count = reduce(
    lambda acc, log: acc + (1 if 'ERROR' in log else 0),
    logs,
    0
)
# 3
```

### 3.2 Обработка данных электронной коммерции

```python
orders = [
    {'user_id': 1, 'items': [{'price': 100}, {'price': 50}]},
    {'user_id': 2, 'items': [{'price': 200}]},
    {'user_id': 1, 'items': [{'price': 75}]},
]

# Общая выручка
total_revenue = reduce(
    lambda acc, order: acc + reduce(
        lambda sum, item: sum + item['price'],
        order['items'],
        0
    ),
    orders,
    0
)
# 425
```

### 3.3 MapReduce для Big Data (концептуально)

```python
# Подсчет слов в документах (Word Count)
documents = [
    "hello world",
    "hello python",
    "world of python"
]

# MAP фаза: doc → [(word, 1), (word, 1), ...]
def map_phase(doc):
    return [(word, 1) for word in doc.split()]

# Применяем MAP ко всем документам
mapped = []
for doc in documents:
    mapped.extend(map_phase(doc))
# [('hello', 1), ('world', 1), ('hello', 1), ...]

# REDUCE фаза: группируем и считаем
from collections import defaultdict
word_counts = defaultdict(int)
for word, count in mapped:
    word_counts[word] += count

print(dict(word_counts))
# {'hello': 2, 'world': 2, 'python': 2, 'of': 1}
```

### 3.4 Обработка временных рядов

```python
# Скользящее среднее
prices = [100, 102, 101, 105, 110, 108, 112]

def moving_average(data, window=3):
    return [
        reduce(lambda acc, x: acc + x, data[i:i+window]) / window
        for i in range(len(data) - window + 1)
    ]

avg = moving_average(prices)
# [101.0, 102.67, 105.33, 107.67, 110.0]
```


## 4. Задачи для практики на LeetCode

### Легкий уровень
1. **[1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/)** - базовая работа с map
2. **[2114. Maximum Number of Words Found in Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/)** - map + reduce
3. **[1470. Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/)** - трансформация массива

### Средний уровень
4. **[677. Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/)** - хэш-мап + prefix sum
5. **[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)** - reduce для подсчета
6. **[692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)** - map-reduce паттерн
7. **[451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)** - частотный анализ

### Сложный уровень
8. **[336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)** - сложные трансформации
9. **[895. Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/)** - частота + стек


## Пример решения LeetCode задачи

### 347. Top K Frequent Elements

> Дан целочисленный массив `nums` и целое число `k`. Верните `k` наиболее частых элементов. Вы можете вернуть ответ в любом порядке.

> [!TIP]
> Похоже на задачу решаемую в 3 лабораторной работе с помощью кучи.

```
Пример 1:

Вход: nums = [1,1,1,2,2,3], k = 2
Выход: [1,2]

Пример 2:

Вход: nums = [1], k = 1
Выход: [1]

Пример 3:

Вход: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Выход: [1,2]
```

```python
from collections import Counter
from functools import reduce

def topKFrequent(nums, k):
    # Вариант 1: С использованием Counter
    return [x[0] for x in Counter(nums).most_common(k)]

    # Вариант 2: С reduce
    freq = reduce(
        lambda acc, num: {**acc, num: acc.get(num, 0) + 1},
        nums,
        {}
    )
    return sorted(freq.keys(), key=lambda x: freq[x], reverse=True)[:k]

# Тест
print(topKFrequent([1,1,1,2,2,3], 2))  # [1, 2]
```

## Как и когда использовать?

Map–Reduce использует:

- Хеш-таблицы (группировка)
- Ассоциативные массивы (dict)
- Функциональное программирование
- Параллельные вычисления
- Разделяй и властвуй

### Обработка больших данных

В распределённых системах:
- Map работает параллельно на разных узлах
- Reduce агрегирует результат

Используется в:
- Hadoop
- Spark
- ClickHouse
- BigQuery


## Полезные материалы

- [MapReduce Wikipedia](https://en.wikipedia.org/wiki/MapReduce)
- [BigDataSchool](https://bigdataschool.ru/wiki/mapreduce/)
- [Google MapReduce Paper (2004)](https://static.googleusercontent.com/media/research.google.com/ru//archive/mapreduce-osdi04.pdf)
- [Python модуль functools документация](https://docs.python.org/3/library/functools.html)
- [DevDocs Python functools reduce](https://devdocs.io/python~3.14/library/functools#functools.reduce)
- Apache Hadoop/Spark для промышленного MapReduce
