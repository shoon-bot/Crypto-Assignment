from RSA_helper import rsa_key_generation
from RSA_helper import rsa_text_encryption
from RSA_helper import rsa_text_decryption
import subprocess as sp
import readchar


def main():
    while True:
        tmp = sp.call('clear', shell=True)
        print("1. Generate Public and Private Keys")
        print("2. Encrypt a message")
        # print("3. Encrypt a message, write to file")
        print("3. Decrypt a message")
        # print("5. Decrypt a message from a file")
        print("0. Exit")
        print("input: ", end='')
        n = int(input())

        if n == 1:
            e, n, d = rsa_key_generation()
            print("\nPublic Key n =\n", n, sep = '')
            print("\nPublic Key e =\n", e, sep = '')
            print("\nPrivate Key d =\n", d, sep = '')
            print("\nSave these values")
            print("DO NOT SHATE THE PRIVATE KEY WITH ANYONE!")
            e = n = d = 0

        elif n == 2:
            message = input("\nEnter the message to encrypt: ")
            e = int(input("\nEnter the public key e: ").strip())
            n = int(input("\nEnter the public key n: ").strip())
            cipher = rsa_text_encryption(message, e, n)
            print("\nThe cipher text to be shared is: ")
            [print(c) for c in cipher]
            print("\nCopy the cipher text above and transmit it to the receiver")
            message = ""
            e = n = 0

        elif n == 3:
            cipher = []
            print("Paste the cipher bellow")
            print("Press enter to denote end of input")
            while True:
                line = input().strip()
                if line:
                    cipher.append(int(line))
                else:
                    break
            n = int(input("\nEnter the public key n: ").strip())
            d = int(input("\nEnter the private Key d: ").strip())
            message = rsa_text_decryption(cipher, d, n)
            print("The decrypted message is: ")
            print(message)
            message = ""
            n = d = 0

        elif n == 0:
            exit()

        else:
            print("Please enter a valid input from 0-3")

        print("\n\nPress enter to continue...")
        readchar.readkey()

if __name__ == '__main__':
    main()
