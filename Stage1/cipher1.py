import string
import json

def caesar_decrypt(ciphertext):
    frequency = [0] * 26
    
    # Frequency Analysis
    for char in ciphertext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            if (ord(char) - shift_base) < len(frequency):
                frequency[ord(char) - shift_base] += 1
    
    letters = list(string.ascii_uppercase)
    letter_freq = [(letters[i], frequency[i]) for i in range(len(frequency))]
    sorted_letter_freq = sorted(letter_freq, key=lambda x: x[1], reverse=True)
    sorted_letters = [letter for letter, freq in sorted_letter_freq]
    
    most_common = ['E', 'T', 'A', 'I', 'N', 'O', 'S', 'H', 'R', 'D', 'L', 'U', 'C', 'M', 'F', 'W', 'Y', 'G', 'P', 'B', 'V', 'K', 'Q', 'J', 'X', 'Z']
    decrypted_message = list(ciphertext)

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            if char in most_common:
                decrypted_message[i] = most_common[sorted_letters.index(char)]    
    decrypted_message = ''.join(decrypted_message)
    return decrypted_message

def translate_with_known_chars(ciphertext, known_chars):
    translated_message = []
    for char in ciphertext:
        # Check if the character is in known_chars and has a non-empty value
        if char.isalpha() and char.upper() in known_chars:
            translated_value = known_chars[char.upper()]
            if translated_value:  # Check if the translated value is not an empty string
                translated_message.append(translated_value.lower())
            else:
                translated_message.append(char)  # Append original char if translated value is empty
        else:
            translated_message.append(char)  # Keep as is if no translation or not an alphabet
    return ''.join(translated_message)

if __name__ == "__main__":
    # Load known characters from the JSON file
    with open("Stage1/data/known_chars.json", "r") as file:
        known_chars = json.load(file)

    with open("Stage1/data/input.txt", "r") as infile:
        ciphertext = infile.read().strip()

    decrypted_message = caesar_decrypt(ciphertext)
    translated_message = translate_with_known_chars(ciphertext, known_chars)

    # Write both messages to frequency_analysis.txt
    with open("Stage1/data/frequency_analysis.txt", "w") as outfile:
        outfile.write(ciphertext + "\n")  # Original cipher text
        outfile.write(translated_message + "\n")  # Translated message
