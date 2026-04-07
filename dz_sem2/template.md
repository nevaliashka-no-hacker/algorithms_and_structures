# Типовые шаблоны

## Фиксированное окно

```python
def fixed_window(nums, k):
    if len(nums) < k:
        return None

    window = sum(nums[:k])
    result = window

    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        result = max(result, window)  # или другая логика

    return result
```

## Переменное окно

```python
def variable_window(nums, target):
    left = 0
    current = 0
    result = 0

    for right in range(len(nums)):
        current += nums[right]

        while current > target:
            current -= nums[left]
            left += 1

        result = max(result, right - left + 1)

    return result
```


## Окно с частотным словарём

```python
from collections import defaultdict

def window_with_counts(s):
    left = 0
    count = defaultdict(int)

    for right in range(len(s)):
        count[s[right]] += 1

        while count[s[right]] > 1:
            count[s[left]] -= 1
            left += 1

    return right - left + 1
```
