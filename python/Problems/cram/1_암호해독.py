# ord() : 문자 -> 숫자
# chr() : 숫자 -> 문자

text = [
    "   + -- + - + -   ",
    "   + --- + - +   ",
    "   + -- + - + -   ",
    "   + - + - + - +   ",
]
letter = []
for i in text:
    letter.append(
        chr(int(i.strip().replace(" ", "").replace("-", "0").replace("+", "1"), 2))
    )

print("".join(letter))
