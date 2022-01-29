
class QuizBrain:

    def __init__(self, ques_list):
        self.question_number = 0
        self.question_list = ques_list
        self.score = 0

    def still_have_questions(self):
        if self.question_number < len(self.question_list):
            return True

    def new_question(self):
        current_question = self.question_list[self.question_number].question
        self.question_number += 1
        user_input = input(f"Q-{self.question_number} : {current_question} (True/False):- ")
        self.check_answer(user_answer=user_input, current_answer=self.question_list[self.question_number - 1].answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You're wrong!")
        print(f"The correct answer is {current_answer}")
        print(f"Your total score is : {self.score}/{self.question_number}")
        print("\n")