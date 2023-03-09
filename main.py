from AutomaticTest import AutomaticTest
from random import randint

test = AutomaticTest()
test.load_data("zbran_test.txt")
test.shuffle_answers()

print("ZBROJNÍ PAS - TEST")
print("----------------------------------------------------------------")
print("Odpovídejte pouze a/b/c")
print()
print()
while True:
    rand_question = randint(0, len(test.questions))
    print(test.questions[rand_question])
    print("-------------------------------------------------------------")
    print(f"A) {test.answers[rand_question][0]}")
    print(f"B) {test.answers[rand_question][1]}")
    print(f"C) {test.answers[rand_question][2]}")
    answer = input()
    print(test.check_answer(rand_question, answer))
    print()