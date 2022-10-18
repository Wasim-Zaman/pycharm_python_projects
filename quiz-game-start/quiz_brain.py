class QuizGame:
    def __init__(self, questions_objects_list):
        self.question_no = 0
        self.questions_objects_list = questions_objects_list
        self.score = 0

    def is_remaining_question(self):
        return self.question_no < len(self.questions_objects_list)

    def get_question(self):
        current_question = self.questions_objects_list[self.question_no].question_text
        self.question_no += 1
        user_input = input(f"Q.{self.question_no}: {current_question}. (True/False):")
        self.evaluate_answer(user_input, self.questions_objects_list[self.question_no - 1].question_ans)

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('Well done! You are right')
            self.score +=1
        else:
            print("OOPS! that was wrong answer")
        print(f'The correct answer was {correct_answer}')
        print(f'Your total score is {self.score}/{self.question_no}')