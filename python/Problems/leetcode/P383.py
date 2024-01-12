# Ransom Note
from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    st1 = Counter(ransomNote)
    st2 = Counter(magazine)
    return st1 & st2 == st1


def canConstruct2(ransomNote: str, magazine: str) -> bool:
    for i in set(ransomNote):
        if magazine.count(i) < ransomNote.count(i):
            return False
    return True


ransomNote = "aa"
magazine = "ab"

print(magazine.count("a"))
