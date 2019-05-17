from RSA_helper import rsa_key_generation
from RSA_helper import rsa_hex_encryption
from RSA_helper import rsa_hex_decryption
import subprocess as sp
import readchar
import os
E = N = D = 0


def main():
    public_set = private_set = False
    while True:
        tmp = sp.call('clear', shell=True)
        print("1. Generate Public and Private Keys")
        print("2. Store a Public Key")
        print("3. Store a Private Key")
        print("4. Encrypt a message")
        print("5. Decrypt a message")
        print("0. Exit")
        try:
            n = int(input("input: "))
        except:
            print("\nPlease enter a valid input...")
            readchar.readkey()
            continue

        if n == 1:
            e, n, d = rsa_key_generation()
            print("\nExponent Public Key, E =", e)
            print("\nModulus Public Key, N =\n", n, sep = '')
            print("\nPrivate Key D =\n", d, sep = '')
            print("\nCopy these values")
            print("DO NOT SHATE THE PRIVATE KEY WITH ANYONE!")

            c = input("\nDo you want to save these values in memory? [Y/n]: ")
            if c in "Yy":
                print("Saving Values...")
                E = e
                N = n
                D = d
                public_set = private_set = True
            else:
                print("Discarding Values...")
            e = n = d = 0

        elif n == 2:
            E = int(input("\nEnter the Public Key Exponent 'E' to store in memory: ").strip())
            N = int(input("\nEnter the Public Key Modulus 'N' to store in memory: ").strip())
            print("\nValues Successfully Stored")
            public_set = True

        elif n == 3:
            D = int(input("\nEnter the Private Key 'D' to store in memory: ").strip())
            if public_set:
                c = input("\nDo you want to use the current value of N stored in memory? [Y/n]: ")
                if c in "Yy":
                    print("Keeping value N =", N)
                else:
                    N = int(input("\nEnter the Public Key N to store in memory: ").strip())
            else:
                N = int(input("\nEnter the Public Key N to store in memory: ").strip())
            print("Values Successfully Stored")
            private_set = True

        elif n == 4:
            message = input("\nEnter the message to encrypt: ")
            if public_set:
                cipher = rsa_hex_encryption(message, E, N)
            else:
                e = int(input("\nEnter the Public Key e: ").strip())
                n = int(input("\nEnter the Public Key n: ").strip())
                cipher = rsa_hex_encryption(message, e, n)
            if cipher == 0:
                print("The Text entered is too large to be encrypted.")
                print("Please Try again with smaller text")
                continue
            print("\nThe cipher text to be shared is: ")
            print(cipher)
            print("\nCopy the cipher text above and transmit it to the receiver")
            c = input("\nDo you want to store the cipher text in a file? [Y/n]: ")
            if c in 'Yy':
                file = open("cipher_text.txt", "w")
                file.write(str(cipher))
                file.close()
                file = None
                print("The cipher was stored in the file cipher_text.txt")
            message = ""
            e = n = 0

        elif n == 5:
            exists = os.path.isfile('cipher_text.txt')
            if exists:
                c = input("\nDo you want to read the cipher text from the file 'cipher_text.txt'? [Y/n]: ")
                if c in 'Yy':
                    file = open("cipher_text.txt", "r")
                    cipher = int(file.read())
                else:
                    print("\nPaste the cipher bellow:")
                    cipher = int(input().strip())
            else:
                print("\nPaste the cipher bellow:")
                cipher = int(input().strip())

            if private_set:
                message = rsa_hex_decryption(cipher, D, N)
            elif public_set:
                c = input("Do you want to use the same value of N stored in memory? [Y/n]: ")
                if c in "Yy":
                    print("Using value N =", N)
                    n = N
                else:
                    n = int(input("\nEnter the Public Key Moculus 'N': ").strip())
                d = int(input("\nEnter the Private Key 'D': ").strip())
                message = rsa_hex_decryption(cipher, d, n)
            else:
                n = int(input("\nEnter the Public Key Moculus 'N': ").strip())
                d = int(input("\nEnter the Private Key 'D': ").strip())
                message = rsa_hex_decryption(cipher, d, n)

            print("\nThe decrypted message is: ")
            print('"', message, '"', sep='')
            message = ""
            n = d = 0

        elif n == 0:
            exit()

        else:
            print("Please enter a valid input from 0-3")

        print("\nPress any key to continue...")
        readchar.readkey()

if __name__ == '__main__':
    main()
