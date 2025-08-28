class QuizBrain:
    # Controls the flow of the quiz, tracks score and question progression.
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        # Prompts the user with the next question and checks the answer.
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        # Returns True if there are more questions to ask.
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, current_answer):
        # Checks user's answer and updates score.
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("That's wrong!")
        print(f"Correct Answer was: {current_answer}")
        print(f"Your Score: {self.score} / {self.question_number}\n")
