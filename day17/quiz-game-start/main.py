from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for entry in question_data:
    current_text = entry["question"]
    current_answer = entry["correct_answer"]
    current_question = Question(current_text, current_answer)
    question_bank.append(current_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"\nFinish. Yuor final score is {quiz.score}/{len(quiz.question_list)}")
