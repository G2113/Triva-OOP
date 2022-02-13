from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

quiz = QuizBrain(question_bank)

for item in question_data:
    q_text = item["question"]
    q_answer = item["correct_answer"]
    question_bank.append(Question(q_text,q_answer))

while quiz.still_have_questions():
    quiz.next_question()

print(f"You have completed the quiz \n Your final score was: {quiz.score}/{quiz.question_number}")