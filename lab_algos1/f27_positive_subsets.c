#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <time.h>

// 15 20 25

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

int main() {
    int n = 1000;
    int *arr = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000;
    }

    clock_t start = clock();
    long long result = f27_positive_subsets(arr, n);
    clock_t end = clock();

    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Result = %lld\n", result);
    printf("Time = %f seconds\n", time_spent);

    free(arr);
    return 0;
}