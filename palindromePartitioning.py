from typing import List

# Here is a very detailed guide for backtracking technique in general
# https://leetcode.com/problems/palindrome-partitioning/solutions/182307/java-backtracking-template-general-approach/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current = []
        