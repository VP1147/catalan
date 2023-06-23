import math as m

def s(x):
	s = sum(i for i in range(1, x) if x % i == 0)
	return s

def σ(x):
	σ = sum(i for i in range(1, x+1) if x % i == 0)
	return σ

def basel(n):
	S = 0
	for i in range(1, n+1):
		S += σ(i)/i
	print("[{:d}]	σ(n)/n = {:.2f}		S/n = {:.16f}	S > {:d}".format(i, σ(i)/i, S/i, int(S)))
	print("--- Final ---")

def basel_simulation(n):
	basel = m.pi**2 / 6
	print("basel = {:.10f}".format(basel))
	print("S ~ {:d}".format(int(basel * n)))

n = 10000

basel(n)

basel_simulation(n)

# Imprimindo números 	: 0m15,675s
# Sem imprimir 			: 0m3,487s