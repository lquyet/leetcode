from typing import List

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        invalid = set()
        np = len(primes)
        seen = set()
        mapping = {}

        for i in range(2, 31):
            c = i
            m = set()
            ip = 0
            while c != 1:
                while ip < np:
                    if c % primes[ip] == 0:
                        if primes[ip] in m:
                            invalid.add(i)
                            c = 1
                            break
                        m.add(primes[ip])
                        c /= primes[ip]
                        continue
                    ip += 1
                mapping[i] = m

        res = 0
        current = []

        count = {}
        rnums = set()

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

            if num != 1:
                rnums.add(num)

        rnums = list(rnums)
        nn = len(rnums)

        def canChose(num):
            if num in invalid:
                return False
            
            for u in mapping[num]:
                if u in seen:
                    return False
                
            for u in mapping[num]:
                seen.add(u)

            return True

        def getTotal(c):
            r = 1
            for n in c:
                r *= count[n]
            return r

        def helper(current, index):
            nonlocal res
            if index == nn:
                res += getTotal(current)
                return
            
            if canChose(rnums[index]):
                current.append(rnums[index])
                helper(current, index + 1)
                current.pop()
                for u in mapping[rnums[index]]:
                    seen.remove(u)
                
            helper(current, index + 1)
                
        helper(current, 0)
        return (res - 1) * (2**count.get(1, 0))
        
print(Solution().numberOfGoodSubsets([18,28,2,17,29,30,15,9,12]))
            
        
        
        