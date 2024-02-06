from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    text = item["question"]
    answer = item["correct_answer"]
    question = Question(text, answer)
    question_bank.append(question)


brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.new_question()

print(f"You've completed the quiz.\nYour final score was {brain.score}/{brain.question_number}")
