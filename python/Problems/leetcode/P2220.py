def minBitFlips(start: int, goal: int) -> int:
    answer = 0
    start_bin = format(start, "b")
    goal_bin = format(goal, "b")
    diff = len(start_bin) - len(goal_bin)
    if diff > 0:
        goal_bin = "0" * abs(diff) + goal_bin
    else:
        start_bin = "0" * abs(diff) + start_bin

    for i in range(len(start_bin)):
        if start_bin[i] == goal_bin[i]:
            continue
        else:
            answer += 1
    return answer


start = 10
goal = 7

print(minBitFlips(start, goal))
