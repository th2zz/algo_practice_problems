class Solution:  # https://leetcode-cn.com/problems/decode-ways/
    # give a digit str, return #ways to decode it to ascii letter str. A=1,B=2...

    def numDecodings(self, s):
        if not s:
            return 0
        return self.dfs(s, 0, {})

    def dfs(self, s, start_index, memo):  # 递归定义 找到s[start_index:]的decode_ways
        if start_index in memo:
            return memo[start_index]
        if start_index == len(s):  # 越界=空串 空串decode ways = 1
            return 1
        if s[start_index] == '0':  # 子问题起始字符为0 无法decode
            return 0
        result = self.dfs(s, start_index + 1, memo)  # 起始字符非0 单字可以decode 加上decode1个字符后 剩余问题解
        if start_index + 2 <= len(s) and int(s[start_index: start_index + 2]) <= 26:  # 起始字符非0 2个字符可以decode 加上decode2个字符后剩余问题解
            result += self.dfs(s, start_index + 2, memo)
        memo[start_index] = result  # add 子问题解到memo
        return result

    # 当前字符串可以由 2种情况decode而来
    # 已decode i-1个字符 再decode1个合法字符 123 = [1,2], + 3    or       [1 2], + 3  只有当字符非0才为合法选择
    # 已decode i-2个字符 再decode一组合法2字符group [1], + 23        只有当2字符group为10-26才为合法选择
    # 前i个字符decode ways = 如果可以decode1个字符 前i-1个字符decode ways + 如果可以decode2个字符 前i-2个字符decode ways
    # 如果都无法decode 返回0
    def numDecodings2(self, s: str) -> int:
        if s == "" or s[0] == '0':  # s为空或以0开头 无法decode
            return 0
        n = len(s)
        f = [1, 1]  # f[i]:= 前i个字符的decode ways   i做s index要-1
        for i in range(2, n + 1):  # i-1为当前字符 i-2为前一个字符
            f.append(0)
            curr_c, prev_c = s[i - 1], s[i - 2]
            if curr_c != '0':  # decode1个字符过来的 加上f[i-1]贡献前i-1个字符的decode ways
                f[i] += f[i - 1]  # 例如1,2,3 = 12 3 or 1 2 3  3加到12或1 2上都还是原来的方案数量
            if 10 <= int(prev_c + curr_c) <= 26:  # decode2个字符过来的 group2不能以0开头 需要为10-26 可贡献的f[i-2]前i-2个字符decode ways
                f[i] += f[i - 2]
            if f[i] == 0:  # 无法decode1个或2个字符 = 无解
                return 0
        return f[n]
