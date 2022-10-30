from distutils import archive_util
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

cracked_method = ""
cracked = False

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
def dictionary_attack(arguments):
    # Check if the hash has been cracked, if so then return from function
    if (cracked):
        return

    # Open the wordlist file using read permissions and set contents to variable
    dictionary = open(arguments.dictionary, "r")

    testing_string = ""
    # If the user has decided to output all attempts to the cli, then print out attempted string
    if (arguments.output.lower() == "yes"):
        print ("Attemping: ", testing_string)

    dictionary.close() 


# Function to brute force attack the hash
def brute_force_attack(arguments,testing_string_length, testing_string):
    # Check if the hash has been cracked, if so then return from function
    if (cracked):
        return
    
    # If the user has decided to output all attempts to the cli, then print out attempted string
    if (arguments.output.lower() == "yes"):
        print ("Attemping: ", testing_string)

    if (arguments.algorithm.lower() == "all" or arguments.algorithm.lower() == "md5"):
        new_hash = hashlib.md5(testing_string)
        hash_method = "MD5"
    elif (arguments.algorithm.lower() == "all" or arguments.algorithm.lower() == "sha1"):
        new_hash = hashlib.sha1(testing_string)
        hash_method = "SHA1"
    elif (arguments.algorithm.lower() == "all" or arguments.algorithm.lower() == "sha224"):
        new_hash = hashlib.sha224(testing_string)
        hash_method = "SHA224"
    elif (arguments.algorithm.lower() == "all" or arguments.algorithm.lower() == "sha256"):
        new_hash = hashlib.sha256(testing_string)
        hash_method = "SHA256"
    elif (arguments.algorithm.lower() == "all" or arguments.algorithm.lower() == "sha384"):
        new_hash = hashlib.sha384(testing_string)
        hash_method = "SHA384"
    elif (arguments.algorithm.lower() == "all" or arguments.algorithm.lower() == "sha512"):
        new_hash = hashlib.sha512(testing_string)
        hash_method = "SHA512"

    # Check to see if the inputted hash matched the new testing hash.
    # If so set cracked to True, cracked_method to function name and return
    if (new_hash == arguments.hash):
        cracked = True
        cracked_method = "Brute Force"
        return

# Function to use random strings from the dictionary
def random_string_attack():
    print ("Random String Attack")

# Function to validate that a integer falls between two values
def validate_int(min, max, value):
    while (value < min or value > max):
        user_input = input("Invalid entry. Please enter a value between ",min," and ",max,":")
    return user_input

# Function to validate if the wordlist file entered, exists and is the right format
def validate_dictionary(wordlist):
    # Check if the file enetered exists
    if (os.path.exists(wordlist) == False):
        print ("Wordlist file not found. Please enter full path to the chosen wordlist or use the default flag")
        quit()

    # Seperate file name and extension into array
    file_attr = os.path.splitext(wordlist)
    
    # Extract the file extension
    file_extension = file_attr[len(file_attr)]

    # Check the file extension matches what is required, in this case a .txt file
    if (file_extension != ".txt"):
        print ("Invalid dictionary file extension. Please input a dictionary with a .txt extension")
        quit()

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
        print ("Invalid method specified, please enter a valid choice from: dictionary, brute, random or all")
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
        print ("Invalid hashing method, please enter a valid choice from: MD5, SHA1, SHA224, SHA256, SHA384, SHA512 or All")
        quit()
    if (arguments.output.lower() != "yes" or arguments.output.lower() != "no"):
        print ("Invalid output choice specified, default of No has been chosen")
        arguments.output = "no"
    # Call the dictionary validation function
    validate_dictionary(arguments.dictionary)

if __name__ == "__main__":
    # Initialise parser
    parser = argparse.ArgumentParser()
    
    # Adding arguments
    parser.add_argument("-i", "--hash", required=True, help = "Inputted Hash")
    parser.add_argument("-m", "--method", default = "All", help = "Selected Attack Method (Default: All)")
    parser.add_argument("-d", "--dictionary", default = "Wordlist.txt", help = "Defined Word Dictionary (Default: Wordlist.txt)")
    parser.add_argument("-t", "--threads", default = "1", help = "Specified Number of Threads (Default: 2)")
    parser.add_argument("-a", "--algorithm", default = "All", help = "Selected Hashing Algorithm (Default: All)")
    parser.add_argument("-o", "--output", default = "N", help = "Select to display all attempted passwords to cli or not (Default: No)")
    
    # Read arguments from command line
    args = parser.parse_args()

    # Call main function
    main()