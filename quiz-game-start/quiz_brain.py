class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number = self.question_number+1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?")
        self.check_answer(current_question.answer, user_answer)

    def check_answer(self, correct_answer, user_answer):
        if user_answer.lower() == correct_answer.lower():
            print('Correct.. Next question')
            self.score += 1
        else:
            print('Incorrect')
        print(f"The correct answer was: {correct_answer}")
        print(f"Your correct score is: {self.score}/{self.question_number}")
        print("\n")

