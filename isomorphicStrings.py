class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def cc(a, b):
            if len(a) != len(b):
                return False
        
            check = {}
            n = len(a)

            for i in range(n):
                sum = a[i] + b[i]
                if a[i] not in check:
                    check[a[i]] = sum
                    continue
                if check[a[i]] != sum:
                    return False
            return True

        return cc(s, t) and cc(t, s)

if __name__ == "__main__":
    sol = Solution()
    print(sol.isIsomorphic("badc", "badc")) # True
