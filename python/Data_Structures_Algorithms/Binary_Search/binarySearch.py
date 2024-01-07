"""
이진탐색 구현
python 에서는 bisect 라이브러리 지원
"""
from bisect import bisect, bisect_left, bisect_right


def myBisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError("lo must be greater than or equal to 0")
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1  # 찾는 x 가 mid 값보다 크면, mid 오른쪽 탐색
        else:
            hi = mid  # 찾는 x가 mid 값보다 작으면, mid 왼쪽 탐색
    return lo


mylist = [1, 2, 3, 3, 3, 7, 9, 11, 33]
print(bisect(mylist, 3))
print(bisect_left(mylist, 3))
print(bisect_right(mylist, 3))
