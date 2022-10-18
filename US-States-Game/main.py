from turtle import Turtle, Screen

# import the data set
import pandas as pd
dataset = pd.read_csv('50_states.csv')

# creating a turtle and screen objects
tur = Turtle()
screen = Screen()

# setting path of the image to the variable
image = "./blank_states_img.gif"

# Adding image to the screen so that we can set the shape of the turtle as the same image
screen.addshape(image)

# setting the shape of the turtle to image
tur.shape(image)

# keeping track of the correct guesses
correct_guess = []

# Use the loop to allow the user to keep guessing
for state in range(len(dataset)):
    # Taking input guess from the user
    user_input = screen.textinput(title=f'{state + 1}/{len(dataset)} States', prompt='Write the name of the next state')


    if user_input != None:  # if user press cancel button

        # converting the input into the title case
        user_input = user_input.title()

        # Exit if you want
        if user_input == "Exit":
            break

        # check if the guess is among the 50 states
        states = dataset['state'].tolist()
        if user_input in states:

            # record the correct guessing into the list
            correct_guess.append(user_input)

            # write correct guess onto the map
            current_state = dataset[dataset['state'] == user_input]
            print (user_input)
            x = int(current_state['x'])
            y = int(current_state['y'])
            write_state = Turtle()
            write_state.hideturtle()
            write_state.penup()
            write_state.goto(x, y)
            write_state.write(current_state['state'].values[0])
    else:
        break

# Track the score
if len(correct_guess) != len(states):
    non_guessed_states = [st for st in states if states != correct_guess]
    non_guessed_states = pd.DataFrame(data=non_guessed_states, columns=['Missing States'])
    non_guessed_states.to_csv('missing_states.csv')

screen.exitonclick()