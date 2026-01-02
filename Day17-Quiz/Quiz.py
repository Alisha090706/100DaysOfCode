from Question import Question
from QuestionBank import questions
from Quiz_Brain import QuizBrain

question_bank=[] 
for question in questions:
    new_question=Question(question["text"],question["answer"])
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score: ({quiz.score}/{quiz.question_number})")