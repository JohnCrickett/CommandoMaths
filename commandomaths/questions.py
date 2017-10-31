import operator

OPERATORS = \
    {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }


def generate_question():
    # TODO question generator
    return \
        {
            'lhs': 1,
            'rhs': 2,
            'operation': '+',
            'options': [1, 3, 7]
        }


def check_answer(question, answer):
    return answer == OPERATORS[question['operation']](question['lhs'],
                                                      question['rhs'])
