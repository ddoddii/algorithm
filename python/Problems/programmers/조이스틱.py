def solution(name):
    ans = 0
    # count up
    A_idx = []
    for i, c in enumerate(name):
        count_up = min(ord(c) - ord("A"), ord("Z") - ord(c) + 1)
        if c == "A":
            A_idx.append(i)
        ans += count_up

    # count side
    n = len(name)
    min_move = n - 1
    next_i = 0
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == "A":
            next_i += 1
        min_move = min(min_move, i + n - next_i + min(i, n - next_i))

    return ans + min_move


name = "JAAABAN"
print(solution(name))
