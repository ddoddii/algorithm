from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        answer = ""
        counter = Counter(s)
        intersection = [_ for _ in order if _ in s]
        not_inter = [_ for _ in s if _ not in order]
        for char in intersection:
            answer += char * counter[char]
        for char in set(not_inter):
            answer += char * counter[char]
        return answer


order = "hucw"
s = "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"
sol = Solution()
print(sol.customSortString(order, s))
