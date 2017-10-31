from commandomaths.questions import check_answer, generate_question, OPERATORS


def test_generate_question_types():
    question = generate_question()

    assert isinstance(question, dict)
    assert isinstance(question['lhs'], int)
    assert question['operation'] in OPERATORS
    assert isinstance(question['rhs'], int)


def test_generate_random_questions():
    assert False


def test_check_answer():
    question = \
        {
            'lhs': 3,
            'rhs': 5,
            'operation': '+',
            'options': [1, 3, 8]
        }
    correct_answer = 8
    incorrect_answer = 17
    assert check_answer(question, correct_answer)
    assert not check_answer(question, incorrect_answer)
