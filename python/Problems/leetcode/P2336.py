import heapq

# 2336. Smallest Number in Infinite Set
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.cur = 1
        self.added = set()

    def popSmallest(self) -> int:
        if self.heap:
            smallest =  heapq.heappop(self.heap)
            self.added.remove(smallest)
            return smallest
        else: 
            self.cur += 1
            return self.cur - 1

    def addBack(self, num: int) -> None:
        if self.cur > num and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)
