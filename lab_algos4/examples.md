# Примеры использования в разных языках программирования

Примеры использование хеш-таблиц на встроенных в язык или стандартную библиотеку типах/контейнерах.


## Python

В Python сразу несколько типов реализуют "под капотом" хеш-таблицы.

Ограничения хешируемых объектов:

- **Неизменяемость**: хешируемый объект должен быть неизменяемым после создания. Это означает, что его состояние не может быть изменено.
- **Детерминированность**: для одного и того же хешируемого объекта функция хеширования всегда будет выдавать один и тот же хеш.
- **Уникальность хешей**: разные хешируемые объекты должны иметь разные хеши.

| Тип | Хешируемый? | Причина |
|-----|------------|---------|
| `int`, `float`, `str` | Да | Встроенные неизменяемые типы |
| `tuple` | Да (если содержит только хешируемые элементы) | Неизменяемый контейнер |
| `list`, `dict`, `set` | Нет | Изменяемые контейнеры |
| `frozenset` | Да | Неизменяемое множество |
| Пользовательский класс | По умолчанию | По умолчанию хешируем, но теряет хешируемость если переопределить `__eq__` |

```python
phone_book = {}
phone_book["Alice"] = "123-456"
phone_book["Bob"] = "789-012"
print(phone_book.get("Alice"))  # 123-456
```

```python
from collections import defaultdict
word_count = defaultdict(int)
for word in ["apple", "banana", "apple"]:
    word_count[word] += 1
print(dict(word_count))  # {'apple': 2, 'banana': 1}
```

```python
from collections import Counter
counter = Counter([1, 2, 2, 3, 3, 3])
print(counter.most_common(2))  # [(3, 3), (2, 2)]
```


## C++

В C++ `std::unordered_map` и `std::unordered_set` реализуют концепцию хранения ключ-значение, что фактически реализуется хеш-таблицей "под капотом" (подробнее на cppreference: [map](https://en.cppreference.com/cpp/container/unordered_map), [set](https://en.cppreference.com/cpp/container/unordered_set)).

```cpp
#include <unordered_map>
#include <string>

std::unordered_map<std::string, int> ages;
ages["Alice"] = 25;
ages["Bob"] = 30;

if (ages.find("Alice") != ages.end()) {
    std::cout << ages["Alice"];  // 25
}
```
