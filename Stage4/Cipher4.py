def pair_frequencies(ciphertext):
    pairs_dict = {}
    for i in range(0, len(ciphertext)-2, 2):
        pair = ciphertext[i:i+3]
        if pair not in pairs_dict:
            pairs_dict[pair]=1
        else:
            pairs_dict[pair]+=1
    pairs_dict = {pair: freq for pair, freq in sorted(pairs_dict.items(), key=lambda item: item[1], reverse=True)}
    #print(str(pairs_dict) + "\n\n")

def triplet_frequencies(ciphertext):
    triplet_dict = {}
    for i in range(0, len(ciphertext)-4, 2):
        triplet = ciphertext[i:i+5]
        if triplet not in triplet_dict:
            triplet_dict[triplet]=1
        else:
            triplet_dict[triplet]+=1
    triplet_dict = {triplet: freq for triplet, freq in sorted(triplet_dict.items(), key=lambda item: item[1], reverse=True)}
    #print(triplet_dict)

def vigenere_solver(ciphertext, key_length):
    caesershifts = [""]*key_length
    chars_added = 0
    for char in ciphertext:
        if char != "\n" and char != " ":
            index = chars_added % 5
            caesershifts[index] += char
            chars_added+=1
    return caesershifts

def frequency_analsyis(ciphertext):
    char_dict = {} 
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char not in char_dict:
            char_dict[char]=1
        else:
            char_dict[char]+=1
    char_dict = {char: freq for char, freq in sorted(char_dict.items(), key=lambda item: item[1], reverse=True)}
    return char_dict

def test_shift(ciphertext):
    plaintext = []
    chars_added = 0
    for char in ciphertext:
        caeser = chars_added%5

        if caeser == 0:
            shift = 18
        elif caeser == 1:
            shift = 2
        elif caeser == 2:
            shift = 20
        elif caeser == 3:
            shift = 1
        elif caeser == 4:
            shift = 0

        if char != "\n" and char != " ":    
            shift_base = 65 if char.isupper() else 97
            newchar = (ord(char) - shift_base - shift) % 26  # Correct wrap-around
            newchar += shift_base
            plaintext.append(chr(newchar))
            chars_added+=1
    plaintext = ''.join(plaintext)
    print(plaintext)
    return plaintext

if __name__ == "__main__":    
    with open("Stage4/data/input.txt", "r") as infile:
        ciphertext = infile.read().strip()

    pair_frequencies(ciphertext)
    triplet_frequencies(ciphertext)
    caesers = vigenere_solver(ciphertext, 5)
    for caeser in caesers:
        frequency_dict = frequency_analsyis(caeser)
        print(caeser)
        print(str(frequency_dict) + "\n\n")
    test_shift(ciphertext)
        