from gen_primes import generate_prime_number
from random import randint


def modInverse(e, m) :
	n = m
	x = 0
	d = 1

	while (a > 1) :
		q=a//m

        temp=m
		m=a%m
		a=temp

		temp=x
		x=d-q*x
		d=temp

    if (d < 0) :
		d = d + n
	return d


def rsa_key_generation():
    """ Generate Public and Private keys for RSA RSA_Encryption
        return e, n, d
    """
    p = generate_prime_number(randint(512,544))
    q = generate_prime_number(randint(512,544))
    e = generate_prime_number(randint(512,544))

    n = p * q
    phi = (p-1) * (q-1)
    d = modInverse(e, phi)
    p = q = phi = 0
    return e, n, d
