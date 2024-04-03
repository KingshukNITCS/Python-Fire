'''
Character to ASCII Code
You can use the ord function to get the ASCII code of a character.
'''
char = 'A'
ascii_code = ord(char)
print(f"The ASCII code of '{char}' is {ascii_code}")
# Output - The ASCII code of 'A' is 65


'''
ASCII Code to Character
Conversely, the chr
 function converts an ASCII code to its corresponding character.
 '''
ascii_code = 97
character = chr(ascii_code)
print(f"The character with ASCII code {ascii_code} is '{character}'")
# Output - The character with ASCII code 97 is 'a'


'''
Working with Strings
1. Iterating Through Characters:
You can iterate through each character in a string and obtain its ASCII code.
'''
text = "Hello"
for char in text:
	ascii_code = ord(char)
	print(f"The ASCII code of '{char}' is {ascii_code}")
'''
Output - The ASCII code of 'H' is 72

The ASCII code of 'e' is 101

The ASCII code of 'l' is 108

The ASCII code of 'l' is 108

The ASCII code of 'o' is 111
'''


'''
2. Converting String to ASCII Codes:
You can convert an entire string into a list of ASCII codes.
'''
text = "Python"
ascii_list = [ord(char) for char in text]
print(f"ASCII codes of characters in '{text}': {ascii_list}")
'''
Output - ASCII codes of characters in 'Python': [80, 121, 116, 104, 111, 110]
'''

# Problem Statement - Caesar Cipher Encryption and Decryption. The Caesar cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

def encrypt(message, shift):
    encrypted_text = ''.join([chr(ord(char) + shift) for char in message])
    return encrypted_text

def decrypt(encrypted_message, shift):
    decrypted_text = ''.join([chr(ord(char) - shift) for char in encrypted_message])
    return decrypted_text
  
encrypted_message= encrypt("Hey Geek! What's your progress?", 5)
print("Encrypted Message :", encrypted_message)
decrypted_message = decrypt(encrypted_message, 5)
print("Decrypted Message :", decrypted_message)
'''
Output -Encrypted Message : Mj~%Ljjp&%\mfy,x%~tzw%uwtlwjxxD

Decrypted Message : Hey Geek! What's your progress?
'''


