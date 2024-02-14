
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            k = self.key(s)
            if k in m:
                m[k].append(s)
            else:
                m[k] = [s]
        res = []
        for r in m:
            res.append(m[r])
        return res


    def key(self, string: str) -> str:
        res = ""
        k = {'a':0, 'b': 0, 'c':0, 'd': 0, 'e': 0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
        for s in string:
            if s in k:
                k[s] += 1
            else:
                k[s] = 1
        for key in k:
            res += (key+str(k[key]))
        print("key: ", res)
        return res
    

def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    solution = Solution()
    print(solution.groupAnagrams(strs))

if __name__ == "__main__":
    main()