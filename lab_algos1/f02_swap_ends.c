#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <time.h>

void f02_swap_ends(int *a, int n)
{
    if (n < 2) return;
    int t    = a[0];
    a[0]     = a[n - 1];
    a[n - 1] = t;
}

int main() {
    int n = 100000;
    int *arr = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000;
    }

    clock_t start = clock();
    f02_swap_ends(arr, n);
    clock_t end = clock();

    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

    //printf("Result = %lld\n", result);
    printf("Time = %f seconds\n", time_spent);

    free(arr);
    return 0;
}