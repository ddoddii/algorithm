from math import sqrt


def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(sqrt(int(num)) + 1)):
        if int(num) % i == 0:
            return False
    return True


def solution(numbers):
    answer = set()
    used = [False] * len(numbers)

    def backtrack(curr, used):
        if curr and is_prime(int(curr)):
            answer.add(int(curr))
        for i in range(len(numbers)):
            if not used[i]:
                used[i] = True
                backtrack(curr + numbers[i], used)
                used[i] = False

    backtrack("", used)
    return len(answer)


numbers = "17"
print(solution(numbers))
