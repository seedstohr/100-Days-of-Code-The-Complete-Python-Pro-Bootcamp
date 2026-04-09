from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []

for q in question_data:
    new_t = q["text"]
    new_a = q["answer"]
    new_question = Question(new_t, new_a)
    question_bank.append(new_question)

quiz = QuizzBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

if not quiz.still_has_question():

    print("You have completed the quiz!\n"
          f"Your final score was {quiz.user_score}/{quiz.question_number}")
