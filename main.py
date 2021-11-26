from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


qBank =[]
for question in question_data:
    qText = question["question"]
    qAnswer = question["correct_answer"]
    qNew = Question(qText, qAnswer)
    qBank.append(qNew)


quiz = QuizBrain(qBank)

while quiz.hasQuestions():
    quiz.nextQuestion()
print ("You've finished the quiz game!")
print(f"Your final score was {quiz.score}/{quiz.qNumber}")