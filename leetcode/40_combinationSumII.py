from typing import List


# Well the problem description is not really clear. 
# https://leetcode.com/problems/combination-sum-ii/description/
# It said `Each number in candidates may only be used once in the combination.`
# You may think the result will only contains distinct numbers, but it doesn't.
# Eg: if the input list is [1,1,3,5], target = 5
# We will have 2 solutions [5] and [1,1,5]. Each ELEMENT will be used at most 1 time, and [1,1,5] is a valid answer
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(cl, cn, csum):
            if csum > target:
                return
            
            if csum == target:
                res.append(cn[::])
                return
            
            if cl == n:
                return
            
            cn.append(candidates[cl])
            backtrack(cl+1, cn, csum + candidates[cl])
            cn.pop()

            while (cl < n - 1 and candidates[cl] == candidates[cl+1]):
                cl += 1

            backtrack(cl+1, cn, csum)
        
        backtrack(0, [], 0)
        return res

# We may found similar solution like this:
# Basically, the `for` loop functions similarly to the "additional" backtrack(cl+1, cn, csum) in our algorithm
# Just another way to write the solution
"""
class Solution:
    def combinationSum2(self, can: List[int], tar: int) -> List[List[int]]:
        can.sort()
        res = set()
        curr = []
        self.solve(can , curr , res , 0 , tar)
        # print(res , can)
        # res = set(res)
        return res

    def solve(self , can:List[int] , curr:List[int] , res:set() , ind:int , tar:int):

        if tar == 0 :
            res.add(tuple(curr))
            return
        if tar < 0 :
            return 
        if ind == len(can):
            return

        n = len(can)

        for i in range(ind , n):
            if i > ind and can[i] == can[i-1] :
                continue
            
            if can[i] > tar :
                break
            
            curr.append(can[i])
            self.solve(can , curr , res , i+1 , tar-can[i])
            curr.pop()

        return 
"""

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([1,2,3,3,4,2,4], 6))
            
