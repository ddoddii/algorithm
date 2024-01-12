# Valid Palindrome
import re


def isPalindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    s_list = re.findall(r"[a-zA-Z0-9]", s)
    str = "".join(s_list)
    return str == str[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
