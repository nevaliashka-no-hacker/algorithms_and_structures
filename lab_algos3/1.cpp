#include <iostream>
#include <set>
#include <vector>

void print_array(int* arr, int n);
void clear_matrix(int** arr, int n);

void swap_intervals(int a[2], int b[2]);

/*
912. Sort an Array

Отсортировать массив по возрастанию, сложность O(n log n) или меньше.
*/

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void heapify(int* arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;

    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

int* sort_an_array(int* arr, int n)  // heap_sort
{
    // Здесь подойдет пирамидальная сортировка

    for (int i = n / 2 - 1; i > -1; i--) {
        heapify(arr, n, i);
    }

    for (int i = n - 1; i > -1; i--) {
        swap(&arr[0], &arr[i]);
        heapify(arr, i, 0);
    }

    return arr;
}

/*
88. Merge Sorted Array

Даны 2 массива, отсортированных по неубыванию и их длины (num1 num2 m n).
Объединить в неубывающем порядке. Результат в num1.
Входные данные: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Выходные данные: [1,2,2,3,5,6]
O(m + n)?
*/

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quick_sort_inplace(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quick_sort_inplace(arr, low, pi - 1);
        quick_sort_inplace(arr, pi + 1, high);
    }
}

void merge_sorted_array1(int nums1[], int m, int nums2[], int n) {
    // складываем все в один список O(n + n log n)
    for (int i = 0; i < n; i++) {
        nums1[m + i] = nums2[i];
    }
    // и сортируем его
    quick_sort_inplace(nums1, 0, m + n - 1);
}

/*
977. Squares of a Sorted Array

Дан массив (неубывающий). Вернуть массив квадратов в неубывающем порядке.
Входные данные: nums = [-4,-1,0,3,10]
Выходные данные: [0,1,9,16,100]
O(n)?
*/

void square(int* arr, int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = arr[i] * arr[i];
    }
}

int* square_of_a_sorted_array1(int* arr, int n) {
    // 1 способ: в квадрат и сортируем O(n + n log n)
    square(arr, n);

    // пирамидальная сортировка из первого задания
    sort_an_array(arr, n);

    return arr;
}

/*
int* square_of_a_sorted_array2(int* arr, int n)
{
    // 2 способ: проход по каждому элементу, его сортировка и квадрат O(n)
    // попытка 1
    for (int i = 0; i < n - 1; i++)
    {
        if (arr[i] * arr[i] > arr[i + 1] * arr[i + 1])
        {
            arr[i + 1] = arr[i + 1] * arr[i + 1];
            swap(&arr[i], &arr[i + 1]);
        }
    }

    // попытка 2
    int i = n - 1;
    while (i != 0)
    {
        arr[i] = arr[i] * arr[i];
        if (arr[i] < arr[i - 1] * arr[i - 1])
        {
            arr[i - 1] = arr[i - 1] * arr[i - 1];
            swap(&arr[i], &arr[i - 1]);
        }
        i -= 1;
    }

    return arr;
}
*/

/*
56. Merge Intervals

Дан массив интервалов. Объединить эти интервалы.
Входные данные: intervals = [[1,3],[2,6],[8,10],[15,18]]
Выходные данные: [[1,6],[8,10],[15,18]]
Пояснение: Поскольку интервалы [1,3] и [2,6] пересекаются, объединим их в [1,6].
*/

int max(int a, int b) {
    if (a > b) return a;
    return b;
}

void swap_intervals(int a[2], int b[2]) {
    int temp[2] = {a[0], a[1]};
    a[0] = b[0];
    a[1] = b[1];
    b[0] = temp[0];
    b[1] = temp[1];
}

void quick_sort(int a[][2], int lo, int hi) {
    if (lo >= hi) return;
    int pivot = a[lo + (hi - lo) / 2][1];  // опорный — средний элемент
    int i = lo, j = hi;
    while (i <= j) {
        while (a[i][1] < pivot) i++;
        while (a[j][1] > pivot) j--;
        if (i <= j) {
            swap_intervals(a[i], a[j]);
            i++;
            j--;
        }
    }
    quick_sort(a, lo, j);
    quick_sort(a, i, hi);
}

int** merge_intervals(int arr[][2], int n, int* res_len) {
    quick_sort(arr, 0, n - 1);

    int j = 0;
    int** res = new int*[n];
    for (int i = 0; i < n; i++) {
        res[i] = new int[2];
    }

    res[0][0] = arr[0][0];
    res[0][1] = arr[0][1];
    for (int i = 0; i < n; i++) {
        if (arr[i][0] <= res[j][1]) {
            res[j][1] = max(res[j][1], arr[i][1]);
        } else {
            j++;
            res[j][0] = arr[i][0];
            res[j][1] = arr[i][1];
        }
    }

    *res_len = j + 1;
    return res;
}

/*
452. Minimum Number of Arrows to Burst Balloons

На стене шары. Дан двумерный массив интервалов возможного диаметра шара (от x до x).
Стрелы выпускаются вертикально (+y). Если стрела выпущена в нужном диапазоне,
шар лопается. Минимальное кол-во стрел, чтобы все шары лопнули.
Входные данные: points = [[10,16],[2,8],[1,6],[7,12]]
Выходные данные: 2
Пояснение: Шарики можно лопнуть с помощью двух стрел:
- Выстрелите в точку с координатой x = 6, чтобы лопнуть шарики [2,8] и [1,6].
- Выстрелите в точку с координатой x = 11, чтобы лопнуть шарики [10,16] и [7,12].
*/

void qs_rec(int a[][2], int lo, int hi) {
    if (lo >= hi) return;
    int pivot = a[lo + (hi - lo) / 2][1];  // опорный — средний элемент
    int i = lo, j = hi;
    while (i <= j) {
        while (a[i][1] < pivot) i++;
        while (a[j][1] > pivot) j--;
        if (i <= j) {
            swap_intervals(a[i], a[j]);
            i++;
            j--;
        }
    }
    qs_rec(a, lo, j);
    qs_rec(a, i, hi);
}

int min_num_of_arrows_to_burst_balloons(int balloons[][2], int n) {
    qs_rec(balloons, 0, n - 1);

    int i = 0, res = 0;
    int temp;
    while (i < n) {
        temp = balloons[i][1];
        i++;
        if (balloons[i][0] <= temp && temp <= balloons[i][1]) {
            i++;
            res++;
        }
    }

    return res;
}

/*
75. Sort Colors

Дан массив с объектами 3 цветов: красного 0, белого 1 и синего 2.
Отсортировать по возрастанию (In-place algorithm).
*/

int partition_colors(int* arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quick_sort_inplace_colors(int* arr, int low, int high) {
    if (low < high) {
        int pi = partition_colors(arr, low, high);
        quick_sort_inplace_colors(arr, low, pi - 1);
        quick_sort_inplace_colors(arr, pi + 1, high);
    }
}

void sort_colors(int* arr, int n) { quick_sort_inplace_colors(arr, 0, n - 1); }

void print_array(int* arr, int n) {
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
}

int main() {
    int n = 0, m = 0;

    // 1
    std::cout << "Sort an Array" << std::endl;
    n = 7;
    int arr1[] = {10, 3, 2, 6, 1, 8, 9};

    print_array(sort_an_array(arr1, n), n);

    std::cout << std::endl;

    // 2
    std::cout << "Merge Sorted Array" << std::endl;
    n = 3;
    m = 3;
    int arr21[] = {1, 2, 3, 0, 0, 0};
    int arr22[] = {2, 5, 6};
    merge_sorted_array1(arr21, m, arr22, n);
    print_array(arr21, m + n);

    std::cout << std::endl;

    // 3
    std::cout << "Squares of a Sorted Array" << std::endl;

    n = 5;
    int arr3[] = {-4, -1, 0, 3, 10};

    print_array(square_of_a_sorted_array1(arr3, n), n);
    // print_array(square_of_a_sorted_array2(arr3, n), n);

    std::cout << std::endl;

    // 4
    std::cout << "Merge Intervals" << std::endl;

    n = 4;
    int res_len;
    int intervals[][2] = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};

    int** result = merge_intervals(intervals, n, &res_len);
    std::cout << '{';
    for (int i = 0; i < res_len; i++) {
        std::cout << " { " << result[i][0] << ", " << result[i][1];
        if (i == res_len - 1) {
            std::cout << " } ";
        } else {
            std::cout << " },";
        }
    }
    std::cout << '}';
    clear_matrix(result, res_len);

    std::cout << std::endl;

    // 5
    std::cout << "Minimum Number of Arrows to Burst Balloons" << std::endl;

    n = 4;
    int balloons[][2] = {{10, 16}, {2, 8}, {1, 6}, {7, 12}};
    std::cout << min_num_of_arrows_to_burst_balloons(balloons, n) << std::endl;

    // 6
    std::cout << "Sort Colors" << std::endl;

    n = 6;
    int arr6[] = {1, 0, 2, 2, 0, 1};
    sort_colors(arr6, n);

    print_array(arr6, n);

    std::cout << std::endl;

    return 0;
}
