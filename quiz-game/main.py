# TODO-1:- import all the necessary libraries
from data import question_data
from question_model import QuestionModel
from quiz_brain import QuizGame
# TODO-2:- Create a model to separate questions form the answers in the given list of question_data
questions_list = []
for question in question_data:
    # catch one by one dictionary
    q_text = question['text']
    q_ans = question['answer']
    # in order to create a model, we need to create an object of the QuestionModel class lies inside the question_model file
    new_question_model = QuestionModel(q_text, q_ans)
    # create a list of objects in the above model we created
    questions_list.append(new_question_model)
# TODO-3:- Repeat while there exists questions in the quiz game
my_quiz_game = QuizGame(questions_list)
while my_quiz_game.is_remaining_question():
    my_quiz_game.get_question()
# TODO-4:- Get one by one question
