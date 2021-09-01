#класс для конкретного ответа на задание 
class Question(object):
    #конструктор 
    def __init__(self, text="", code="", answers=None):

        self.text = text
        self.code = code

        if answers:
            self.answers = answers
        else:
            self.answers = []

    #значение вывода в виде строки 
    def __str__(self):
        return f"{self.text} {self.code} {self.answers}"