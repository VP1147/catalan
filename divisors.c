#include <stdio.h>

long s(long x) {
    long sum = 0;
    for (int i = 1; i <= x / 2; i++) {
        if (x % i == 0) {
            sum += i;
        }
    }
    return sum;
}

long sigma(long x) {
    return s(x) + x;
}

long t(long x) {
    return 2 * s(x) + x;
}

void iter(long n) {
    int i = 0;
    while (n != 0) {
        printf("[%d] : %d\n", i, n);
        n = s(n);
        i++;
    }
}

void IterList(long n, int l) {
    int X[1000];
    int Y[1000];
    int i = 0;
    printf("[%d] : %ld\n", i, n);
    while ((n != 0 && i < l) || (n != 0 && l == 0)) {
        X[i] = i;
        Y[i] = n;
        n = s(n);
        i++;
        printf("[%d] : %ld\n", i, n);
    }
    
    for (int j = 0; j < i; j++) {
        printf("[%d] : %ld\n", X[j], Y[j]);
    }
}

int main() {
    int n = 1488;
    int l = 35;
    IterList(n, l);
    return 0;
}