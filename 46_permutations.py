from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nn = len(nums)
        def bt(n, temp, seen):
            if n == nn:
                self.res.append(temp[::])
                return

            for i in nums:
                if i in seen:
                    continue
                seen.add(i)
                temp.append(i)
                bt(n+1, temp, seen)
                temp.pop()
                seen.remove(i)
        bt(0, [], set())
        return self.res
    
if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))