import random,string


letter_input_1= input ("what letter do you want? Enter 'v' for vowels, 'c' for consonants,'l' for any letter: ")
letter_input_2= input ("what letter do you want? Enter 'v' for vowels, 'c' for consonants,'l' for any letter: ")
letter_input_3= input ("what letter do you want? Enter 'v' for vowels, 'c' for consonants,'l' for any letter: ")

print(letter_input_1,letter_input_2,letter_input_3)
def generator():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    name = letter1 + letter2 + letter3
    return(name)

print(generator())
