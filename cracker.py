import hashlib
import threading
import string
import time
import argparse
import sys
import os
import pyfiglet

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
    arguments = parser.parse_args()
    print (arguments.dictionary)
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
    ascii_banner = pyfiglet.figlet_format("PassCracker")
    print(ascii_banner)


if __name__ == "__main__":
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-i", "--hash", required=True, help = "Inputted Hash")
    parser.add_argument("-m", "--method", default = "All", help = "Selected Attack Method")
    parser.add_argument("-d", "--dictionary", default = "Wordlist.txt", help = "Defined Word Dictionary")
    parser.add_argument("-t", "--threads", default = "1", help = "Specified Number of Threads (Minimum 1)")
    parser.add_argument("-a", "--algorithm", default = "All", help = "Selected Hashing Algorithm")
    
    # Read arguments from command line
    args = parser.parse_args()
    
    if len(sys.argv) > 1:
        main()
    else:
        parser.print_help()
