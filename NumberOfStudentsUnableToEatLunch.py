from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st1 = sum(students)

        st0 = len(students) - st1
        sw_i = 0
        n = len(sandwiches)

        while sw_i < n:
            if st0 > 0 and sandwiches[sw_i] == 0:
                st0 -= 1
                sw_i += 1
                continue

            
            if st1 > 0 and sandwiches[sw_i] == 1:
                st1 -= 1
                sw_i += 1
                continue

            break

        return st0 + st1


if __name__ == "__main__":
    s = Solution()
    print(s.countStudents([1,1,0,0], [0,1,0,1]))