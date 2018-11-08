"""
Written by: Clayton Turner
For: CS 485
Dr. Letha Etzkorn
Project 3: Vigenere Cipher
"""

import string
import itertools

# Generate our dictionary of the alphabet in a dictionary of the form
# A : 0, B : 1, ... etc for uppercase letters, punctionation, and whitespace to handle special characters
alphabet_dict = {a: i for i, a in enumerate(string.ascii_uppercase + string.punctuation + string.whitespace)}

def decrypt(ciphertext: str = None):
    """Decrypts a vigenere cipher"""
    key = ''  # type: str
    plaintext = '' # type: str

    # reads the key into memory. I think this can be accomplished in one line but I wanted to make sure
    # it is read in exactly as written
    for line in open("vcipherkey.txt").readlines():
        line.strip()
        for letter in line:
            key += letter

    # iterate over the cipher text variable,
    # use the modulo operator to not get tripped up if the ciper text is > key length
    # subtract each letters value
    # loop over dictionary, find the matching key, append to plaintext.
    for idx, letter in enumerate(ciphertext):
        current_key_letter  = key[(idx % len(key))] # get the n'th letter of the key
        plaintext_value = (alphabet_dict[letter] - alphabet_dict[current_key_letter]) % len(alphabet_dict)  # add the values together
        for keys, value in alphabet_dict.items():  # find a key that matches the value
            if value == plaintext_value:
                plaintext += keys
    with open("secondplaintext.txt", "w+") as f:
        f.write(plaintext)
    print(plaintext)

def encrypt():
    """Function to encrypt a string through a vigenere method."""
    key = ''  # type: str
    cipher = ''  # type: str

    # reads the key into memory. I think this can be accomplished in one line but I wanted to make sure
    # it is read in exactly as written
    for line in open("vcipherkey.txt").readlines():
        for letter in line:
            key += letter
    
    # iterate over the cipher text variable,
    # use the modulo operator to not get tripped up if the ciper text is > key length
    # add each letters value
    # loop over dictionary, find the matching key, append to plaintext.
    for idx, letter in enumerate(open("plaintext.txt").read()):
        # read file letter by letter
        letter = letter.upper()
        current_key_letter  = key[(idx % len(key))] # get the n'th letter of the key
        cipher_value =  (alphabet_dict[letter] + alphabet_dict[current_key_letter]) % len(alphabet_dict)   # add the values together
        for keys, value in alphabet_dict.items():  # find a key that matches the value
            if value == cipher_value:
                cipher += keys

    with open("vigenerecipheroutput.txt.", "w+") as f:
        f.write(cipher)
    print(cipher)
    decrypt(cipher)
print(alphabet_dict)
encrypt()
