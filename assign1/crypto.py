"""Assignment 1: Cryptography for CS41 Winter 2020.

Name: Fejer Kriszitna
SUNet: fkim1812

Replace this placeholder text with a description of this module.
"""
import utils
import math
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#################
# CAESAR CIPHER #
#################

def encrypt_caesar(plaintext):
    new_text = ""
    for i in range(len(plaintext)):
        index = ( alphabet.find(plaintext[i]) + 3) % 26
        new_text += alphabet[index]
    
    return new_text

def decrypt_caesar(ciphertext):
    new_text = ""
    for i in range(len(ciphertext)):
        index = ( alphabet.find(ciphertext[i]) - 3) % 26
        new_text += alphabet[index]
    
    return new_text


###################
# VIGENERE CIPHER #
###################

def encrypt_vigenere(plaintext, keyword):
    new_text = ""
    longer_keyword = ""
    while (len(longer_keyword) < len(plaintext)):
        longer_keyword += keyword

    for i in range(len(plaintext)):
        index = ( alphabet.find(plaintext[i]) + alphabet.find(longer_keyword[i])) % 26
        new_text += alphabet[index]
    
    return new_text

def decrypt_vigenere(ciphertext, keyword):
    new_text = ""
    longer_keyword = ""
    while (len(longer_keyword) < len(ciphertext)):
        longer_keyword += keyword

    for i in range(len(ciphertext)):
        index = ( alphabet.find(ciphertext[i]) - alphabet.find(longer_keyword[i])) % 26
        new_text += alphabet[index]
    
    return new_text


###################
# SCYTALE CIPHER #
###################

def encrypt_scytale(plaintext,circumference):
    new_text = ""
 
    # puts every letter in a matrix, starting with the columns
    l = [list(plaintext[i:i+ circumference ]) for i in range(0, len(plaintext), circumference)]
    matrix = [s if len(s) == circumference else s+ [None]*(circumference-len(s)) for s in l]
   
   #read the matrix [row][column], starting with the rows
    for j in range(0,circumference):
        for i in range(0, (len(plaintext) // circumference)  ):
            
            if(matrix[i][j] != None):
                new_text += (matrix[i][j])
    return new_text
        

def decrypt_scytale(ciphertext,circumference):
    #construct matrix with empty cells
    matrix = [['\n' for i in range(len(ciphertext))] for j in range(circumference)]
    new_text = []
 
    c = 0
    r = 0

    #filling the matrix with *, to match the pattern
    for i in range(len(ciphertext)):
        if(r == circumference):
            r = 0
        
        matrix[r][c] = '*'
        c += 1
        r += 1

    #changing the *-s with the actual letters
    index = 0
    for i in range(circumference):
        for j in range(c):
            if(matrix[i][j] == "*"):
                matrix[i][j] = ciphertext[index]
                index += 1


    c = 0
    r = 0

    #reading the matrix thru de pattern
    for i in range(len(ciphertext)):
        if(r == circumference):
            r = 0
        
        new_text.append(matrix[r][c])
        c += 1
        r += 1
    
    return ''.join(new_text)

###################
# RAIL FENCE CIPHER #
###################

def encrypt_railfence(plaintext,num_rails):
    matrix = [['\n' for i in range(len(plaintext))] for j in range(num_rails)] 

    dir = False #False->down
    r = 0
    c = 0

    #filling the matrix with the letters in zigzag pattern
    for i in range(len(plaintext)):
        if(r == 0) or (r == num_rails-1):
            dir = not dir

        matrix[r][c] = plaintext[i]
        c += 1

        if dir:
            r += 1
        else:
            r -= 1

    #constructing the answer reading the matrix thru the rows
    new_text = ""
    for j in range(num_rails):
        for i in range(len(plaintext)):
            if matrix[j][i] != '\n':
                new_text += matrix[j][i]

    return new_text

def decrypt_railfence(cyphertext,num_rails):
    matrix = [['\n' for i in range(len(cyphertext))] for j in range(num_rails)] 
    new_text = []

    dir = False #False->down
    r = 0
    c = 0

    #filling the matrix with *, to match the zig-zag pattern
    for i in range(len(cyphertext)):
        if(r == 0) or (r == num_rails-1):
            dir = not dir

        matrix[r][c] = '*'
        c += 1

        if dir:
            r += 1
        else:
            r -= 1

    #changing the *-s with the actual letters
    index = 0
    for i in range(num_rails):
        for j in range(c):
            if(matrix[i][j] == "*"):
                matrix[i][j] = cyphertext[index]
                index += 1
    
    dir = False #False->down
    r = 0
    c = 0
    index = 0

    #reading the matrix thru de pattern
    for i in range(len(cyphertext)):
        if(r == 0) or (r == num_rails-1):
            dir = not dir

        new_text.append(matrix[r][c])
        index += 1
        c += 1

        if dir:
            r += 1
        else:
            r -= 1

    return ''.join(new_text)
