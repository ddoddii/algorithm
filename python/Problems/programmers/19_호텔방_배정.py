# 호텔 방 배정
"""
- k는 1 이상 10^12 이하인 자연수입니다.-> 공간 복잡도도 고려해야 한다. 배열을 사용하여 특정 인덱스가 있는지 확인하는 방법은 불가능하다.
- 주어진 입력값에 대해서만 문제를 해결 ! -> 딕셔너리 활용
- 효율성도 고려해야 한다. -> 20만명의 사람이 같은 방을 찾으면, 재귀가 계속 호출되는 문제가 있다.
- 완전 탐색하지 않게 딕셔너리에 빈 방의 값을 저장해둔다.
"""


import sys

# 재귀의 한도를 올려 놓고 시작 (기본 설정값은 1000)
sys.setrecursionlimit(10000)


def find_emptyroom(chk, rooms):
    # 할당되지 않은 방이면 그대로 반환
    if chk not in rooms:
        rooms[chk] = chk + 1
        return chk
    # 할당된 방이면 재귀 호출 -> chk + 1 부터 시작해서 빈 방이 있는지 확인
    empty = find_emptyroom(rooms[chk], rooms)
    # 다른 사람이 chk 를 원하면, 탐색하지 않고 빈 방 반환하도록 저장
    rooms[chk] = empty + 1
    return empty


def solution(k, room_number):
    rooms = dict()
    for room in room_number:
        chk_in = find_emptyroom(room, rooms)
    return list(rooms)


k = 10
room_number = [1, 3, 4, 1, 3, 1]
print(solution(k, room_number))
