from question_model import Question
from data import question_data
from quiz_brain import quiz_brain
# question_data is a list with dictionaries inside
question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
   #  call question class with attributes from question_data list
    question_bank.append(Question(text, answer))
# print(question_bank)

quiz = quiz_brain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print(f"You've completed the Quiz !!")
print(f"Final Score: {quiz.score}/{quiz.question_number}")
