#include <stdio.h>
#include <math.h>

int s(int x) {
    int sum = 0;
    for (int i = 1; i < x; i++) {
        if (x % i == 0) {
            sum += i;
        }
    }
    return sum;
}

int sigma(int x) {
    int sum = 0;
    for (int i = 1; i <= x; i++) {
        if (x % i == 0) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    int n = 500000;
    double S = 0.0;
    int i;
    for (i = 1; i < n; i++) {
        printf("[%d]\tσ(n)/n = %.2f\t\tS/n = %.10f\tpi ~ %.8f\n", i, (double)sigma(i) / i, S / i, sqrt(6 * S / i));
        S += (double)sigma(i) / i;
    }
    
    return 0;
}

// gcc basel.c -o basel -lm