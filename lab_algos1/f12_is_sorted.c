#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <time.h>

int f12_is_sorted(const int *a, int n)
{
    for (int i = 1; i < n; i++)
        if (a[i] < a[i - 1]) return 0;
    return 1;
}

int main() {
    int n = 100000;
    int *arr = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000;
    }

    clock_t start = clock();
    long long result = f12_is_sorted(arr, n);
    clock_t end = clock();

    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Result = %lld\n", result);
    printf("Time = %f seconds\n", time_spent);

    free(arr);
    return 0;
}