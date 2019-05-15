# using the numbers 5837687 and 8746979 as the primes
# p = 5837687
# q = 8746979
# n = p x q = 51062125597573
# Φ(n) = (p-1)*(q-1) = 51062111012908
# e = 2487143
# d = 19462106925191
# public key = (e,n)
# private key = d

n = 51062125597573
e = 2487143
d = 19462106925191


def Fast_Exponentiation(base, power, mod):
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % mod
        
        power = power // 2
        base = (base * base) % mod
    return result


def RSA_Encryption (P, e, n):
    C = Fast_Exponentiation (P, e, n)
    return C


def RSA_Decryption (C, d, n):
    P = Fast_Exponentiation(C, d, n)
    return P

if __name__ == '__main__':
    plain_text = [1,1,3,5,8,13,21,33,54]
    cypher_text = []
    decrypted_message = []
    for p in plain_text:
        cypher_text.append(RSA_Encryption(p, e, n))
    for c in cypher_text:
        decrypted_message.append(RSA_Decryption(c, d, n))
    print("Plain text is: ", plain_text)
    print("Cypher text is: ", cypher_text)
    print("Decrypted text is: ", decrypted_message)

