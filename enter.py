import math

s = input()


def compiled(s, x):
    definitions = {'exp': 'math.exp',
                   'sqrt': 'math.sqrt',
                   'sin': 'math.sin',
                   'cos': 'math.cos',
                   'tg': 'math.tan'}
    for i, k in sorted(definitions.items()):
        s = s.replace(i, k)
    return eval(s)


print(compiled(s, 25))
