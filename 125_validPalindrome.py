class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        s = s.lower()
        ss = {*"abcdefghijklmnopqrstuvwxyz0123456789"}
        while left <= right:
            try:
                while s[right] not in ss:
                    right -= 1
                while s[left] not in ss:
                    left += 1
            except IndexError:
                break
            if left > right:
                break
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

def main():
    s = " "
    print(Solution().isPalindrome(s))

if __name__ == "__main__":
    main()