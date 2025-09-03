from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for x in question_data:
    text = x['text']
    answer = x['answer']
    question_bank.append(Question(text,answer))

quiz_brain_questions = QuizBrain(question_bank)
while quiz_brain_questions.still_has_question():
    quiz_brain_questions.next_question()
else:
    print("You've completed the quizz!!")
    print(f"Your final score was: {quiz_brain_questions.score}/{quiz_brain_questions.question_number}")


