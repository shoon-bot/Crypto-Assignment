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
a = 2487143
m = 51062111012908
print("Modular multiplicative inverse is", modInverse(a, m)) 

# This code is contributed by Nikita tiwari. 

