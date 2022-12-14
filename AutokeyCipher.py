def char_to_int(character):
    return ord(character)-97

def int_to_char(key):
    return chr(key+97)

def int_to_char_capital(key):
    return chr(key+65)

def encrypt(plaintext,key):
    ciphertext=""
    ciphertext+=int_to_char_capital(key + char_to_int(plaintext[0]))

    for i in range(1,len(plaintext)):
        ciphertext+=int_to_char_capital((char_to_int(plaintext[i])+char_to_int(plaintext[i-1]))%26)
    return ciphertext

plaintext=input("Please enter the text (in lowecase):")
key=input("Enter the key:")
encryption=""
encryption=encrypt(plaintext,int(key))
print(f'Result:{encryption}')