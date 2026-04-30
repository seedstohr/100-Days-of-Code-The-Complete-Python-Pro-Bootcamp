#import pandas
import pandas

#load csv in to pandas dataframe
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

#convert dataframe to dictionary
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()
                          }
#ask user for word, upper case first letter
user_word = input("Enter a word: ").upper()

#split word into letters and convert to list
word_list = [letter for letter in user_word]

#convert letters to phonetic code words using dictionary
phonetic_code_words = [nato_alphabet_dict[c] for c in word_list if c in nato_alphabet_dict]

#return list of phonetic code words
print(phonetic_code_words)
