import hashlib
import threading
import string
import time
import argparse
import sys
  
def main():
    
    arguments = parser.parse_args()
    print (arguments.dictionary)
    
    # printing the equivalent hex value.
    # userInput = "Hello World"
    # result = hashlib.md5(userInput.encode())
    # print("The byte equivalent of hash is : ", end ="")
    # print(result.hexdigest())

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
