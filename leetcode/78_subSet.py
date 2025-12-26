from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(hnums):
            if len(hnums) == 1:
                return [[hnums[0]], []]
            r = helper(hnums[1:])
            return r + [a + [hnums[0]] for a in r]
        return helper(nums)

# Backtracking using backtrack pattern
class BackTrack:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.r = []
        def gen(pos: int, cur: List[int]):
            if pos == len(nums):
                self.r.append(cur.copy())
                return 
            
            for i in [True, False]:
                if i:
                    cur.append(nums[pos])
                gen(pos + 1, cur)
                if i:
                    cur.pop()
        gen(0, [])
        return self.r

# We can avoid i in [True, False] (quite silly i have to admit) by just calling the gen function for the next case like this:
class BackTrackV2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.r = []
        def gen(pos: int, cur: List[int]):
            if pos == len(nums):
                self.r.append(cur.copy())
                return 
            
            cur.append(nums[pos])
            gen(pos + 1, cur)
            cur.pop()

            # Call the next case here meaning we ignore the current element (at pos)
            gen(pos + 1, cur)

        gen(0, [])
        return self.r

t = BackTrackV2()
print(t.subsets([1, 2, 3]))