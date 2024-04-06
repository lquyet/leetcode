from typing import List

# Quite intuitive we can come up with this solution
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.seen= set()
        n = len(nums)
        nums.sort()

        def encode(cn):
            return ','.join(map(str, cn))

        def backtrack(cl, cn):
            if cl == n:
                e = encode(cn)
                if e not in self.seen:
                    self.res.append(cn[::])
                    self.seen.add(e)
                return 
            
            cn.append(nums[cl])
            backtrack(cl+1, cn)
            cn.pop()

            backtrack(cl+1, cn)

        backtrack(0, [])
        if '' not in self.seen:
            self.res.append([])
        return self.res
    
# See this https://www.youtube.com/watch?v=Vn2v6ajA7U0 for an optimization. 
# Basically we only need to call backtrack with the first (if many duplicated) element, then ignore the others
# The video above have a very detailed visualization. 
# REMEMBER to sort the nums first
class OptimizedSolution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        n = len(nums)
        nums.sort()

        def backtrack(cl, cn):
            if cl == n:
                self.res.append(cn[::])
                return 
            
            cn.append(nums[cl])
            backtrack(cl+1, cn)
            cn.pop()
            while cl < len(nums) - 1 and nums[cl] == nums[cl+1]:
                cl += 1

            backtrack(cl+1, cn)

        backtrack(0, [])
        return self.res
    

# Key takaway: remember the difference of using an **index** and a **for loop** to decide the next element in backtracking
# Using a for loop will help to build a result with the constraint like same length
# Using an index with help to **pick** some element from the input list

if __name__ == "__main__":
    s = OptimizedSolution()
    print(s.subsetsWithDup([1,2,3,4,4]))