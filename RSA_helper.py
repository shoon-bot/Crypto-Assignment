from gen_primes import generate_prime_number
from random import randint
from math import gcd


def mod_inverse(e, m) :
    n = m
    x = 0
    d = 1

    while (e > 1) :
        q=e//m

        temp=m
        m=e%m
        e=temp

        temp=x
        x=d-q*x
        d=temp

    if (d < 0) :
        d = d + n
    return d


def fast_exponentiation(base, power, mod):
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % mod
        power = power // 2
        base = (base * base) % mod
    return result


def rsa_key_generation():
    """ Generate Public and Private keys for RSA RSA_Encryption
        Returns e, n, d
    """
    p = generate_prime_number(randint(512,544))
    q = generate_prime_number(randint(512,544))
    e = generate_prime_number(randint(1024,1088))

    n = p * q
    phi = (p-1) * (q-1)

    while True:
        if gcd(e, phi) == 1:
            break
        else:
            e = generate_prime_number(randint(1024,1088))

    d = mod_inverse(e, phi)
    p = q = phi = 0
    return e, n, d


def rsa_text_encryption (plain_text, e, n):
    """ Given a string and public keys, encrypt using RSA Encryption
        Args:
            plain_text - string
            e - public key
            n - public key
        return a list of encrypted characters of the cipher text to be transmited
    """
    cipher_list = []
    for p in plain_text:
        cipher_list.append(fast_exponentiation (ord(p), e, n))
    return cipher_list


def rsa_text_decryption (cipher_list, d, n):
    """ Given a cipher text and private key, decrypt using RSA Decryption
        Args:
            cipher_list - list of
            d - private key
            n - public key
        return the original plain text message
    """
    plain_text = ""
    for c in cipher_list:
        plain_text += chr(fast_exponentiation (c, d, n))
    return plain_text

# e,n,d = rsa_key_generation()
# cipher = rsa_text_encryption("Lol lets try it", e, n)
# text = rsa_text_decryption(cipher, d, n)
# print(cipher)
# print(text)
