#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Função auxiliar para converter um número inteiro para uma string
char* intToString(long num) {
    int length = snprintf(NULL, 0, "%d", num);
    char* str = malloc(length + 1);
    snprintf(str, length + 1, "%d", num);
    return str;
}

// Função para fatoração em forma de multiplicação de primos
char* factors(long n) {
    char* fatores = malloc(1024); // String vazia
    fatores[0] = '\0';

    // Encontra as potencias de 2, se houver
    if(n % 2 == 0) {
    	int k = 0;
    	while (n % 2 == 0) {
        	//strcat(fatores, "2•");
        	k++;
        	n = n / 2;
    	}
    	char* kstring = intToString(k);
    	strcat(fatores, "2("); strcat(fatores, kstring); strcat(fatores, ")•");
    	free(kstring);
    }
    // Encontra os fatores primos ímpares
    for (int i = 3; i * i <= n; i = i + 2) {
        while (n % i == 0) {
            char* fator = intToString(i);
            strcat(fatores, fator);
            strcat(fatores, "•");
            free(fator);
            n = n / i;
        }
    }

    // Se o número restante após a fatoração é maior que 2, ele também é um fator primo
    if (n > 2) {
        char* fator = intToString(n);
        strcat(fatores, fator);
        strcat(fatores, " ");
        free(fator);
    }

    return fatores;
}

long s(long x) {
	long sum = 0L;
	for (long i = 1L; i <= x / 2; i++) {
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

void Iter(long n, int i_lim, bool f) {
	int i = 0; 						// Contador de iterações
	long t_i = n;
	printf("i 		t_i(%ld) 	Fatoração\n", n);
	while (i <= i_lim) {
		printf("%d 		%ld 		", i, t_i);
		if(f == true) { 
			char* fatores = factors(t_i);
			printf("	%s\n", fatores); 
			free(fatores);
		} else {
			printf("\n");
		}
		t_i = t(t_i);		// Executa a função t(n) para o novo valor
		i++;
	}
}

int main() {
	int lim = 125;
	printf("t_0 = ");
	long n; scanf("%ld", &n);
	printf("\n");
	Iter(n, lim, true);
	return 0;
}