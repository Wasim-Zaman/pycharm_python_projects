# List, Dictionary and DataFrame comprehension

# Consider the following dictionary

student_dict = {
    "student": ["Wasim", "Momin", "Faysal"], 
    "score": [57, 76, 97]
}

# To loop through the dictionary
for (key, value) in student_dict.items():
    #Access key and value
    # print(key, value)
    pass

# import pandas module
import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame (special method for looping DataFrames)
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    print(index, row)
    # Access row.student or row.score
    print(row.student, row.score)
    

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in the following format:

{"A": "Alfa", "B": "Bravo"}

# import dataset
dataset = pd.read_csv('nato_phonetic_alphabet.csv')
# make dictionary using dictionary comprehension
dic_data = {row.letter:row.code for (index, row) in dataset.iterrows()}
print(dic_data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Take input from the user
user_input = list(input('Write any word: ').upper())

# making a list out of dictionary
list_of_phonetic_code = [dic_data[letter] for letter in user_input]
print(list_of_phonetic_code)

