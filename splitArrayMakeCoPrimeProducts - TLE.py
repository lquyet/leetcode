from typing import List


def sieve_of_eratosthenes(limit):
    primes = [1] * (limit + 1)
    primes[0] = primes[1] = 1

    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j].append(primes[i] * j)
    r = set()
    for i in range(2, len(primes)):
        if primes[i]:
            r.add(i)
    return r


def build_primes(limit):
    primes = [[] * limit + 1]
    primes[0] = primes[1] = [1]
    for i in range(2, int(limit ** 0.5) + 1):
        if len(primes[i]) == 0:
            for j in range(i * i, limit + 1, i):
                primes[j].append(i * j)



class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        primes = sieve_of_eratosthenes(1000)
        lp = set()
        rp = set()
        lpl = [set() for _ in range(len(nums))]
        rpl = [set() for _ in range(len(nums))]
        for i in range(len(nums)):
            temp = nums[i]
            while temp > 1:
                for p in primes:
                    if temp % p == 0:
                        if p not in lp:
                            lp.add(p)
                        temp //= p
                lpl[i] = lp.copy()

        for i in reversed(range(len(nums))):
            temp = nums[i]
            while temp > 1:
                for p in primes:
                    if temp % p == 0:
                        if p not in rp:
                            rp.add(p)
                        temp //= p
            rpl[i] = rp.copy()

        print(rpl)
        print(lpl)
        for i in range(len(nums)):
            try:
                if not self.collide(lpl[i], rpl[i+1]):
                    return i
            except IndexError:
                return -1

    def collide(self, seta, setb):
        for i in seta:
            if i in setb:
                return True
        return False

def main():
    print(Solution().findValidSplit([557663,280817,472963,156253,273349,884803,756869,763183,557663,964357,821411,887849,891133,453379,464279,574373,852749,15031,156253,360169,526159,410203,6101,954851,860599,802573,971693,279173,134243,187367,896953,665011,277747,439441,225683,555143,496303,290317,652033,713311,230107,770047,308323,319607,772907,627217,119311,922463,119311,641131,922463,404773,728417,948281,612373,857707,990589,12739,9127,857963,53113,956003,363397,768613,47981,466027,981569,41597,87149,55021,600883,111953,119083,471871,125641,922463,562577,269069,806999,981073,857707,831587,149351,996461,432457,10903,921091,119083,72671,843289,567323,317003,802129,612373]))

if __name__ == "__main__":
    main()