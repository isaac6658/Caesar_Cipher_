def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)  # Decrypting is just encrypting with a negative shift


def main():
    print("Caesar Cipher Program")


message = input("Enter your message: ")
shift = int(input("Enter shift value (negative for left shift): "))

encrypted_message = encrypt(message, shift)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, shift)
print("Decrypted Message:", decrypted_message)



if __name__ == "__main__":
    main()