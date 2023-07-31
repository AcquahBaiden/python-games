from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

new_game = QuizBrain(question_bank)
new_game.next_question()
while new_game.still_has_questions():
    new_game.next_question()

print("You;ve completed the quiz")
print(f"Your final score was: {new_game.score}/{len(question_bank)}")