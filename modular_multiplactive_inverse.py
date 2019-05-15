# Algorithm taken from https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/

# Iterative Python 3 program to find 
# modular inverse using extended 
# Euclid algorithm 

# Returns modulo inverse of a with 
# respect to m using extended Euclid 
# Algorithm Assumption: a and m are 
# coprimes, i.e., gcd(a, m) = 1 
def modInverse(a, m) : 
	m0 = m 
	y = 0
	x = 1

	if (m == 1) : 
		return 0

	while (a > 1) : 

		# q is quotient 
		q = a // m 

		t = m 

		# m is remainder now, process 
		# same as Euclid's algo 
		m = a % m 
		a = t 
		t = y 

		# Update x and y 
		y = x - q * y 
		x = t 
		print(a)


	# Make x positive 
	if (x < 0) : 
		x = x + m0 

	return x 


# Driver program to test above function 
a = 6513516734600035718300327211250928237178281758494417357560086828416863929270451437126021949850746381
m = 19087749306171863871810380694827510321936151288556290924968414152545680422633269156988748885053343369109762064796332040185843368964059881088983759307883543865253825485236512359091007027230689880454608003293901812276867252993356685756187955551449885952932415558083504175466131628326975142351635126217482094609055481665080
print("Modular multiplicative inverse is", modInverse(a, m)) 

# This code is contributed by Nikita tiwari. 

