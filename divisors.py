# Algorítmos, funções e notas acerca da pesquisa sobre 
# a conjectura de Catalan-Dickson.

# Aluno:		Vinícius A. Pavão - Instituto de Física - UFMS
# Orientador: 	Elias T. Galante - Instituto de Matemática - UFMS

# Código mantido sob licença GNU GPLv3 - ver LICENSE
# Junho de 2023

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

def IterList(n, l):						# Itera sobre o numero x
										# Retorna uma lista com as somas
										# em funcao da iteracao.
	X = []
	Y = []
	i = 0
	lim = l								# lim = 0 : Itera sem limites
	print("[{:d}] : {:d}".format(i, n))
	while(n != 0 and i < lim or n != 0 and lim == 0):
		X.append(i)
		Y.append(n)
		n = s(n)
		i+=1
		print("[{:d}] : {:d}".format(i, n))
	return X, Y

import matplotlib.pyplot as plt
n = 1488
l = 35
X, Y = IterList(n, l)
fig, ax = plt.subplots()

ax.plot(X, Y)
ax.set_title("$s^i(n)$, n = {:d}".format(n), fontsize=14)
ax.set_xlabel("i", fontsize=12)
ax.set_ylabel("$s^i(n)$", fontsize=12)

plt.show()

## Anotacoes ##

# Lehmer Five: 276, 552, 564, 660, e 966.

# Casos interessantes:
# 600: volta em 601
# 1024: volta em 1023
# 800: converge para 1153 em 1 iteracao
# 2976: Descesce e depois aumenta "exponencialmente"

#for i in range(1, 100):
#	if iter(i) != 0: print("{:d} -> {:d}".format(i, iter(i)))

# Muitas iteracoes:
# 234
# 7868 (Nao eh monot. cresc.)

# Perfeitos:
# 496