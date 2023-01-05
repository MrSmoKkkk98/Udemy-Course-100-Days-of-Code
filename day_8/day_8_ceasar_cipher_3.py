alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def ceasar(your_text, shift_amount, code_direction):
    if direction == "encode":
        cipher_text = ""
        for letter in your_text:
            position = alphabet.index(letter)
            if letter in your_text:
                new_position = position + shift_amount
                cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")
    if direction == "decode":
        plain_text = ""
        for letter in your_text:
            position = alphabet.index(letter)
            if letter in your_text:
                new_position = position - shift_amount
                plain_text += alphabet[new_position]
        print(f"The decoded text is {plain_text}")


# if direction == "encode":
#encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#decrypt(cipher_text=text, shift_amount=shift)

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
ceasar(code_direction=direction, your_text=text, shift_amount=shift)