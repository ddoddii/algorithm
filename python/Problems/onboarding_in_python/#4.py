# 청개구리 

def flip_large(str):
    flipped = chr(155- ord(str))
    return flipped

def flip_small(str):
    flipped = chr(219 - ord(str))
    return flipped

def solution(string) :
    result = []
    for s in string:
        if ord(s) in range(65,91):
            flipped = flip_large(s)
            result.append(flipped)
        if ord(s) in range(97,123):
            flipped = flip_small(s)
            result.append(flipped)
        else:
            result.append(' ')
            
    result_str = "".join(result)
    return result_str

string = "I love you"
print(solution(string))