class Solution:
    # https://leetcode.cn/problems/daily-temperatures/description/
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []  # monotonic stack for storing next greater element index
        for i in range(len(temperatures) - 1, -1, -1):
            x = temperatures[i]
            while st and temperatures[st[-1]] <= x:
                st.pop()
            if st:
                res[i] = st[-1] - i
            st.append(i)
        return res