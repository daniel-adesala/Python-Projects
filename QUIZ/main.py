from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dict in question_data:
    question = dict['question']
    answer = dict['correct_answer']
    newquestion = Question(question, answer)
    question_bank.append(newquestion)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.retrieve()

print(f"You've completed the Quiz \nYour final score is: {quiz.score}/{len(question_bank)}")