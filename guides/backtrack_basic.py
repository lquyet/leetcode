from typing import List

"""
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # basically, every backtracking problem can be solved with this template
        # first we need something to store ALL the satisfied results
        # let's call it `res`
        res = []
        n = len(nums)

        # that looks good for a start xD. 
        # next, we will explore all scenarios and push it to res if we can
        # let's define a variable to store the current exploration
        # we will use this variable to store data in each scenario
        current = []

        # to explore, we should define a helper function for easier recursion
        # that function should accept these things as parameters:
        # - current exploration (to go further)
        # - the place where we are at that time (eg: index,... that we are considering)
        # - any accumulated data to avoid calculate again from current exploration (eg: sum of all current elements)
        def helper(current, index):
            # in helper function, we should first define a base case (end condition)
            # most of the time, this condition is checking if the index (2nd param we describe above) 
            # is at the end of exploration space or not
            # sometimes, we could end the exploration sooner, eg: sum of current elements > CONST, etc
            if index >= n:
                # in subset problem, once we arrive at the end of nums, we push current data to final results list
                # because this is a valid answer (we don't need to check for anything else)
                # just to remember, we have to push a copy (deep copy) of current data, as we refer to the same object
                # in every recursive call
                res.append(current.copy())
                return
            
            # after defining end condition, we have to decide the exploration policy
            # in subset case, there are 2 possible scenarios, or decisions, that we can make
            # 1. add current element to current exploration 
            # 2. not adding ...

            # 1.
            current.append(nums[index])
            helper(current, index+1)

            # 2.
            current.pop()
            helper(current, index+1)

        # Finally, we call the helper function with start case, then return the `res`
        helper(current, 0)
        return res
    

# Different problems have different exploration policy. But there are a few patterns that we can follow
# 1. Add, explore, pop, explore -> It's the method we use in the above example. I personally really like this 
# method because it's really natural and intuitive. 
# 
# 2. 
"""
def backtrack(start, current):
    result.append(current)
    for i in range(start, len(nums)):
        backtrack(i + 1, path + [nums[i]])
"""
# This method has the SAME paths for exploration as 1
#
# 3. 
"""
def backtrack(start, path):
    result.append(path)
    for i in range(start, len(nums)):
        backtrack(i, path + [nums[i]])  -> allow choosing 1 element multiple times
"""