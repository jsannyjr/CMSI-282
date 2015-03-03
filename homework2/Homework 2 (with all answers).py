#Justin Sanny
#CMSI 282
#3/3/2015


#Homework #2

1. 
#a. f = Θ(g) b. f = O(g) c. f = Θ(g) d. f = Θ(g) e. f = Θ(g)
#f. f = Θ(g) g. f = Ω(g) h. f = Ω(g) i. f = Ω(g) j. f = Ω(g)
#k. f = Ω(g)  l. f = O(g) m. f = O(g) n. f = Θ(g)  o. f = Ω(g)
#p. f = O(g) q. f = Θ(g)

2. #a) Picture couldn't be shown in sublime but it is on the hardcopy.






  #b) Using X^8, we can express this as  X^8 = X * X * X * X * X * X * X * X
#By simplifying X*X to X^2, we then have  X^8 = X^2 * X^2 *X^2 *X^2
#Then we can do it again for X^2 * X^2 so that  X^8 = X^4 * X^4  which takes log 8 amount of work.
#The same could be said about X^n which can be simplified as above. 
#Therefore, O(log n) matrix multiplications suffice for computing X^n.

3. 
#a) log(10) / log(2) = N. Ceiling(N) = Ceiling(3.32)  N = 4
#b) Length of binary integer is floor(log base 2 x) + 1
#Length of decimal integer is ceiling(log base 10 x)
#floor(log base 2 x) + 1 <= 4 * ceiling(log base 10 x)
#floor(log base 2 x) + 1 < log base 2 x + 1
#log base 2 x < log base 2 x + 1
#4 * ceiling(log base 10 x) > 4 * log base 10 x
#log base 2 x <= 4 * log base 10 x
#log base 10 x = log base 2 x / log base 2 10
#log base 2 x * log base 2 10 <= 4

4. 
#Ignoring log since both sides contain it, n! < or equal to n^n because n * n – 1 * n -2… * 1 < n *n *n… *n by definition.
#n! > or equal to (n/2) ^ n/2 because n * n – 1 * n – 2 … * 1 > or equal to n / 2 * n / 2 * … n / 2 since (n / 2) ^ (n /2) has only half the numbers of n. 
#Therefore log(n!) = Θ(n log n).

5. 
#4^1536 (mod 35) = 1
#9^4825 (mod 35) = 1
#1 - 1 (mod 35) = 0
#Yes it is divisible by 35.

6.
#By Fermat’s little theorem, p = 31 is prime
#5^30 = 1 (mod 31)
#6^30 = 1 (mod 31)
#Now, 5^30000 = 5 ^ rem(30000,30) (mod 31) = 1
#6^123456 = 6^6 * 6^123450 = 6^6 * 6^rem(123450,30) (mod 31) = 6^6 (mod 31) = 1
#5^30000 – 6^123456 = (1-1) (mod 31) = 0.
#The difference is a multiple of 31.

7.
#An addition chain is better when b = 15.
#a^{15} = x \times (x \times [x \times x^2]^2)^2  \! (squaring, 6 multiplies)
#a^{15} = x^3 \times ([x^3]^2)^2  \! (optimal addition chain, 5 multiplies if x3 is re-used)
#http://en.wikipedia.org/wiki/Exponentiation_by_squaring#Computational_complexity

8. 
#By Fermat’s Little Theorem, 2^126 ≡ 1 mod 127  2^126 = 2^125 * 2. So 2^125 is the inverse of 2 mod 127. 2 * 64 = 128 ≡ 1mod 127, 
#so 2^125 ≡ 64 mod 127 since the inverse is unique.

9. 
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
10. (d) 
#(N − 1)! ≡ −1 (mod N)
#It is simple to check if a number is prime with the test but trying to prove that -1 mod n becomes overly complicated and 
#unreliable since it can lead to different conclusions.
11. 
def compute(a, b, c, p): #a^b^c mod p, p is prime
	x = b ^ c
	a = a^x 
	return a % p

#The algorithm takes O(n^3). 
#By first computing (b mod(p – 1)) in time O(log b log p) then computing (b^c mod (p – 1)) which consists of O(log c) multiplications of numbers of size at most p. 
#Each multciplication will take a total of O(log c log^2 p ) time. Then (a mod p) takes O(log a log p). Note if (b^c mod (p – 1)) < p. 
#Compute a^b^c mod p using repeated squaring in O(log^3 p). So the total running time is O(log b log p + log c log^2p + log a log p + log ^3 p). 
#This is upper bounded by O(n^3) where n is the size of the input. 
#http://courses.csail.mit.edu/6.046/fall03/handouts/pset8-sol.pdf
