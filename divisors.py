def s(x):
	l = []
	for i in range(1, int(x / 2) + 1):
		if x % i == 0:
			l.append(i)
	return sum(l)

def sigma(x):
	return s(x) + x

def t(x):				# H. J. J. te Riele
						# A NOTE ON THE CATALAN-DICKSON CONJECTURE
	return 2*s(x) + x

def iter(n):						# Itera sobre o numero x
	i = 0
	while(n != 0):
		print("[{:d}] : {:d}".format(i, n))
		n = s(n)
		i+=1

def IterList(n):						# Itera sobre o numero x
										# Retorna uma lista com as somas
										# em funcao da iteracao.
	X = []
	Y = []
	i = 0
	while(n != 0):
		print("[{:d}] : {:d}".format(i, n))
		X.append(i)
		Y.append(n)
		n = s(n)
		i+=1
	return X, Y

import matplotlib.pyplot as plt
n = 494
X, Y = IterList(n)
fig = plt.figure()

plt.plot(X, Y)
plt.show()

## Anotacoes ##

# Lehmer Five: 276, 552, 564, 660, e 966.

# Casos interessantes:
# 600: volta em 601
# 1024: volta em 1023
# 800: converge para 1153 em 1 iteracao

#for i in range(1, 100):
#	if iter(i) != 0: print("{:d} -> {:d}".format(i, iter(i)))

# Muitas iteracoes:
# 234
# 7868 (Nao eh monot. cresc.)

# Perfeitos:
# 496