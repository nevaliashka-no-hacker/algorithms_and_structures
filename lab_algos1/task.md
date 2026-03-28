# Задачи на лабораторную работу

## Важные комментарии по измерению времени

### Не все функции надо запускать на одинаковых размерах

Иначе программа будет работать слишком долго.

Ниже представлены предлагаемые значения для замеров функций. Если позволяет компьютер, можно ставить и более высокие значения.

| №  | Функция | Сложность | Рекомендуемый диапазон n |
|----|---------|-----------|--------------------------|
| 1  | `f01_access_middle` | **O(1)** | любой (вызывать в цикле 10⁶+ раз) |
| 2  | `f02_swap_ends` | **O(1)** | любой (вызывать в цикле) |
| 3  | `f03_binary_search` | **O(log n)** | 10³ – 10⁸ (вызывать в цикле) |
| 4  | `f04_lower_bound` | **O(log n)** | 10³ – 10⁸ |
| 5  | `f05_upper_bound` | **O(log n)** | 10³ – 10⁸ |
| 6  | `f06_linear_search` | **O(n)** | 10³ – 10⁷ |
| 7  | `f07_find_max` | **O(n)** | 10³ – 10⁷ |
| 8  | `f08_find_min` | **O(n)** | 10³ – 10⁷ |
| 9  | `f09_sum` | **O(n)** | 10³ – 10⁷ |
| 10 | `f10_count_even` | **O(n)** | 10³ – 10⁷ |
| 11 | `f11_reverse` | **O(n)** | 10³ – 10⁷ |
| 12 | `f12_is_sorted` | **O(n)** | 10³ – 10⁷ |
| 13 | `f13_prefix_sums` | **O(n)** | 10³ – 10⁷ |
| 14 | `f14_merge_sort` | **O(n log n)** | 10³ – 10⁶ |
| 15 | `f15_quick_sort` | **O(n log n)** средн. | 10³ – 10⁶ |
| 16 | `f16_heap_sort` | **O(n log n)** | 10³ – 10⁶ |
| 17 | `f17_count_inversions` | **O(n log n)** | 10³ – 10⁶ |
| 18 | `f18_bubble_sort` | **O(n²)** | 10² – 5·10⁴ |
| 19 | `f19_selection_sort` | **O(n²)** | 10² – 5·10⁴ |
| 20 | `f20_insertion_sort` | **O(n²)** | 10² – 5·10⁴ |
| 21 | `f21_has_pair_sum` | **O(n²)** | 10² – 5·10⁴ |
| 22 | `f22_count_dup_pairs` | **O(n²)** | 10² – 5·10⁴ |
| 23 | `f23_pairwise_product_sum` | **O(n²)** | 10² – 5·10⁴ |
| 24 | `f24_three_sum_bsearch` | **O(n² log n)** | 10² – 10⁴ |
| 25 | `f25_matrix_mult` | **O(dim³)** | dim = 10 – 500 |
| 26 | `f26_three_sum_naive` | **O(n³)** | 10² – 2·10³ |
| 27 | `f27_positive_subsets` | **O(n · 2ⁿ)** | 10 – 25 |
| 28 | `f28_subset_sum` | **O(2ⁿ)** | 10 – 25 |
| 29 | `f29_fib_naive` | **O(2ⁿ)** | 10 – 45 |
| 30 | `f30_count_perms` | **O(n!)** | 4 – 12 |

### Сортировки меняют массив

Если вы хотите сравнивать сортировки правильно, нужно перед каждым запуском делать копию входного массива.

### Компилируйте внимательно

Для правильных замеров компилируйте без оптимизацией, например `-O0`, либо следите, чтобы компилятор не выкинул вычисления как "ненужные".

Проверить себя можно поиском в интернете, либо сравнением полученных результатов с функциями линейной сложности.

Также можно добавить макрос для запрета встравивания функции (метода класса):

```c
#if defined(__GNUC__) || defined(__clang__)
#define NOINLINE __attribute__((noinline))
#elif defined(_MSC_VER)
#define NOINLINE __declspec(noinline)
#else
#define NOINLINE
#endif
```

## Пример простого измерения времени на Си

```c
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n = 100000;
    int *arr = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000;
    }

    clock_t start = clock();
    long long result = func_name(arr, n);
    clock_t end = clock();

    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Result = %lld\n", result);
    printf("Time = %f seconds\n", time_spent);

    free(arr);
    return 0;
}
```

## Функции для замеров

Выберите 5-10 функций и выполните запуск на разном размере (величине) входного массива/индекса/числа. Результаты сохраните с таблицу и постройте графики для каждой.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <time.h>

/* ==========================================================
 *  ГРУППА 1 :  O(1) — константная сложность
 *  Время работы НЕ зависит от размера массива.
 * ========================================================== */

/*  1. Доступ к элементу по индексу
 *
 *  Обращение к a[n/2] — одна операция чтения из памяти.
 *  Сколько бы ни был велик массив, выполняется ровно
 *  одна операция — O(1).
 */
int f01_access_middle(const int *a, int n)
{
    return a[n / 2];
}

/*  2. Обмен первого и последнего элемента
 *
 *  Три присваивания — фиксированное число операций,
 *  не зависящее от n.  O(1).
 */
void f02_swap_ends(int *a, int n)
{
    if (n < 2) return;
    int t    = a[0];
    a[0]     = a[n - 1];
    a[n - 1] = t;
}


/* ==========================================================
 *  ГРУППА 2 :  O(log n) — логарифмическая сложность
 *  Массив должен быть ОТСОРТИРОВАН.
 *  На каждом шаге область поиска сужается вдвое ⇒ log₂ n шагов.
 * ========================================================== */

/*  3. Бинарный поиск (итеративный)
 *
 *  Делим отрезок [lo, hi] пополам, пока не найдём key
 *  или отрезок не станет пустым.  O(log n).
 */
int f03_binary_search(const int *a, int n, int key)
{
    int lo = 0, hi = n - 1;
    while (lo <= hi) {
        int m = lo + (hi - lo) / 2;
        if      (a[m] == key) return m;
        else if (a[m] <  key) lo = m + 1;
        else                  hi = m - 1;
    }
    return -1;
}

/*  4. Lower bound — индекс первого элемента ≥ key
 *
 *  Аналог std::lower_bound из C++.
 *  Тот же принцип деления пополам — O(log n).
 */
int f04_lower_bound(const int *a, int n, int key)
{
    int lo = 0, hi = n;
    while (lo < hi) {
        int m = lo + (hi - lo) / 2;
        if (a[m] < key) lo = m + 1;
        else            hi = m;
    }
    return lo;
}

/*  5. Upper bound — индекс первого элемента > key
 *
 *  Отличается от lower_bound только условием (≤ вместо <).
 *  O(log n).
 */
int f05_upper_bound(const int *a, int n, int key)
{
    int lo = 0, hi = n;
    while (lo < hi) {
        int m = lo + (hi - lo) / 2;
        if (a[m] <= key) lo = m + 1;
        else             hi = m;
    }
    return lo;
}


/* ==========================================================
 *  ГРУППА 3 :  O(n) — линейная сложность
 *  Один проход (или фиксированное число проходов) по массиву.
 * ========================================================== */

/*  6. Линейный поиск
 *
 *  Последовательно проверяем каждый элемент.
 *  В худшем случае (элемента нет) — n сравнений.  O(n).
 */
int f06_linear_search(const int *a, int n, int key)
{
    for (int i = 0; i < n; i++)
        if (a[i] == key) return i;
    return -1;
}

/*  7. Нахождение максимального элемента
 *
 *  Один проход, n−1 сравнений.  O(n).
 */
int f07_find_max(const int *a, int n)
{
    int mx = a[0];
    for (int i = 1; i < n; i++)
        if (a[i] > mx) mx = a[i];
    return mx;
}

/*  8. Нахождение минимального элемента — O(n). */
int f08_find_min(const int *a, int n)
{
    int mn = a[0];
    for (int i = 1; i < n; i++)
        if (a[i] < mn) mn = a[i];
    return mn;
}

/*  9. Сумма всех элементов
 *
 *  Аккумулируем в long long, чтобы избежать переполнения.  O(n).
 */
long long f09_sum(const int *a, int n)
{
    long long s = 0;
    for (int i = 0; i < n; i++) s += a[i];
    return s;
}

/* 10. Подсчёт чётных элементов — O(n). */
int f10_count_even(const int *a, int n)
{
    int c = 0;
    for (int i = 0; i < n; i++)
        if (a[i] % 2 == 0) c++;
    return c;
}

/* 11. Реверс массива на месте
 *
 *  Обмениваем элементы навстречу друг другу.
 *  n/2 обменов — O(n).
 */
void f11_reverse(int *a, int n)
{
    for (int i = 0, j = n - 1; i < j; i++, j--) {
        int t = a[i]; a[i] = a[j]; a[j] = t;
    }
}

/* 12. Проверка, отсортирован ли массив по неубыванию
 *
 *  Один проход с проверкой a[i] >= a[i-1].  O(n).
 */
int f12_is_sorted(const int *a, int n)
{
    for (int i = 1; i < n; i++)
        if (a[i] < a[i - 1]) return 0;
    return 1;
}

/* 13. Построение массива префиксных сумм
 *
 *  out[i] = a[0] + a[1] + ... + a[i].
 *  Один проход — O(n).
 *  (массив out должен быть выделен вызывающим кодом)
 */
void f13_prefix_sums(const int *a, int n, long long *out)
{
    out[0] = a[0];
    for (int i = 1; i < n; i++)
        out[i] = out[i - 1] + a[i];
}


/* ==========================================================
 *  ГРУППА 4 :  O(n log n) — линеарифмическая сложность
 *  Типичная сложность эффективных сортировок.
 * ========================================================== */

/* --- вспомогательные функции для merge sort --- */
static void ms_merge(int *a, int *buf, int l, int m, int r)
{
    int i = l, j = m + 1, k = l;
    while (i <= m && j <= r)
        buf[k++] = (a[i] <= a[j]) ? a[i++] : a[j++];
    while (i <= m) buf[k++] = a[i++];
    while (j <= r) buf[k++] = a[j++];
    memcpy(a + l, buf + l, (size_t)(r - l + 1) * sizeof(int));
}

static void ms_rec(int *a, int *buf, int l, int r)
{
    if (l >= r) return;
    int m = l + (r - l) / 2;
    ms_rec(a, buf, l, m);
    ms_rec(a, buf, m + 1, r);
    ms_merge(a, buf, l, m, r);
}

/* 14. Сортировка слиянием (merge sort)
 *
 *  Рекурсивно делим массив пополам, затем сливаем
 *  два отсортированных половинки.
 *  Глубина рекурсии log n, на каждом уровне O(n) работы.
 *  Итого O(n log n) ГАРАНТИРОВАННО.
 */
void f14_merge_sort(int *a, int n)
{
    int *buf = (int *)malloc((size_t)n * sizeof(int));
    ms_rec(a, buf, 0, n - 1);
    free(buf);
}

/* --- вспомогательные для quick sort (схема Хоара) --- */
static void qs_rec(int *a, int lo, int hi)
{
    if (lo >= hi) return;
    int pivot = a[lo + (hi - lo) / 2]; // опорный — средний элемент
    int i = lo, j = hi;
    while (i <= j) {
        while (a[i] < pivot) i++;
        while (a[j] > pivot) j--;
        if (i <= j) {
            int t = a[i]; a[i] = a[j]; a[j] = t;
            i++; j--;
        }
    }
    qs_rec(a, lo, j);
    qs_rec(a, i, hi);
}

/* 15. Быстрая сортировка (quick sort)
 *
 *  Выбираем опорный элемент, разделяем массив на две части
 *  (< pivot и > pivot), рекурсивно сортируем каждую.
 *  В среднем O(n log n), в худшем O(n^2).
 */
void f15_quick_sort(int *a, int n)
{
    qs_rec(a, 0, n - 1);
}

/* --- вспомогательные функции для heap sort --- */
static void hs_sift(int *a, int n, int i)
{
    for (;;) {
        int big = i, l = 2 * i + 1, r = 2 * i + 2;
        if (l < n && a[l] > a[big]) big = l;
        if (r < n && a[r] > a[big]) big = r;
        if (big == i) break;
        int t = a[i]; a[i] = a[big]; a[big] = t;
        i = big;
    }
}

/* 16. Пирамидальная сортировка (heap sort)
 *
 *  Строим max-heap за O(n), затем n раз извлекаем максимум
 *  (каждый раз O(log n)).  Итого O(n log n) ГАРАНТИРОВАННО.
 */
void f16_heap_sort(int *a, int n)
{
    /* построение кучи */
    for (int i = n / 2 - 1; i >= 0; i--)
        hs_sift(a, n, i);
    /* извлечение максимумов */
    for (int i = n - 1; i > 0; i--) {
        int t = a[0]; a[0] = a[i]; a[i] = t;
        hs_sift(a, i, 0);
    }
}

/* --- вспомогательные функции для подсчёта инверсий --- */
static long long inv_merge(int *a, int *buf, int l, int m, int r)
{
    long long inv = 0;
    int i = l, j = m + 1, k = l;
    while (i <= m && j <= r) {
        if (a[i] <= a[j]) {
            buf[k++] = a[i++];
        } else {
            inv += (m - i + 1); // все оставшиеся в левой половине
            buf[k++] = a[j++];
        }
    }
    while (i <= m) buf[k++] = a[i++];
    while (j <= r) buf[k++] = a[j++];
    memcpy(a + l, buf + l, (size_t)(r - l + 1) * sizeof(int));
    return inv;
}

static long long inv_rec(int *a, int *buf, int l, int r)
{
    if (l >= r) return 0;
    int m = l + (r - l) / 2;
    long long c = 0;
    c += inv_rec(a, buf, l, m);
    c += inv_rec(a, buf, m + 1, r);
    c += inv_merge(a, buf, l, m, r);
    return c;
}

/* 17. Подсчёт инверсий в массиве
 *
 *  Инверсия — пара (i, j), где i < j, но a[i] > a[j].
 *  Используем модифицированный merge sort: при слиянии
 *  считаем, сколько элементов правой половины "обгоняют"
 *  элементы левой.  O(n log n).
 */
long long f17_count_inversions(const int *a, int n)
{
    int *copy = (int *)malloc((size_t)n * sizeof(int));
    int *buf  = (int *)malloc((size_t)n * sizeof(int));
    memcpy(copy, a, (size_t)n * sizeof(int));
    long long res = inv_rec(copy, buf, 0, n - 1);
    free(copy);
    free(buf);
    return res;
}


/* ==========================================================
 *  ГРУППА 5 :  O(n^2) — квадратичная сложность
 *  Два вложенных цикла по n ⇒ порядка n^2 операций.
 * ========================================================== */

/* 18. Сортировка пузырьком (bubble sort)
 *
 *  На каждой итерации внешнего цикла «всплывает» один
 *  максимум.  (n−1) + (n−2) + ... + 1 = n(n−1)/2 сравнений.
 *  O(n^2).
 */
void f18_bubble_sort(int *a, int n)
{
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++)
            if (a[j] > a[j + 1]) {
                int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
            }
}

/* 19. Сортировка выбором (selection sort)
 *
 *  На каждом шаге ищем минимум среди оставшихся и ставим
 *  его на нужное место.  O(n^2).
 */
void f19_selection_sort(int *a, int n)
{
    for (int i = 0; i < n - 1; i++) {
        int mi = i;
        for (int j = i + 1; j < n; j++)
            if (a[j] < a[mi]) mi = j;
        int t = a[i]; a[i] = a[mi]; a[mi] = t;
    }
}

/* 20. Сортировка вставками (insertion sort)
 *
 *  Каждый новый элемент «вставляется» в уже отсортированную
 *  часть массива, сдвигая бОльшие элементы вправо.  O(n^2).
 */
void f20_insertion_sort(int *a, int n)
{
    for (int i = 1; i < n; i++) {
        int key = a[i], j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }
}

/* 21. Наивный поиск пары элементов с заданной суммой (two-sum)
 *
 *  Перебираем все пары (i, j), проверяем a[i]+a[j]==target.
 *  C(n,2) = n(n−1)/2 пар.  O(n^2).
 */
int f21_has_pair_sum(const int *a, int n, int target)
{
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (a[i] + a[j] == target) return 1;
    return 0;
}

/* 22. Подсчёт пар дубликатов
 *
 *  Считаем количество пар (i, j), i < j, где a[i] == a[j].
 *  O(n^2).
 */
long long f22_count_dup_pairs(const int *a, int n)
{
    long long c = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (a[i] == a[j]) c++;
    return c;
}

/* 23. Сумма попарных произведений
 *
 *  S = Σ a[i]·a[j]  для всех 0 ≤ i < j < n.
 *  O(n^2).
 */
long long f23_pairwise_product_sum(const int *a, int n)
{
    long long s = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            s += (long long)a[i] * a[j];
    return s;
}


/* ==========================================================
 *  ГРУППА 6 :  O(n^2 log n)
 * ========================================================== */

/* 24. Поиск тройки с суммой target (с бинарным поиском)
 *
 *  Фиксируем пару (i, j), ищем третий элемент
 *  need = target − a[i] − a[j] бинарным поиском
 *  среди a[j+1 .. n−1].
 *  Пар C(n,2), каждый поиск O(log n) ⇒ O(n^2 log n).
 *  ВАЖНО: массив должен быть отсортирован!
 */
int f24_three_sum_bsearch(const int *a, int n, int target)
{
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) {
            int need = target - a[i] - a[j];
            int lo = j + 1, hi = n - 1;
            while (lo <= hi) {
                int m = lo + (hi - lo) / 2;
                if      (a[m] == need) return 1;
                else if (a[m] <  need) lo = m + 1;
                else                   hi = m - 1;
            }
        }
    return 0;
}


/* ==========================================================
 *  ГРУППА 7 :  O(n^3) — кубическая сложность
 * ========================================================== */

/* 25. Умножение квадратных матриц dim × dim
 *
 *  Стандартный алгоритм: C[i][j] = Σ A[i][k]·B[k][j].
 *  Три вложенных цикла по dim ⇒ O(dim^3).
 *  Матрицы хранятся в одномерных массивах (row-major),
 *  размер каждого: dim * dim.
 */
void f25_matrix_mult(const int *A, const int *B, int *C, int dim)
{
    for (int i = 0; i < dim; i++)
        for (int j = 0; j < dim; j++) {
            long long s = 0;
            for (int k = 0; k < dim; k++)
                s += (long long)A[i * dim + k] * B[k * dim + j];
            C[i * dim + j] = (int)s;
        }
}

/* 26. Наивный поиск тройки с суммой target — O(n^3)
 *
 *  Полный перебор всех троек (i, j, k).
 *  C(n,3) = n(n−1)(n−2)/6 проверок.
 */
int f26_three_sum_naive(const int *a, int n, int target)
{
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            for (int k = j + 1; k < n; k++)
                if (a[i] + a[j] + a[k] == target)
                    return 1;
    return 0;
}


/* ==========================================================
 *  ГРУППА 8 :  O(2^n) — экспоненциальная сложность
 *  Запускать для МАЛЫХ n (до 20–25)!
 * ========================================================== */

/* 27. Подсчёт подмножеств с положительной суммой
 *
 *  Перебираем все 2^n подмножеств с помощью битовой маски.
 *  Для каждой маски суммируем выбранные элементы — O(n).
 *  Итого O(n*2^n).
 */
long long f27_positive_subsets(const int *a, int n)
{
    long long cnt = 0;
    long long total = 1LL << n; // 2^n
    for (long long mask = 1; mask < total; mask++) {
        long long s = 0;
        for (int i = 0; i < n; i++)
            if (mask & (1LL << i))
                s += a[i];
        if (s > 0) cnt++;
    }
    return cnt;
}

/* 28. Задача о сумме подмножеств (subset sum), рекурсия
 *
 *  Для каждого элемента два варианта: включить или нет.
 *  Дерево решений имеет 2^n листьев ⇒ O(2^n).
 */
static int ss_rec(const int *a, int i, int rem)
{
    if (rem == 0) return 1; // нашли подмножество
    if (i < 0)    return 0; // элементы кончились
    // включаем a[i] ИЛИ не включаем
    if (ss_rec(a, i - 1, rem - a[i])) return 1;
    return ss_rec(a, i - 1, rem);
}

int f28_subset_sum(const int *a, int n, int target)
{
    return ss_rec(a, n - 1, target);
}

/* 29. Наивное вычисление числа Фибоначчи — O(2^n)
 *
 *  Классический пример экспоненциальной рекурсии:
 *  fib(n) = fib(n-1) + fib(n-2), без мемоизации.
 *  Дерево рекурсии имеет ~2^n вершин.
 *
 *  (Аргумент — не массив, а число `n`.)
 */
long long f29_fib_naive(int n)
{
    if (n <= 1) return n;
    return f29_fib_naive(n - 1) + f29_fib_naive(n - 2);
}


/* ==========================================================
 *  ГРУППА 9 :  O(n!) — факториальная сложность
 *  Запускать для МАЛЫХ n (до 10–12)
 * ========================================================== */

static long long perm_counter;

static void perm_gen(int *a, int l, int r)
{
    if (l == r) {
        perm_counter++; // учёт перестановки
        return;
    }
    for (int i = l; i <= r; i++) {
        int t = a[l]; a[l] = a[i]; a[i] = t; // swap
        perm_gen(a, l + 1, r);
        t = a[l]; a[l] = a[i]; a[i] = t; // swap back
    }
}

/* 30. Генерация (подсчёт) всех перестановок — O(n!)
 *
 *  Для n элементов существует n! перестановок.
 *  Алгоритм обходит каждую ⇒ O(n!).
 */
long long f30_count_perms(const int *a, int n)
{
    int *copy = (int *)malloc((size_t)n * sizeof(int));
    memcpy(copy, a, (size_t)n * sizeof(int));
    perm_counter = 0;
    perm_gen(copy, 0, n - 1);
    free(copy);
    return perm_counter;
}
```
