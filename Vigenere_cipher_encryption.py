import string

def vigenere_encrypt(plaintext, key):
    plaintext = ''.join(filter(str.isalpha, plaintext)).upper()
    key = key.upper()
    ciphertext = []
    
    for i, char in enumerate(plaintext):
        shift = ord(key[i % len(key)]) - ord('A')
        encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        ciphertext.append(encrypted_char)
    
    return ''.join(ciphertext)

    key=input("Enter key : ")
    plaintext=input("Enter text to be encrypted : ")
