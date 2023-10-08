def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = ord(char) + shift
            if shifted > ord('z'):
                shifted -= 26
            encrypted_char = chr(shifted)
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

# Example usage
plaintext = "Mensur Khalid"
shift_value = 3

encrypted_text = caesar_cipher(plaintext, shift_value)
print("Encrypted: " + encrypted_text)

decrypted_text = caesar_decipher(encrypted_text, shift_value)
print("Decrypted: " + decrypted_text)


'''

Certainly! Here's a step-by-step explanation of the Caesar cipher encryption and decryption process along with some insights:

Caesar Cipher Encryption and Decryption Explained:

Step 1: Define the Caesar Cipher Functions

First, we define two functions: caesar_cipher for encryption and caesar_decipher for decryption.

Step 2: Initialize Variables

We start with an empty string encrypted_text where we will store the encrypted or decrypted result.
Step 3: Iterate Through Each Character in the Input Text

We loop through each character in the input text (text) one by one.
Step 4: Check if the Character is an Alphabet Character

Inside the loop, we check if the character is an alphabet character (a-z or A-Z).
Step 5: Handle Uppercase and Lowercase Letters Separately

If the character is alphabetic, we check if it is uppercase or lowercase. This distinction is important because we want to preserve the case of the original text.
To do this, we temporarily convert the character to lowercase with char = char.lower() and then shift it back to uppercase later if needed.
Step 6: Apply the Caesar Cipher Shift

We calculate the shifted character code by adding the shift value to the ASCII code of the lowercase character.
If the shifted code exceeds the code for 'z' (122), we wrap it around to the beginning of the alphabet. This accounts for the shifting beyond 'z' in the alphabet.
Finally, we convert the shifted code back to a character with chr(shifted).
Step 7: Preserve Uppercase

If the original character was uppercase, we convert the shifted character to uppercase as well. This ensures that the case of the letter remains the same.
Step 8: Add the Encrypted/Decrypted Character to the Result

We concatenate the encrypted or decrypted character to the encrypted_text string.
Step 9: Handle Non-Alphabet Characters

If the character is not an alphabet character, such as punctuation or spaces, we leave it unchanged and directly add it to encrypted_text.
Step 10: Return the Encrypted/Decrypted Text

After processing all characters in the input text, we return the encrypted_text as the result.
Step 11: Encryption and Decryption

To encrypt a message, you call caesar_cipher with the plaintext and a positive shift value.
To decrypt the encrypted message, you call caesar_decipher with the ciphertext and the same negative shift value.
Step 12: Example Usage

We provide an example usage of the functions by encrypting and decrypting a message. You can change the plaintext and shift_value to experiment with different messages and encryption strengths.
Feel free to copy and paste this explanation as a comment in your VSCode to better understand the Caesar cipher implementation and how it works.
'''