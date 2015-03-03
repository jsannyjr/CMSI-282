
def lcm(p, q): #takes in two n-bit numbers and returns the least common denominator.
	x = abs(int(p, 2))
	y = abs(int(q, 2))
	m = x * y
	if not m: return 0
	while True:
		x %= y
		if not x: return m 
		x %= y
		if not y: return m

def compute(a, b, c, p): #a^b^c mod p, p is prime
	x = b ^ c
	a = a^x 
	return a % p

