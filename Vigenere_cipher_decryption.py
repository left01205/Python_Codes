import string
def vigenere_decrypt(ciphertext, key):
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).upper()
    key = key.upper()
    plaintext = []
    
    for i, char in enumerate(ciphertext):
        shift = ord(key[i % len(key)]) - ord('A')
        decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        plaintext.append(decrypted_char)
    
    return ''.join(plaintext)

key=input("Enter key :")
ciphertext=input("Enter text :")
