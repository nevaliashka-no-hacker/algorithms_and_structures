#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <time.h>

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

int main() {
    int n = 100000;
    int *arr = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000;
    }

    clock_t start = clock();
    long long result = f03_binary_search(arr, n, 5555);
    clock_t end = clock();

    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Result = %lld\n", result);
    printf("Time = %f seconds\n", time_spent);

    free(arr);
    return 0;
}