#ask user for a plain text sentence
sentence = input("Please enter a plain text sentence to be encrypted:")

#convert to lower case
sentence = sentence.lower()

#create a dictionary of the ceasar cipher
ceasar_cipher = {'a' : 'f',
                 'b' : 'g',
                 'c' : 'h',
                 'd' : 'i',
                 'e' : 'j',
                 'f' : 'k',
                 'g' : 'l',
                 'h' : 'm',
                 'i' : 'n',
                 'j' : 'o',
                 'k' : 'p',
                 'l' : 'q',
                 'm' : 'r',
                 'n' : 's',
                 'o' : 't',
                 'p' : 'u',
                 'q' : 'v',
                 'r' : 'w',
                 's' : 'x',
                 't' : 'y',
                 'u' : 'z',
                 'v' : 'a',
                 'w' : 'b',
                 'x' : 'c',
                 'y' : 'd',
                 'z' : 'e',
}


#create an empty string variable for the encrpted sentence
encrypted_sentence = ''

#encrypt the sentence by making a for loop to cycle through caharacter and replace them if they match an entry in the cipher dictionary, else add the un-encrypted character to the sentence(punctutaion, spaces, numbers, etc.)
for c in sentence:
    if c in ceasar_cipher:
        encrypted_sentence = encrypted_sentence + ceasar_cipher[c]
    else:
        encrypted_sentence = encrypted_sentence + c

#print the encrypted senctence7
print(encrypted_sentence)
# add your code here
