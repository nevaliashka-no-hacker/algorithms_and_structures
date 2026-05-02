# Хеш-таблицы и хеширование


## 1. Теория

### Проблема

Из реальной жизни:
- Проверка логина пользователя (email → данные пользователя)
- Кэширование результатов запросов
- Подсчет частоты слов
- Таблицы маршрутизации

Обобщение:
- Нужно быстро проверять, встречался ли элемент ранее
- Нужно хранить пары "ключ → значение"
- Нужно выполнять операции поиска, вставки и удаления за $O(1)$ в среднем


### Решение


### Что такое хеш-таблица?
**Хеш-таблица** — структура данных для хранения пар "ключ-значение" с $O(1)$ в среднем для операций поиска, вставки и удаления.

#### **Основные компоненты**

**Хеш-функция** — преобразует ключ в индекс массива.

> [!TIP]
> Хеш-функций существует огромное количество. Также можно сделать свою на основе встроенной в Python:
> ```python
> index = hash(key) % capacity
> ```

Требования:
- Быстрая
- Равномерное распределение
- Детерминированная

**Массив (bucket array)** — хранит данные.

**Механизм разрешения коллизий** — обработка ситуаций, когда разные ключи дают одинаковый хеш.

Методы разрешения коллизий:
1. **Цепочки (chaining)** — каждая ячейка содержит связный список
2. **Открытая адресация** — поиск следующей свободной ячейки
   - Линейное пробирование
   - Квадратичное пробирование
   - Двойное хеширование

### Временная сложность
| Операция | Средний случай | Худший случай |
|----------|----------------|---------------|
| Поиск    | $O(1)$         | $O(n)$        |
| Вставка  | $O(1)$         | $O(n)$        |
| Удаление | $O(1)$         | $O(n)$        |


## 2. Примеры кода

### Базовая реализация

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Простая хеш-функция"""
        return hash(key) % self.size

    def insert(self, key, value):
        """Вставка O(1) в среднем"""
        index = self._hash(key)
        # Проверяем, есть ли ключ
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Обновление
                return
        self.table[index].append((key, value))  # Добавление

    def get(self, key):
        """Поиск O(1) в среднем"""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(key)

    def delete(self, key):
        """Удаление O(1) в среднем"""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
        raise KeyError(key)

# Пример
ht = HashTable()
ht.insert("name", "Alice")
ht.insert("age", 25)
print(ht.get("name"))  # Alice
ht.delete("age")
```

### Встроенные хеш-таблицы

#### dict

```python
phone_book = {}
phone_book["Alice"] = "123-456"
phone_book["Bob"] = "789-012"
print(phone_book.get("Alice"))  # 123-456
```

#### defaultdict

```python
from collections import defaultdict
word_count = defaultdict(int)
for word in ["apple", "banana", "apple"]:
    word_count[word] += 1
print(dict(word_count))  # {'apple': 2, 'banana': 1}
```

#### Counter

```python
from collections import Counter
counter = Counter([1, 2, 2, 3, 3, 3])
print(counter.most_common(2))  # [(3, 3), (2, 2)]
```


### Хеширование строк (Rolling Hash)

> [!NOTE]
> Подробнее про полиномиальное хеширование строк можно почитать на [Algoritmica](https://ru.algorithmica.org/cs/hashing/polynomial/).
>
> Подробнее про Rabin-Karp алгоритм поиска подстроки на [e-maxx](http://e-maxx.ru/algo/rabin_karp).

```python
def polynomial_hash(s, p=31, m=10**9 + 9):
    """Полиномиальное хеширование строки"""
    hash_value = 0
    p_pow = 1
    for char in s:
        hash_value = (hash_value + (ord(char) - ord('a') + 1) * p_pow) % m
        p_pow = (p_pow * p) % m
    return hash_value

# Rabin-Karp алгоритм поиска подстроки
def rabin_karp(text, pattern):
    """O(n + m) поиск подстроки"""
    n, m = len(text), len(pattern)
    if m > n:
        return -1

    p, mod = 31, 10**9 + 9
    p_pow = pow(p, m, mod)

    pattern_hash = polynomial_hash(pattern)
    current_hash = polynomial_hash(text[:m])

    if current_hash == pattern_hash and text[:m] == pattern:
        return 0

    for i in range(1, n - m + 1):
        # Rolling hash: удаляем первый символ и добавляем новый
        current_hash = (current_hash - (ord(text[i-1]) - ord('a') + 1)) % mod
        current_hash = (current_hash * p) % mod
        current_hash = (current_hash + (ord(text[i+m-1]) - ord('a') + 1)) % mod

        if current_hash == pattern_hash and text[i:i+m] == pattern:
            return i

    return -1
```


## 3. Реальные применения

### Кэширование (мемоизация)

> [!TIP]
> Задача может быть решена встроенным в модуль `functools` декоратором `lru_cache` (подробнее в [документации](https://docs.python.org/3/library/functools.html#functools.lru_cache)).

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)  # Обновляем позицию
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Удаляем самый старый
```

### Подсчет частоты элементов

```python
from collections import Counter

def top_k_frequent(nums, k):
    """Топ K частых элементов"""
    count = Counter(nums)
    return [num for num, _ in count.most_common(k)]

# Пример: [1,1,1,2,2,3], k=2 → [1,2]
```

### Группировка анаграмм

```python
from collections import defaultdict

def group_anagrams(words):
    """Группировка слов-анаграмм"""

    anagrams = defaultdict(list)
    for word in words:
        # Используем отсортированное слово как ключ
        key = ''.join(sorted(word))
        anagrams[key].append(word)

    return list(anagrams.values())

# ["eat","tea","tan","ate","nat","bat"]
# → [["eat","tea","ate"],["tan","nat"],["bat"]]
```

### Дедупликация данных

```python
def remove_duplicates(items):
    """Удаление дубликатов с сохранением порядка"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```

## Реальные системы
- `std::unordered_map` и `std::unordered_set` в C++
- `HashMap` в Java
- Индексация в БД
- Redis
- Кэш DNS

## Ключевые выводы

- Хеш-таблицы дают **$O(1)$** для основных операций
- Выбор хеш-функции критичен для избежания коллизий
- В Python используйте `dict`, `set`, `defaultdict`, `Counter`
- Частые паттерны: подсчет частоты, кэширование, поиск пар
- Всегда учитывайте **load factor** и возможность rehashing


## Полезные материалы

- [Хеширование - Algoritmica](https://ru.algorithmica.org/cs/hashing/)
- [Hash Table - Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
- Problem Solving with Algorithms and Data Structures Using Python. Брэд Миллер и Дэвид Рэнум
- [⬆️ Глава про хеш-таблицы в русском переводе](aliev.me/runestone/SortSearch/Hashing.html)
- "Algorithms". Роберт Седжвик и Кевин Уэйн (Глава 3.4)
- "Introduction to Algorithms" (CLRS, Глава 12)
- [MIT 6.006: Hashing](https://www.youtube.com/watch?v=Nu8YGneFCWE)
- [Hash Table - VisuAlgo](https://visualgo.net/en/hashtable)
