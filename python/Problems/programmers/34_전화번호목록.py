# 전화번호 목록에서 접두사 확인


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][: len(phone_book[i])]:
            return False
    return True


# 딕셔너리 사용
def solution2(phone_book):
    headers = dict()
    for phone_number in phone_book:
        headers[phone_number] = 1

    for phone_number in phone_book:
        header = ""
        for number in phone_number:
            header += number
            if header in headers and header != phone_number:
                return False
    return True


# 문자열 정렬 후 , startswith() 함수 사용
def solutino3(phone_book):
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


phone_book = ["12", "123", "1235", "567", "88"]
print(solution2(phone_book))
