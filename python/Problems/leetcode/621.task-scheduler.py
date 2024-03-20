#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks).values()
        max_freq = max(task_counts)
        max_freq_tasks = sum(freq == max_freq for freq in task_counts)

        return max((n + 1) * (max_freq - 1) + max_freq_tasks, len(tasks))


# @lc code=end
