def s(x):
	l = []
	for i in range(1, int(x / 2) + 1):
		if x % i == 0:
			l.append(i)
	return sum(l)

def iter(x):
	i=1
	xi = x
	print("--> n = {:d}".format(x))
	while(x != 0):
		x = s(x)
		print("[{:d}] : {:d}".format(i, x))
		if x == s(x):
			return x
		i+=1
	return xi

# 276, 552, 564, 660, and 966.
#alg(8400)
#alg(552, 100)
#alg(564, 100)
#alg(660, 100)
#alg(966, 100)

# Caso interessante: volta em 601
#s(600)

# Caso interessante: Numero sociavel
#alg(12496)
#dk(576)

#for i in range(1, 100):
#	if iter(i) != 0: print("{:d} -> {:d}".format(i, iter(i)))

iter(95)
iter(27)