import hashlib
import threading
import string
import time
import argparse
import sys
import os
import pyfiglet
import psutil

capital_letters = {
	'A', 'B', 'C', 'D', 'E', 'F', 'G',
	'H', 'I', 'J', 'K', 'L', 'M', 'N',
	'O', 'P', 'Q', 'R', 'S', 'T', 'U',
	'V', 'W', 'X', 'Y', 'Z'}

lower_case_letters = {
	'a', 'b', 'c', 'd', 'e', 'f', 'g',
	'h', 'i', 'j', 'k', 'l', 'm', 'n',
	'o', 'p', 'q', 'r', 's', 't', 'u',
	'v', 'w', 'x', 'y', 'z'}

symbols = {
	'!','£','$','%','^','&','*','(',')'
	,'@','~','#','|','?','¬','`','{',
	'}','[',']',';',':','-','_','=','+'}

numbers = {
	'1','2','3','4','5','6','7','8','9','0'}

def main():
    # Parse arguments
    arguments = parser.parse_args()
    
    # Call function to display banner
    display_banner()

    # Call function to validate arguments passed in
    validate_arguments

    # printing the equivalent hex value.
    # userInput = "Hello World"
    # result = hashlib.md5(userInput.encode())
    # print("The byte equivalent of hash is : ", end ="")
    # print(result.hexdigest())

# Function to use the inputted dictionary to attempt the crack the hash
def dictionary_attack():
    print ("Dictionary Attack")

# Function to brute force attack the hash
def brute_force_attack():
    print ("Brute Force Attack")

# Function to use random strings from the dictionary
def random_string_attack():
    print ("Random String Attack")

# Function to validate that a integer falls between two values
def validate_int(min, max):
    print ("Validate Integer")

# Function to validate the wordlist file entered 
def validate_file_format():
    print ("Validate File Format")

# Function to display the banner at the top of the cli when first launched
def display_banner():
    # Initialise pyfiglet
    ascii_banner = pyfiglet.figlet_format("PassCracker")
    # Print out name banner and supported hashes and attacks
    print (ascii_banner)
    print ("This program was developed to crack a given hash using a variety of different methods.")
    print ("Supported hashes: MD5, SHA1, SHA224, SHA256, SHA384, SHA512")
    print ("Supported attack methods: Dictionary, Random String, Brute Force")

# Function to validate that the arguments passed into the program fall within the required specification
def validate_arguments():
    # Initialise array for supported hashing methods, boolean for if the hashing method is supported
    hashing_methods = {"md5", "sha1", "sha224", "sha256", "sha384", "sha512", "all"}
    hashing_algorithm_found = False

    # Parsing arguments for validation
    arguments = parser.parse_args()

    # Check to ensure that the inputted attack method matches one of the supported methods, if not send error message and quit the program
    if (str(arguments.method.lower()) != "dictionary" or str(arguments.method.lower()) != "brute" or str(arguments.method.lower()) != "random" or str(arguments.method.lower()) != str("all")):
        print ("Invalid method specified, please enter a valid choice from: dictionary, brute, random, all")
        quit()
    # Check to ensure that the inputted number of threads is within the number of threads available for the system running the program, if not send error message and quit the program
    if (arguments.threads.isnumeric() == False or int(arguments.threads) < 1 or int(arguments.threads) > psutil.cpu_count(logical=False)):
        print ("Please enter a valid number of threads, the maximum for your system is: ", psutil.cpu_count(logical=False))
        quit()
    # Check to ensure that the inputted hashing algorithm matches one of the supported algorithms, if not send error message and quit the program
    for x in hashing_methods:
        if (arguments.algorithm.lower() == x):
            hashing_algorithm_found = True
    if (hashing_algorithm_found == False):
        print ("Invalid hashing method, please enter a valid choice from: MD5, SHA1, SHA224, SHA256, SHA384, SHA512, All")
        quit()
    # Check to ensure that the inputted dictionary file exists, if not send error message and quit the program
    if (os.path.exists(arguments.dictionary) == False):
        print ("Wordlist file not found. Please enter full path to the chosen wordlist or use the default flag")
        quit()

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

    # Call main function
    main()