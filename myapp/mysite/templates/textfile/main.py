# -* utf-8 *-
import random

class UserInsert:

    def __init__(self):
        pass

    def inserttext(self, question):
        return input('>>' + question)

class Questions:

    def __init__(self):
        pass

    def question(self):
        with open('Questions.text', 'r') as f:
            line = f.read()
            line = line.split('\n')
        que = random.choice(line)
        return que


if __name__ == '__main__':
    userinsert = UserInsert()
    question = Questions()
    while True:
        q = question.question()
        a = userinsert.inserttext(q)
        if a == 'yes':
            print('頑張ってね！')
            break
        else:
            print(a)
