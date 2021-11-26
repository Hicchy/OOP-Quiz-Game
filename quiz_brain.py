


# TODO: Ask the question
# TODO: Check if answer is correct
# TODO Check if quiz ended


notEnded = True
correct = "That's correct!"
wrong = "That was the wrong answer."


class QuizBrain:
    def __init__(self, qList):
        self.qNumber = 0
        self.qList = qList
        self.score = 0
        self.qAsked = 0


    def hasQuestions(self):
        if self.qNumber < len(self.qList):
            return True
        elif self.qNumber > len(self.qList):
            print ("You've completed the quiz game!")
            print(f"Your final score was {self.score} / {self.curQuestion}")
            return False

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer == correctAnswer:
            self.score += 1
            print("You got it right!")
        else:
            print("That was the wrong answer.")
        print(f"The correct answer was {correctAnswer}")
        print(f"{self.score} / {self.qNumber}")
        print("\n")


    def nextQuestion(self):
        self.curQuestion = self.qList[self.qNumber]
        self.qNumber += 1
        userAnswer = input(f"Q.{self.qNumber}: {self.curQuestion.text} (True/False): ")
        self.checkAnswer(userAnswer, self.curQuestion.answer)













# while notEnded:
#    qqq = random.choice(qBank)
#    print(qqq.text)
#    userAnswer = input("Is this question True or False?    ")
#    if userAnswer == qqq.answer:
#        score +=1
#        print(correct)
#    else:
#        print(wrong)
#    questionAsked += 1
#    scoreBoard = str(score) + "/" + str(questionAsked)
#    print(scoreBoard)
#    print("")
#    print("")
#
#    if questionAsked == 4:
#        print(f"Your final score is {score} out of {questionAsked}")
#        notEnded = False
