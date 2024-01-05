# 완전 탐색


def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]

    student1_ans = make_ans(student1, answers)
    student2_ans = make_ans(student2, answers)
    student3_ans = make_ans(student3, answers)

    scores[0] = count_matches(student1_ans, answers)
    scores[1] = count_matches(student2_ans, answers)
    scores[2] = count_matches(student3_ans, answers)

    return highest_score_indices(scores)


def make_ans(student, answers):
    n = len(answers)
    return student * (n // len(student)) + student[: n % len(student)]


def count_matches(student_answer, answers):
    matches = [i for i, j in zip(answers, student_answer) if i == j]
    return len(matches)


def highest_score_indices(scores):
    # Finding the maximum score
    max_score = max(scores)

    indices = [i + 1 for i, score in enumerate(scores) if score == max_score]

    return indices
