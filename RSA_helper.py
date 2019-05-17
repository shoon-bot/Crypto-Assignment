from gen_primes import generate_prime_number
from random import randint
from math import gcd
import binascii


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
    e = 65537
    p = q = e+1
    # Check to ensure gcd(e,p-1) = gcd(e,q-1) = 1
    # => gcd(e,(p-1)(q-1)) = gcd(e,phi) = 1
    while p % e == 1:
        p = generate_prime_number(512)
    while q % e == 1:
        q = generate_prime_number(512)

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


def rsa_hex_encryption (plain_text, e, n):                  # text
    hex_data = binascii.hexlify(plain_text.encode())        # hex
    plain_text_int = int(hex_data, 16)                      # int
    if plain_text_int > n:
        return 0
    cipher = fast_exponentiation(plain_text_int, e, n)
    return cipher                                           # int


def rsa_hex_decryption (cipher, d, n):                      # int
    decrypted_text = fast_exponentiation(cipher, d, n)      # int
    hex_data = hex(decrypted_text)[2:]  # removes the 0x    # hex
    try:
        plain_text = binascii.unhexlify(hex_data).decode()
    except:
        print("\nThe Key is incorrect! Unable to decrypt the cipher!")
        return ""
    return plain_text                                       # text

# e,n,d = rsa_key_generation()
# cipher = rsa_text_encryption("Lol lets try it", e, n)
# text = rsa_text_decryption(cipher, d, n)
# print(cipher)
# print(text)

# e, n, d = rsa_key_generation()
# message = "Lets see if this works Lets see if this works Lets see if this works Lets see if this works Lets see if this works Lets see if i"
# cipher = rsa_hex_encryption(message, e, n)
# print("Cipher =", cipher)
# new_message = rsa_hex_decryption(cipher, d, n)
# print("Transmited message =", message)
