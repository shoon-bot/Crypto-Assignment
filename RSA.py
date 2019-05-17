from RSA_helper import rsa_key_generation
from RSA_helper import rsa_text_encryption
from RSA_helper import rsa_text_decryption
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
        n = int(input("input: "))

        if n == 1:
            e, n, d = rsa_key_generation()
            print("\nPublic Key e =\n", e, sep = '')
            print("\nPublic Key n =\n", n, sep = '')
            print("\nPrivate Key d =\n", d, sep = '')
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
            E = int(input("\nEnter the Public Key E to store in memory: ").strip())
            N = int(input("\nEnter the Public Key N to store in memory: ").strip())
            print("\nValues Successfully Stored")
            public_set = True

        elif n == 3:
            D = int(input("\nEnter the Private Key D to store in memory: ").strip())
            if public_set:
                c = input("\nDo you want to keep the current value of N stored in memory? [Y/n]: ")
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
                cipher = rsa_text_encryption(message, E, N)
            else:
                e = int(input("\nEnter the Public Key e: ").strip())
                n = int(input("\nEnter the Public Key n: ").strip())
                cipher = rsa_text_encryption(message, e, n)
            print("\nThe cipher text to be shared is: \n")
            [print(ci) for ci in cipher]
            print("\nCopy the cipher text above and transmit it to the receiver")
            c = input("\nDo you want to store the cipher text to a file? [Y/n]: ")
            if c in 'Yy':
                file = open("cipher text.txt", "w")
                [file.write(str(ci) + "\n") for ci in cipher]
                # file.writelines(cipher)
                # cipher_string = []
                # [cipher_string.append(str(cip) + "\n") for cip in cipher]
                # file.writelines(cipher_string)
                file.close()
                file = None
            message = ""
            e = n = 0

        elif n == 5:
            cipher = []
            exists = os.path.isfile('cipher text.txt')
            if exists:
                c = input("\nDo you want to read the cipher text from the file? [Y/n]: ")
                if c in 'Yy':
                    file = open("cipher text.txt", "r")
                    cipher_str = file.readlines()
                    [cipher.append(int(ci)) for ci in cipher_str]
                else:
                    print("\nPaste the cipher bellow")
                    print("Press enter to denote end of input:")
                    while True:
                        line = input().strip()
                        if line:
                            cipher.append(int(line))
                        else:
                            break
            else:
                print("Paste the cipher bellow")
                print("Press enter to denote end of input")
                while True:
                    line = input().strip()
                    if line:
                        cipher.append(int(line))
                    else:
                        break
            if private_set:
                message = rsa_text_decryption(cipher, D, N)
            elif public_set:
                c = input("Do you want to use the same value of N stored in memory? [Y/n]: ")
                if c in "Yy":
                    print("Using value N =", N)
                    n = N
                else:
                    n = int(input("\nEnter the Public Key n: ").strip())
                d = int(input("\nEnter the Private Key d: ").strip())
                message = rsa_text_decryption(cipher, d, n)
            print("\nThe decrypted message is: ")
            print('"', message, '"', sep='')
            message = ""
            n = d = 0

        elif n == 0:
            exit()

        else:
            print("Please enter a valid input from 0-3")

        print("\nPress enter to continue...")
        readchar.readkey()

if __name__ == '__main__':
    main()
