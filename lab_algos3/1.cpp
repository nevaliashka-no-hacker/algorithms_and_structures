#include <iostream>

void print_array(int* arr, int n);

/*
912. Sort an Array

Отсортировать массив по возрастанию, сложность O(n log n) или меньше.
*/

void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void heapify(int* arr, int n, int i)
{
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i)
    {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

int* sort_an_array(int* arr, int n) // heap_sort
{
    // Здесь подойдет пирамидальная сортировка

    for (int i = n / 2 - 1; i > -1; i--)
    {
        heapify(arr, n, i);
    }

    for (int i = n - 1; i > -1; i--)
    {
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

/* //не получилось реализовать
int partition(int* arr, int low, int high)
{
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++)
    {
        if (arr[j] <= pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quick_sort_inplace(int* arr, int low, int high)
{
    if (low < high) 
    {
        int pi = partition(arr, low, high);
        quick_sort_inplace(arr, low, pi - 1);
        quick_sort_inplace(arr, pi + 1, high);
    }
}

void merge_sorted_array1(int* nums1, int m, int* nums2, int n)
{
    // 1 способ
    // складываем все в один список O(n + n log n)
    for (int i = 0; i < n; i++)
    {
        nums1[m + i] = nums2[i];
    }
    // и сортируем его
    quick_sort_inplace(nums1, 0, m);
}
*/

void merge_sorted_array2(int* nums1, int m, int* nums2, int n)
{
    // 2 способ
    // вставить сразу в нужное место через сортировку вставками O(n^3)
    int z;
    int key;
    for (int j = 0; j < n; j++)
    {
        for (int i = 0; i < m; i++)
        {
            key = nums1[i];
            z = i - 1;
            while (z >= 0 && nums1[z] > key)
            {
                nums1[z + 1] = nums2[j];
                z -= 1;
            }
            nums1[z + 1] = key;
        }
    }
}


/*
977. Squares of a Sorted Array

Дан массив (неубывающий). Вернуть массив квадратов в неубывающем порядке.
Входные данные: nums = [-4,-1,0,3,10]
Выходные данные: [0,1,9,16,100]
O(n)?
*/

void square(int* arr, int n)
{
    for (int i = 0; i < n; i++)
    {
        arr[i] = arr[i] * arr[i];
    }
}

int* square_of_a_sorted_array1(int* arr, int n)
{
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


/*
435. Non-overlapping Intervals

Дан массив интервалов. Максимальное кол-во интервалов, которые нужно удалить, 
чтобы не было пересечений. [1, 2] [2, 3] пересечений нет.
Входные данные: intervals = [[1,2],[2,3],[3,4],[1,3]]
Выходные данные: 1
Пояснение: [1,3] можно удалить, а остальные интервалы не пересекаются.
*/


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


/*
347. Top K Frequent Elements

Дан массив и число (nums k). Вернуть ТОП k элементов, встречающихся чаще.
Входные данные: nums = [1,1,1,2,2,3], k = 2
Выходные данные: [1,2]
O(n log n)?
*/


/*
451. Sort Characters By Frequency

Дана строка. Отсортировать ее по убыванию частоты символов.
Входные данные: s = "tree"
Выходные данные: "eert"
*/


/*
75. Sort Colors

Дан массив с объектами 3 цветов: красного 0, белого 1 и синего 2. 
Отсортировать по возрастанию (In-place algorithm).
*/


/*
148. Sort List

Отсортировать связный список по возрастанию.
Входные данные: head = [4,2,1,3]
Выходные данные: [1,2,3,4]
*/

/*
406. Queue Reconstruction by Height

Дан массив людей. Человек: рост, кол-во людей x>=рост впереди стоящих.
Выстроить по логике.
Входные данные: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Выходные данные: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
*/


/*
179. Largest Number

Дан список неотрицательных чисел. Переставить, чтобы получилось неаибольшее число.
Входные данные: nums = [10,2]
Выходные данные: "210"
*/



void print_array(int* arr, int n)
{
    for (int i = 0; i < n; i++) 
    {
        std::cout << arr[i] << " ";
    }
}

int main() 
{
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
    m = 6;
    int arr21[] = {1, 2, 3, 0, 0, 0};
    int arr22[] = {2, 5, 6};
    //2.1
    // merge_sorted_array1(arr21, m, arr22, n);
    //2.2
    merge_sorted_array2(arr21, m, arr22, n);
    print_array(arr1, m);

    // 3
    std::cout << "Squares of a Sorted Array" << std::endl;

    n = 5;
    int arr3[] = {-4, -1, 0, 3, 10};

    print_array(square_of_a_sorted_array1(arr3, n), n);
    // print_array(square_of_a_sorted_array2(arr3, n), n);

    std::cout << std::endl;


   
    return 0;
}
