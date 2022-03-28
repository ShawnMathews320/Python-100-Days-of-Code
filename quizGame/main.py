from questionModel import Question
from data import question_data
from quizBrain import QuizBrain

questionBank = []

for i in range(len(question_data['results'])):
    newQuestion = Question(question_data['results'][i]['question'], question_data['results'][i]['correct_answer'])
    questionBank.append(newQuestion)

quiz = QuizBrain(questionBank)

while quiz.stillHasQuestions():
    quiz.nextQuestion()

print(f"You've completed the quiz.\nYour final score is {quiz.score}/{quiz.questionNumber}.")
