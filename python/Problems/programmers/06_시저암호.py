#06. 시저 암호
# ord(a) = 97, ord(z) = 122, ord(A) = 65, ord(Z) = 90
def solution(s, n):
    answer = ''
    for char in s:
        if ord(char) >= 97 and ord(char) <= 122:
            if ord(char) + n <= 122:
                newChar = chr(ord(char)+n)
            else :
                newChar = chr(ord(char)+n-26)
        if ord(char) >= 65 and ord(char) <= 90:
            if ord(char) + n <= 90:
                newChar = chr(ord(char)+ n)
            else:
                newChar = chr(ord(char)+n-26)
        if char == ' ':
            newChar = char
        answer += newChar
    
    return answer

def solution2(s,n):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        corr = ord('A') if s[i].isupper() else ord('a')
        s[i] = chr((ord(s[i]) - corr + n)%26 + corr)
    return ''.join(s)

s = "a B z"
n = 4
print(solution2(s,n))