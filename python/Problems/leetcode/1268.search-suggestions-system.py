#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        products.sort()

        answer = []
        match = []
        for idx in range(1, len(searchWord) + 1):
            match = []
            for product in products:
                if product.startswith(searchWord[:idx]):
                    match.append(product)
            answer.append(match[:3])
        return answer

    """
    - two pointer
    """

    def suggestedProducts2(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        answer = []
        products.sort()
        left, right = 0, len(products) - 1
        for idx in range(len(searchWord)):
            c = searchWord[idx]
            while left <= right and (
                len(products[left]) <= idx or products[left][idx] != c
            ):
                left += 1
            while left <= right and (
                len(products[right]) <= idx or products[right][idx] != c
            ):
                right -= 1

            answer.append(products[left : right + 1][:3])
        return answer


# @lc code=end
