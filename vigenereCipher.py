#!bin/
# Juan Carlos Ramirez
# Vigenere Cipher, can encrypt and decrypt
import argparse, sys

parser = argparse.ArgumentParser(description="Encrypts and Decrypt messages based on a keyword")
parser.add_argument("-D", default="", help="Data to encrypt or decrypt")
parser.add_argument("-k", default="", help="En/Decryption Key")
parser.add_argument("-d", action="store_true", help="Decrypt")
parser.add_argument("-e", action="store_true", help="Encrypt")

args = parser.parse_args()

if ((args.d != True and args.e != True) and (args.d == True and args.e == True)):
    sys.exit(parser.print_help())

if (args.D == ""):
    dataFile = raw_input("Please enter the File Name: ")
else:
    dataFile = args.D

open_file = open(dataFile)
open_file.seek(0)
data = open_file.read()

if (args.k == ""):
    key = raw_input("Please enter the Encryption Key: ")
else:
    key = args.k

# Create the Vigenere Square
vSquare = []

for i in range(0, 26):
    vSquare.append([])
    for x in range(0, 26):
        # print "I: ", i, " X: ", x, "VALUE: ", chr(ord('A') + ((i + x) % 26))
        vSquare[i].append(chr(ord('A') + ((i + x) % 26)))
        # sys.stdout.write(vSquare[i][x])
        # sys.stdout.flush()
        # print ""

if (args.d):
    # Decrypt using key
    x = 0
    for i in range(0, data.__len__()):
        if (data[i] != " "):
            sys.stdout.write(vSquare[0][(ord("A") - ord(key[x])) + (ord(data[i]) - ord("A"))])
            sys.stdout.flush()
            x = (x + 1) % key.__len__()
        else:
            sys.stdout.write(" ")
            sys.stdout.flush()


else:
    # Encrypt Using key
    encryptedData = open("encryptedMessage.txt", 'w+')
    x = 0
    for i in range(0, data.__len__() - 1):
        if (data[i] != " "):
            encryptedData.write(vSquare[ord(key[x]) - ord("A")][ord(data[i]) - ord("A")])
            sys.stdout.write(vSquare[ord(key[x]) - ord("A")][ord(data[i]) - ord("A")])
            sys.stdout.flush()
            x = (x + 1) % key.__len__()
        else:
            encryptedData.write(" ")
            sys.stdout.write(" ")
            sys.stdout.flush()

print ""
