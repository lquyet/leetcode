class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0 or len(s) == 1 or k + 1 >= len(s): return len(s)

        l = r = 0
        count = {}
        max_length = -1

        while r < len(s):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1

            _, max_freq = self.get_most_freq_char(count)
            if r - l + 1 - max_freq <= k:
                max_length = max(max_length, r - l + 1)
                r += 1

            else:
                count[s[l]] -= 1
                l += 1
                r += 1

        return max_length   

    def get_most_freq_char(self, count):
        max_freq = 0
        max_char = None
        for char, freq in count.items():
            if freq > max_freq:
                max_freq = freq
                max_char = char
        return max_char, max_freq


if __name__ == "__main__":
    solution = Solution()
    input = "AABABBA"
    k = 1
    print(solution.characterReplacement(input, k))

        