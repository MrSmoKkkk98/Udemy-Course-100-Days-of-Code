import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("day_26/nato_alphabet/nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = str(input("Type your word: ")).upper()

# for letter in user_input:
#     print(dict[letter])
    
code_words_list = [dict[letter] for letter in user_input]
print(code_words_list)