# assignment: programming assignment 4
# author: Diwa Ashwini Vittala
# date: 11-28-2020
# file: cipher.py is a program that encodes or decodes a message using cesar's cipher.
# input: The user chooses to encode, decode, or quit program, then selects the files.
# output: According to the user's choice, the message is encoded or decoded.

#definitions
#asks for and reads the file
def readfile():
    message = []
    filename= input("Please enter a file for reading: \n")
    file1 = open(filename, "r") #ENTER THE FILENAME!
    try:
        for line in file1.readlines():
            message.append(line)
        file1.close()
    except IOError:
        print("File cannot be opened")
        file1.close()
    else:
        file1.close()
    return message
#writes the message into the second file
def writefile(message):
    try:
        filename= input("Please enter a file for writing: \n")
        file1 = open(filename, "w")
        file1.write(message)
        file1.close()
    except IOError:
        print("File cannot be opened")
        file1.close()
    else:
        file1.close()
    return file1
# make a list (tuple) of letters in the English alphabet
def make_alphabet():
   alphabet = ()
   for i in range(26):
       char = i + 65
       alphabet += (chr(char),)
   return alphabet
# encode text letter by letter using a Caesar cipher
# return a list of encoded symbols
def encode(plaintext):
   shift = 3
   ciphertext = []
   alphabet = make_alphabet()
   length = len(alphabet)
   for char in plaintext:
       found = False
       for i in range(length):
           if char == alphabet[i]:
               letter = alphabet[(i + shift) % length]
               ciphertext.append(letter)
               found = True
               break
       if not found:
           ciphertext.append(char)
   return ciphertext
# decode text letter by letter using a Caesar cipher
# return a list of decoded symbols
# check how the function encode() is implemented
# your implementation of the function decode() can be very similar
# to the implementation of the function encode()
def decode(text):
   shift = -3
   plaintext = []
   alphabet = make_alphabet()
   length = len(alphabet)
   for char in text:
       found = False
       for i in range(length):
           if char == alphabet[i]:
               letter = alphabet[(i + shift) % length]
               plaintext.append(letter)
               found = True
               break
       if not found:
           plaintext.append(char)
   return plaintext
# converts a list into a string
# for example, the list ["A", "B", "C"] to the string "ABC" or
# the list ["H", "O", "W", " ", "A", "R", "E", " ", "Y", "O", "U", "?"] to the string "HOW ARE YOU?"
def to_string(text):
    s = ""
    return s.join(text)


# main program
playing = True
while playing == True: #loop begins
    method = input("\nWould you like to encode or decode the message?\
    \nType E to encode, D to decode, or Q to quit: \n")
    if method == "E" or method == "e":
        a = to_string(readfile()) #reads file
        b = to_string(encode(a)) #encodes
        c = writefile(b) #writes encoded 
        print(f"\nPlaintext:\n{a}\n")
        print(f"Ciphertext:\n{b}")  #prints out the work
    elif method == "D" or method == "d":
        a = to_string(readfile()) #reads file
        b = to_string(decode(a)) #encodes
        c = writefile(b) #writes encoded 
        print(f"\nCiphertext:\n{a}\n")
        print(f"Plaintext:\n{b}") #prints out the work
    elif method == "Q" or method == "q":
        print("\nGoodbye!")
        playing = False #loop ends
    else:
        print("\nYou did not choose correctly!")  #if the user ever puts in something that's not "e" "d" or "q"

        
