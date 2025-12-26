class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix_sum = [0 for _ in range(n+1)]

        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        
        def helper(fl: int, sl: int):
            res = -1

            max_suffix_sum = [0 for _ in nums]
            max_suffix_sum[n-sl] = prefix_sum[n] - prefix_sum[n-sl]
            for i in range(n - sl - 1, fl-1, -1):
                max_suffix_sum[i] = max(max_suffix_sum[i+1], - prefix_sum[i] + prefix_sum[i + sl])
            
            for i in range(0, n - fl - sl + 1):
                first_sum = - prefix_sum[i] + prefix_sum[i + fl]
                res = max(first_sum + max_suffix_sum[i + fl], res)

            return res

        return max(helper(firstLen, secondLen), helper(secondLen, firstLen))
        
