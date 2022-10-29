import hashlib
import threading
import string
import time
import argparse
import sys
import os
import pyfiglet
import psutil

CapitaLetters = {
	'A', 'B', 'C', 'D', 'E', 'F', 'G',
	'H', 'I', 'J', 'K', 'L', 'M', 'N',
	'O', 'P', 'Q', 'R', 'S', 'T', 'U',
	'V', 'W', 'X', 'Y', 'Z'}

LowerCaseLetters = {
	'a', 'b', 'c', 'd', 'e', 'f', 'g',
	'h', 'i', 'j', 'k', 'l', 'm', 'n',
	'o', 'p', 'q', 'r', 's', 't', 'u',
	'v', 'w', 'x', 'y', 'z'}

Symbols = {
	'!','£','$','%','^','&','*','(',')'
	,'@','~','#','|','?','¬','`','{',
	'}','[',']',';',':'}

Numbers = {
	'1','2','3','4','5','6','7','8','9','0'}

def main():
    # Parse arguments
    arguments = parser.parse_args()
    print (arguments.dictionary)

    # Call function to display banner
    display_banner()

    # printing the equivalent hex value.
    # userInput = "Hello World"
    # result = hashlib.md5(userInput.encode())
    # print("The byte equivalent of hash is : ", end ="")
    # print(result.hexdigest())

def dictionary_attack():
    print ("Dictionary Attack")

def brute_force_attack():
    print ("Brute Force Attack")

def random_string_attack():
    print ("Random String Attack")

def validate_int():
    print ("Validate Integer")

def validate_file_format():
    print ("Validate File Format")

def display_banner():
    # Initialise pyfiglet
    ascii_banner = pyfiglet.figlet_format("PassCracker")
    # Print out name banner and supported hashes and attacks
    print (ascii_banner)
    print ("This program was developed to crack a given hash using a variety of different methods.")
    print ("Supported hashes: MD5, SHA1, SHA224, SHA256, SHA384, SHA512")
    print ("Supported attack methods: Dictionary, Random String, Brute Force")

def validate_arguments():
    hashing_methods = {"md5", "sha1", "sha224", "sha256", "sha384", "sha512", "all"}
    hashing_algorithm_found = False
    arguments = parser.parse_args()

    print (arguments.method.lower())
    print (arguments.threads.isnumeric())

    if (str(arguments.method.lower()) != "dictionary" or str(arguments.method.lower()) != "brute" or str(arguments.method.lower()) != "random" or str(arguments.method.lower()) != str("all")):
        print ("Invalid method specified, please enter a valid choice from: dictionary, brute, random, all")
    if (arguments.threads.isnumeric() != False or arguments.threads < 1 or arguments.threads > psutil.cpu_count(logical=False)):
        print ("Please enter a valid number of threads, the maximum for your system is: ", psutil.cpu_count(logical=False))
    for x in hashing_methods:
        if (arguments.algorithm.lower() == x):
            hashing_algorithm_found = True
    if (hashing_algorithm_found == False):
        print ("Invalid hashing method, please enter a valid choice from: MD5, SHA1, SHA224, SHA256, SHA384, SHA512, All")



if __name__ == "__main__":
    # Initialise parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-i", "--hash", required=True, help = "Inputted Hash")
    parser.add_argument("-m", "--method", default = "All", help = "Selected Attack Method")
    parser.add_argument("-d", "--dictionary", default = "Wordlist.txt", help = "Defined Word Dictionary")
    parser.add_argument("-t", "--threads", default = "1", help = "Specified Number of Threads (Minimum 1)")
    parser.add_argument("-a", "--algorithm", default = "All", help = "Selected Hashing Algorithm")
    
    # Read arguments from command line
    args = parser.parse_args()

    # Validate arguments
    validate_arguments()

    # Call main function
    main()