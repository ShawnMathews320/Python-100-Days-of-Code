class QuizBrain:
    def __init__(self, questionsList) -> None:
        self.questionNumber, self.score = 0, 0  # start game and score at 0
        self.questionsList = questionsList  # get our list of questions

    def nextQuestion(self):
        currentObject = self.questionsList[self.questionNumber]  # get the current object in the list
        self.questionNumber += 1
        userAnswer = input(f"Q.{self.questionNumber}: {currentObject.text} (True/False)?: ")  # ask user to answer question
        
        return self.checkAnswer(userAnswer, currentObject.answer)

    def stillHasQuestions(self):
        return self.questionNumber < len(self.questionsList)  # return if there is any more questions left to ask user

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():  # if answer is correct
            self.score += 1
            print(f"You got it right!\nThe correct answer was: {correctAnswer}\nYour current score is: {self.score}/{self.questionNumber}\n")
        else:
            print(f"That's wrong.\nThe correct answer was: {correctAnswer}\nYour current score is: {self.score}/{self.questionNumber}\n")