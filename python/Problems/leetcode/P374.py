# Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


def guessNumber(n: int) -> int:
    start, end = 1, n
    while start <= end:
        mid = (start + end) // 2
        # 고른 숫자가 정답보다 크면, 범위를 mid 왼쪽으로 줄인다.
        if guess(mid) == -1:
            end = mid - 1
        # 고른 숫자가 정답보다 작으면, 범위를 mid 오른쪽으로 줄인다.
        elif guess(mid) == 1:
            start = mid + 1
        elif guess(mid) == 0:
            return mid


def guessNumber2(n: int) -> int:
    start, end = 1, n
    # Binary operator (Bitmask)
    myGuess = (start + end) >> 1
    while (res := guess(myGuess)) != 0:
        if res == 1:
            start = myGuess + 1
        else:
            end = myGuess - 1
        myGuess = (start + end) >> 1
    return myGuess


n = 10
pick = 6
print(guessNumber2(n))
