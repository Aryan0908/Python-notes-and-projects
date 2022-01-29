from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question_answer in question_data:
    question_bank.append(Question(text=question_answer["text"], answer=question_answer["answer"]))


quiz = QuizBrain(question_bank)
while quiz.still_have_questions():
    quiz.new_question()

print("You have completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")

