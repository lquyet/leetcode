from typing import List


# Y tuong la cac cot trong stack co do cao tang dan, cac cot nay se la first edge cua 1 rectangle nao do
# Khi xuat hien 1 cot index i co h < top stack (index j)
# Tuc la nhung cot trong stack co do cao > h, chi co the tao thanh rectangle voi xa nhat la cot i-1,
# voi do cao cua chinh no heights[j]
# Xem video https://www.youtube.com/watch?v=zx5Sw9130L0 de hieu ro hon
# -----------
# 1 solution ban dau bi TLE, do logic xu ly tao ra qua nhieu hinh chu nhat. Vi du [2,3,1], khi process den 1 thi tao ra
# 2 hinh tu 0->2, tu 1-> 2, trong khi do hinh 1->2 la khong can thiet -> O(n^2) khi den i phai process het cac hinh
# start tu j -> i-1 voi j thuoc [0, i-1]
# TLE submission: https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/1013096736/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        columns = []
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            if len(columns) == 0 or h > columns[-1][1]:
                columns.append([i, h])
                continue
            else:
                first_edge = -1
                while len(columns) > 0 and columns[-1][1] >= h:
                    first_edge = columns[-1][0]
                    area = (i - 1 - columns[-1][0] + 1) * columns[-1][1]
                    max_area = max(area, max_area)
                    columns.pop()

                columns.append([first_edge, h])
        return max_area




def main():
    print(Solution().largestRectangleArea([4,2,0,3,2,4,3,4]))


if __name__ == "__main__":
    main()
