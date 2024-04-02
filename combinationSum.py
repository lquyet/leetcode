from typing import List

# Intuitive backtracking idea, quite similar to subSet problem. We can optimize by sorting the candidates first, then use a stop condition if 
# current sum > target to avoid unnecessary recursion
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        self.result = []

        def helper(current_sum_list: List[int], c_index: int, sum_so_far: int = 0):
            if sum_so_far + candidates[c_index] == target:
                self.result.append(current_sum_list + [candidates[c_index]])
                return
            
            if sum_so_far + candidates[c_index] > target:
                return
            
            current_sum_list.append(candidates[c_index])
            helper(current_sum_list, c_index, sum_so_far + candidates[c_index])
            current_sum_list.pop()

            if c_index + 1 < len(candidates):
                helper(current_sum_list, c_index + 1, sum_so_far)


        helper([], 0, 0)
        return self.result
    
# We can also solve this problem using dp approach. DP[i] represents the number of ways to get the target i using the candidates
# The dp equation is:
# for (each way in dp[i - candidate]):  (note that dp[i - candidate] is a list of ints that its sum is equal to i - candidate)
#     dp[i].append(way + [candidate])   (so dp[i-candidate] + [candidate] is a list of ints that its sum is equal to i)
    
# The above solution may produce duplicate results, due to the fact that we make the previous dp of c1 "aware" of c2, c3, c4, ... candidates
# For example, in c = 2 (the first candidate in list), we should not get any values for dp[5] (by dp[5 - candidate 2] = dp[3] -> we already have values for dp[3] here -> wrong). Here we can only fill dp[2] 
# with [2] and dp[4] by dp[4 - candidate 2] = dp[2]. 
# in c = 3, we now aware of 2 candidates 2 and 3, only then we should have the value for dp[5] (by dp[5 - candidate 3] = dp[2] - since we got dp[2] in previous loop, this is correct)
class SolutionDP:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]

        # WRONG SECTION START
        for c in candidates:
            dp[c].append([c])
        # WRONG SECTION END

        for c in candidates:
            for i in range(c + 1, target + 1):
                for way in dp[i - c]:
                    dp[i].append(way + [c])
        
        return dp[target]

# To fix it, we can not pre-set the value for dp[candidate]. Only fill dp[candidate] with [candidate] when we are looping at that exact candidate
class SolutionDPV2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]

        for c in candidates:
            dp[c].append([c])
            for i in range(c + 1, target + 1):
                for way in dp[i - c]:
                    dp[i].append(way + [c])
        
        return dp[target]

if __name__ == "__main__":
    # s = Solution()
    # s = SolutionDP()
    s = SolutionDPV2()
    print(s.combinationSum([2,3,6,7], 7)) # [[2,2,3], [7]]