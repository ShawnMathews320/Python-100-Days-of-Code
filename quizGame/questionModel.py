from winreg import QueryValue


class Question:
    def __init__(self, questionText, questionAnswer) -> None:
        self.text = questionText
        self.answer = questionAnswer