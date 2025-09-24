class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def cmp(v1, v2):
            if int(v1) == int(v2):
                return 0
            elif int(v1) > int(v2):
                return 1
            return -1

        def helper(v1, v2):
            if len(v1) > 0 and len(v2) > 0:
                r = cmp(v1[0], v2[0])
                if r != 0:
                    return r

                return helper(v1[1:], v2[1:])

            elif len(v1) == 0:
                if any(int(x) != 0 for x in v2):
                    return -1
                return 0
            else:
                if any(int(x) != 0 for x in v1):
                    return 1
                return 0

        version1 = version1.split(".")
        version2 = version2.split(".")

        return helper(version1, version2)


if __name__ == "__main__":
    s = Solution()
    print(s.compareVersion("1.01", "1.001"))  # Output: 0
    print(s.compareVersion("1.0", "1.0.0"))   # Output: 0
    print(s.compareVersion("0.1", "1.1"))     # Output: -1
    print(s.compareVersion("1.0.1", "1"))     # Output: 1
