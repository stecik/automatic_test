from random import shuffle

class AutomaticTest():

    def __init__(self):
        self.questions = []
        self.answers = []
        self.validation = []

    def load_data(self, dir):
        with open(dir, "r", encoding="utf-8") as f:
            data = f.readlines()
        for i in range(0, len(data) -5, 5):
            self.questions.append(data[i].strip())
            answers = []
            for j in range(i+1, i+4):
                answers.append(data[j].strip())
            self.answers.append(answers)
            self.validation.append([True, False, False])

    def shuffle_answers(self):
        for i in range(len(self.answers)):
            temp = list(zip(self.answers[i], self.validation[i]))
            shuffle(temp)
            res1, res2 = zip(*temp)
            res1, res2 = list(res1), list(res2)
            self.answers[i] = res1
            self.validation[i] = res2

    def check_answer(self, question_number, answer):
        answer = answer.strip().lower()
        if answer == "a":
            answer = 0
        elif answer == "b":
            answer = 1
        elif answer == "c":
            answer = 2
        else:
            return False
        if self.validation[question_number][answer]:
            return "Správně"
        else:
            return f"Špatně, správně je {self.find_correct_answer(question_number)}"

    def find_correct_answer(self, question_number):
        answers = ["A", "B", "C"]
        for i in range(3):
            if self.validation[question_number][i]:
                return answers[i]
