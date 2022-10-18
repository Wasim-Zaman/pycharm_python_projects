student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(key, value)
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    # print(index, row)
    #Access row.student or row.score
    # print(row.student)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
dataset = pd.read_csv('nato_phonetic_alphabet.csv')
dic_data = {row.letter:row.code for (index, row) in dataset.iterrows()}
print(dic_data)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = list(input('Write any word: ').upper())

list_of_phonetic_code = [dic_data[letter] for letter in user_input]
print(list_of_phonetic_code)

