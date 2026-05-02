# Лабораторная работа 4: Хеш-таблицы и хеширование

## Теория
- Изучить различные хеш-функции (MurmurHash, CityHash)
- Понять, почему `load factor` важен для производительности

## Практика
1. Решить 5 задач с LeetCode
2. Реализовать хеш-таблицу с открытой адресацией
3. **Доп. баллы** (необязательное): Реализовать Bloom Filter ([Wikipedia](https://en.wikipedia.org/wiki/Bloom_filter))

## Задачи на LeetCode

### Базовый уровень
1. **[1. Two Sum](https://leetcode.com/problems/two-sum/)**
   - Найти два числа, дающих заданную сумму
   - Ключевая идея: хранить `{число: индекс}`

2. **[217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)**
   - Есть ли дубликаты в массиве

3. **[242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)**
   - Проверка анаграмм через подсчет символов

4. **[383. Ransom Note](https://leetcode.com/problems/ransom-note/)**
   - Подсчет доступных символов

### Средний уровень
5. **[49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)**
   - Группировка анаграмм (пример выше)

6. **[128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)**
   - Самая длинная последовательность за $O(n)$

7. **[146. LRU Cache](https://leetcode.com/problems/lru-cache/)**
   - Реализация LRU кэша

8. **[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)**
   - Топ K частых элементов

9. **[560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)**
   - Префиксные суммы + хеш-таблица

### Продвинутый уровень
10. **[41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)**
    - Использование массива как хеш-таблицы

11. **[76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)**
    - Скользящее окно + хеш-таблица

12. **[149. Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/)**
    - Хеширование углов наклона
