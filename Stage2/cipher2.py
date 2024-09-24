import enchant

def test_shift(ciphertext, shift):
    plaintext = []
    for char in ciphertext:
        if char.isalpha():    
            shift_base = 65 if char.isupper() else 97
            newchar = (ord(char) - shift_base - shift) % 26  # Correct wrap-around
            newchar += shift_base
            plaintext.append(chr(newchar))
        else:
            # Append non-alphabetic characters as is
            plaintext.append(char)

    plaintext = ''.join(plaintext)
    return plaintext

if __name__ == "__main__":
    with open("Stage2/data/input.txt", "r") as infile:
        ciphertext = infile.read().strip()

    shift = 0
    translated_message = ""
    while translated_message == "" and shift<26:
        translated_message = test_shift(ciphertext, shift)
        shift+=1

    with open("Stage1/data/output.txt", "w") as outfile:
        outfile.write(translated_message)  # Translated message