class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # build dictionary of target characters
        count = {}
        for char in t:
            count[char] = count.get(char, 0) + 1

        start = 0
        end = 0
        min_length = len(s) + 1
        res = None

        current_count = {s[0]: 1}

        while True:
            if self.isMatch(current_count, count):
                # min_length = min(min_length, end - start + 1)
                if end - start + 1 <= min_length:
                    res = s[start:end+1]
                    min_length = end - start + 1
                current_count[s[start]] -= 1
                start += 1
                continue
            else:
                end += 1

            if end >= len(s):
                break
            else:
                current_count[s[end]] = current_count.get(s[end], 0) + 1

        return res if res else ""

    def isMatch(self, current_count, count):
        for key in count.keys():
            if key not in current_count or current_count[key] < count[key]:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    input = "ADOBECODEBANC"
    target = "ABC"
    print(solution.minWindow(input, target))