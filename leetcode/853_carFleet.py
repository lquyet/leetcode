from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        m = {}
        for i in range(len(position)):
            m[position[i]] = speed[i]

        position.sort()
        stack = []
        for i in position:
            if len(stack) == 0:
                stack.append(i)
                continue

            while len(stack) > 0:
                if self.could_form_fleet(i, stack[-1], m, target):
                    stack.pop()
                else:
                    stack.append(i)
                    break
                if len(stack) == 0:
                    stack.append(i)
                    break
        return len(stack)

    def could_form_fleet(self, i, j, m, target):
        # i is closer to target than j
        if m[i] >= m[j]:
            return False
        # calculate number of turns that i comes to target
        turns = (target - i) / m[i]
        if j + turns * m[j] >= target:
            return True
        return False


def main():
    target = 10
    position = [2, 4]
    speed = [3, 2]
    sol = Solution()
    print(sol.carFleet(target, position, speed))


if __name__ == "__main__":
    main()
