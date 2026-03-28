#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <time.h>

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

int main() {
    int n = 100000;
    int *arr = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000;
    }

    clock_t start = clock();
    long long result = f17_count_inversions(arr, n);
    clock_t end = clock();

    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Result = %lld\n", result);
    printf("Time = %f seconds\n", time_spent);

    free(arr);
    return 0;
}