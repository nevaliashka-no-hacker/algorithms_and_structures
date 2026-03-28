#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <time.h>

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

void f15_quick_sort(int *a, int n)
{
    qs_rec(a, 0, n - 1);
}

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

int main() {
    int n = 1000;
    int *arr = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000;
    }

    f15_quick_sort(arr, n);
    clock_t start = clock();
    long long result = f24_three_sum_bsearch(arr, n, 123400);
    clock_t end = clock();

    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Result = %lld\n", result);
    printf("Time = %f seconds\n", time_spent);

    free(arr);
    return 0;
}