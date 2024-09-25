import json

def frequencies(ciphertext):
    frequency_dict = {}
    for char in ciphertext:
        if char not in frequency_dict:
            frequency_dict[char]=1
        else:
            frequency_dict[char]+=1
    frequency_dict = {char: freq for char, freq in sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)}
    del(frequency_dict['\n'])
    print(frequency_dict)
    return frequency_dict

def pair_frequencies(ciphertext):
    pairs_dict = {}
    for i in range(len(ciphertext)-1):
        pair = ciphertext[i:i+2]
        if pair not in pairs_dict and not 'X' in pair:
            pairs_dict[pair]=1
        elif not 'X' in pair:
            pairs_dict[pair]+=1
    pairs_dict = {pair: freq for pair, freq in sorted(pairs_dict.items(), key=lambda item: item[1], reverse=True)}
    print(pairs_dict)

def triplet_frequencies(ciphertext):
    triplet_dict = {}
    for i in range(len(ciphertext)-2):
        triplet = ciphertext[i:i+3]
        if triplet not in triplet_dict and not 'X' in triplet:
            triplet_dict[triplet]=1
        elif not 'X' in triplet:
            triplet_dict[triplet]+=1
    triplet_dict = {triplet: freq for triplet, freq in sorted(triplet_dict.items(), key=lambda item: item[1], reverse=True)}
    print(triplet_dict)

def attempt_decrypt(ciphertext, frequency_dict):
    most_common = [' ','E', 'T', 'A', 'I', 'N', 'O', 'S', 'H', 'R', 'D', 'L', 'U', 'C', 'M', 'F', 'W', 'Y', 'G', 'P', 'B', 'V', 'K', 'Q', 'J', 'X', 'Z']
    plaintext = list(ciphertext)
    for i in range(len(plaintext)):
        if plaintext[i] in frequency_dict:    
            index = list(frequency_dict).index(plaintext[i])
            if index < 27:
                plaintext[i] = most_common[index]
            else:
                plaintext[i] = most_common[index-1]
    plaintext = ''.join(plaintext)
    return plaintext

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
    with open("Stage3/data/known_chars.json", "r") as file:
        known_chars = json.load(file)
    
    with open("Stage3/data/input.txt", "r") as infile:
        ciphertext = infile.read().strip()

    triplet_frequencies(ciphertext)
    pair_frequencies(ciphertext)
    known_chars_translation = translate_with_known_chars(ciphertext, known_chars)
    frequency_dict = frequencies(ciphertext)
    translated_message = attempt_decrypt(ciphertext, frequency_dict)

    # Write both messages to frequency_analysis.txt
    with open("Stage3/data/frequency_analysis.txt", "w") as outfile:
        outfile.write(ciphertext + "\n\n\n")  # Original cipher text
        outfile.write(known_chars_translation + "\n")  # Translated message