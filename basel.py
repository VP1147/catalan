def s(x):
	s = sum(i for i in range(1, x) if x % i == 0)
	return s

def σ(x):
	σ = sum(i for i in range(1, x+1) if x % i == 0)
	return σ

n = 10000
S = 0

for i in range(1, n):
	S += σ(i)/i
	print("[{:d}]	σ(n)/n = {:.2f}		S/n = {:.10f} pi ~ {:.8f}".format(i, σ(i)/i, S/i, (6*S/i)**(1/2)))
