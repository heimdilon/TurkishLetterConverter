# Created by kor_a at 25/08/2021
unwanted_letters = ["ş", "ı", "ğ", "ü", "ö", "ç",
                    "İ", "Ş", "Ü", "Ö", "Ğ", "Ç"]

wanted_letters = ["s", "i", "g", "u", "o", "c",
                  "I", "S", "U", "O", "G", "C"]

sentence = input("Write something : ")

def changeLetters(sentence):
    letters = [x for x in sentence]
    for letter in letters:
        if letter in unwanted_letters:
            letter_index = letters.index(f"{letter}")
            unwanted_letter_index = unwanted_letters.index(f"{letter}")
            letters[letter_index] = wanted_letters[unwanted_letter_index]
        new_sentence = "".join(letters)
    print(new_sentence)


changeLetters(sentence)
