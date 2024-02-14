from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
            if l == r:
                return []
        return [l+1, r+1]

def main():
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))

if __name__ == "__main__":
    main()