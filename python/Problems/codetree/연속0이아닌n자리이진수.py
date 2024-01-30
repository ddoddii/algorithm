def binary():
    n = int(input())
    total = []
    for i in range(n):
        temp = ""


n = 3
total = []


def makenumber(total, temp, n):
    if len(temp) == n:
        total.append(temp)
        return
    if temp and temp[-1] == "0":
        makenumber(total, temp + "1", n)
    else:
        makenumber(total, temp + "0", n)
        makenumber(total, temp + "1", n)


makenumber(total, "", 7)
print(total)
