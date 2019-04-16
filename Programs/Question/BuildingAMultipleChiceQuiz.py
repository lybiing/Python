from Question import Question

question_prompts =[
    'what color are apples?\n(a) red/green\n(b) puple/blue\n(c) orange\n\n',
    'what color are banana?\n(a) red/green\n(b) puple/blue\n(c) orange\n\n',
    'what color are strawberries?\n(a) red/green\n(b) puple/blue\n(c) orange\n\n'
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print('You got ' + str(score) + '/' + str(len(questions)) + ' correct')

run_test(questions)