class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        right_dp = [0 for _ in dominoes]
        left_dp = [0 for _ in dominoes]

        n = len(dominoes)
        closet_r_index = -1
        closet_l_index = -1

        for i in range(n):
            if dominoes[i] == "R":
                closet_r_index = i
            elif dominoes[i] == ".":
                right_dp[i] = closet_r_index
            else:
                closet_r_index = -1

        for i in range(n - 1, -1, -1):
            if dominoes[i] == "L":
                closet_l_index = i
            elif dominoes[i] == ".":
                left_dp[i] = closet_l_index
            else:
                closet_l_index = -1

        for i in range(n):
            if dominoes[i] in ("L", "R"):
                continue

            if right_dp[i] == -1 and left_dp[i] == -1:
                pass
            elif right_dp[i] != -1 and left_dp[i] == -1:
                dominoes[i] = "R"
            elif right_dp[i] == -1 and left_dp[i] != -1:
                dominoes[i] = "L"
            else:
                # no need to +1 here as we need to know which one is larger only, no need to care about the exact value
                rd = i - right_dp[i]
                ld = left_dp[i] - i
                if rd > ld:
                    dominoes[i] = "L"
                elif rd < ld:
                    dominoes[i] = "R"
                # if equal, that it stays straight "."

        return "".join(dominoes)
