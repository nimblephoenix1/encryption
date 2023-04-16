def caesar_cipher(text, key, mode):
    result = ""
    for char in text:
        if char in ['\n', '\t']:
            result += char
            continue
        shift = key % 256
        new_char = chr((ord(char) + shift) % 256)
        if mode == 'd':
            new_char = chr((ord(new_char) - shift * 2) % 256)
        result += new_char
    return result

mode = input("Enter 'e' to encrypt or 'd' to decrypt: ")
file_name = input("Enter the name of the file: ")
key = int(input("Enter the key: "))

with open(file_name, 'r') as f:
    text = f.read()

new_text = caesar_cipher(text, key, mode)

new_file_name = "encrypted_" + file_name if mode == 'e' else "decrypted_" + file_name
with open(new_file_name, 'w') as f:
    f.write(new_text)

print(f"Done! The result has been saved to {new_file_name}.")