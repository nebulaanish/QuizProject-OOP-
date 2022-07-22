

class quiz_brain():
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f'Q.{self.question_number}: {current_question.text}(True or false)? ')
        self.check_answer(current_question.answer, user_answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, correct_answer, user_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Your are correct ")
            self.score += 1
        else:
            print("You were wrong! :( ")

        print(f"Correct Answer: {correct_answer}")
        print(f"Score: {self.score}/{self.question_number}\n")
