#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <time.h>

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

void f14_merge_sort(int *a, int n)
{
    int *buf = (int *)malloc((size_t)n * sizeof(int));
    ms_rec(a, buf, 0, n - 1);
    free(buf);
}

int main() {
    int n = 100000;
    int *arr = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000;
    }

    clock_t start = clock();
    f14_merge_sort(arr, n);
    clock_t end = clock();

    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

    //printf("Result = %lld\n", result);
    printf("Time = %f seconds\n", time_spent);

    free(arr);
    return 0;
}