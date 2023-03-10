from AutomaticTest import AutomaticTest
from random import randint

test = AutomaticTest()
test.load_data("zbran_test.txt")
test.shuffle_answers()
test.score = 0
answered_questions = []

print("ZBROJNÍ PAS - TEST")
print("----------------------------------------------------------------")
print("Odpovídejte pouze a/b/c")
print()
print()
while True:
    if len(answered_questions) == len(test.questions):
        break
    else:
        rand_question = randint(0, len(test.questions)-1)
        while rand_question in answered_questions:
            rand_question = randint(0, len(test.questions)-1)
        print(test.questions[rand_question])
        print("-------------------------------------------------------------")
        print(f"A) {test.answers[rand_question][0]}")
        print(f"B) {test.answers[rand_question][1]}")
        print(f"C) {test.answers[rand_question][2]}")
        answer = input()
        print(test.check_answer(rand_question, answer))
        answered_questions.append(rand_question)
        print()

print(f"Vaše skóre je: {test.score}/{len(test.questions)}")
input()