class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        count_c1 = {}
        for c in s1:
            count_c1[c] = count_c1.get(c, 0) + 1
        
        frame_size = len(s1)
        count_c2 = {}
        for i in range(frame_size):
            count_c2[s2[i]] = count_c2.get(s2[i], 0) + 1
        
        if count_c1 == count_c2: return True
        
        start = frame_size
        while start < len(s2):
            count_c2[s2[start]] = count_c2.get(s2[start], 0) + 1
            count_c2[s2[start - frame_size]] -= 1
            if count_c2[s2[start - frame_size]] == 0:
                del count_c2[s2[start - frame_size]]
            if count_c1 == count_c2: return True
            start += 1

        return False
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkInclusion("ab", "eidbaooo"))