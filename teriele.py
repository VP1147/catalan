# Algorítmos, funções e notas acerca da pesquisa sobre 
# a conjectura de Catalan-Dickson. Especificamente acerca
# da publicação:
# A Note on the Catala-Dickson Conjecture - H. J. J. te Riele.
# Mathematics of Computation, Volume 27, Number 121, January 1973.

# Aluno:		Vinícius A. Pavão - Instituto de Física - UFMS
# Orientador: 	Elias T. Galante - Instituto de Matemática - UFMS

# Código mantido sob licença GNU GPLv3 - ver LICENSE
# Julho de 2023

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

def Iter(n, i_lim):
	i = 0
	t_i = n
	print("i 	t_i({:d})".format(n))
	while(i <= i_lim):
		print("{:d} 		{:d}".format(i, t_i))
		t_i = t(t_i)
		i += 1

Iter(1488, 35)