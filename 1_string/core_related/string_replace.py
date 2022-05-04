class Solution0:
    """https://www.lintcode.com/problem/841/?_from=collection&fromId=161
Given two identical-sized string array A, B and a string S. All substrings A appearing in S are replaced by B.(Notice:
From left to right, it must be replaced if it can be replaced. If there are multiple alternatives,
replace longer priorities. After the replacement of the characters can't be replaced again.)
无重复 对应位置长度相等
The size of each string array does not exceed 100, the total string length does not exceed 50000.
The lengths of A [i] and B [i] are equal.
The length of S does not exceed 50000.
All characters are lowercase letters.
We guarantee that the A array does not have the same string
Example
Example 1

Input:
A = ["ab","aba"]
B = ["cc","ccc"]
S = "ababa"

Output: "cccba"
Explanation: In accordance with the rules, the substring that can be replaced is "ab" or "aba". Since "aba" is longer,
we replace "aba" with "ccc".
Example 2

Input:
A = ["ab","aba"]
B = ["cc","ccc"]
S = "aaaaa"

Output: "aaaaa"
Explanation: S does not contain strings in A, so no replacement is done.
Example 3

Input:
A = ["cd","dab","ab"]
B = ["cc","aaa","dd"]
S = "cdab"

Output: "ccdd"
Explanation: From left to right, you can find the "cd" can be replaced at first, so after the replacement becomes "ccab",
then you can find "ab" can be replaced, so the string after the replacement is "ccdd".
Tags
Hash Table
Company
Microsoft
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """

    def strStr2(self, source: str, target: str):
        """OPTIONAL Rabin Karp
        source abcde   target cde
        cde
         cde
          cde
        abc => bcd 判断是否等于cde 需要O(m)一个一个字符串比较  如何加速?    如何O(1)完成字符串变换并判断是否相等?
        use hash function to map str to int      k=>v 1:1 injective
        先用个简单的方式: 进制转换方式做hash function\
        31 = magic number base   (we want a big number) % hash size
        hash size = 10^6 越大越不易hash collision
        abcde = (a*31^4 + b*31^3 + c*31^2 + d*31 + e) % 10^6
        bcd = (b*31^2 + c*31 + d) % 10^6
        abcd => bcd
        避免overflow  加减乘前后的取模的结果是一样的。在实现的时候做到应模尽模就可以了 其实不会错乱结果的； 如果变成了负数 再加一遍base
        (a + b) % c = (a % c + b % c) % c
        (a * b) % c =(a % c) * (b % c) % c
        （其中a,b是整数）
        循环过程中的当前window hash变化 abc => bcd  增加d 删掉a
        [ (x * 31 + d) % 10^6 - a * 31^3] % 10^6
        hashcode相等 double check是否真的想等 O(m)  总时间复杂度取决于冲突的次数 均摊O(n + m) SPACE O(1)
        """
        if source is None or target is None:
            return -1
        if target == "":
            return 0
        modulus = 1000000
        m, n = len(target), len(source)
        power = 1
        # 31^m mod modulus
        for i in range(m):
            power = (power * 31) % modulus
        # compute hashcode for target
        target_code = 0
        for i in range(m):
            target_code = (target_code * 31 + ord(target[i])) % modulus
        hash_code = 0
        for i in range(n):
            #  abc +d
            hash_code = (hash_code * 31 + ord(source[i])) % modulus
            # 不够m个字符 继续
            if i < m - 1:
                continue
            elif i >= m:  # 判断是不是第二个window (第一个window 0...m-1) i在m-1 只有第二个window才需要开始考虑删字符 删掉之前window第一个字符
                # abcd -a 目标找到bcd m=3 power=31^3;
                #    i
                # i = 3, 上面已经*31 +d hashcode = a*31^3 + b*31^2 + c*31 + d, power = 31^3,  source[i - m] = a
                hash_code = (hash_code - ord(source[i - m]) * power) % modulus
                if hash_code < 0:
                    hash_code += modulus
            if hash_code == target_code:  # hash is the same, can still have collision, verify if actually found
                if source[i - m + 1:i + 1] == target:
                    return i - m + 1
        return -1

    def stringReplace(self, a: list[str], b: list[str], s: str):
        # 直接rabin karp会TLE 需要借用前缀和 + 预计算思想
        # 查看每个a中patter长度滑动窗口 通过s前缀hash ahash直接计算此窗口子串hash来比较确定是否match  子串hash=ahash =匹配
        # 这样while内匹配直接变成O(1)
        if not a or not b:
            return s
        # sort = inplace, sorted = new arr
        curr_index = 0
        end_res = ""
        used = [False] * len(a)
        while curr_index < len(s):  # not finished
            max_len_pattern = ""
            max_len_pattern_index = -1
            for i, pattern in enumerate(a):  # traverse a
                if used[i] or curr_index + len(pattern) > len(s):  # skip visited
                    continue
                pattern_start_index = self.strStr2(s[curr_index:], pattern)
                if pattern_start_index == curr_index and len(pattern) > len(
                        max_len_pattern):  # matched one, record max len
                    max_len_pattern = pattern
                    max_len_pattern_index = i
            if max_len_pattern:  # if found at least one advance progress
                used[max_len_pattern_index] = True
                end_res += b[max_len_pattern_index]
                curr_index += len(max_len_pattern)
            else:  # cannot match any unused str in a    max_len_pattern_index = -1
                end_res += s[curr_index:curr_index + 1]
                curr_index += 1
        return end_res + s[curr_index:]


"""
["ab","aba"]
["cc","ccc"]
"ababa"
"""


class Solution:
    """ rolling hash, main application: robin karp string pattern matching by polynomial rolling hash
    rsync program
    "bcde" compute substr hash by full string hash
    formula:  substr hash = full str hash - preceded str hash * radix^len(substr)
    gist: 通过预计算的前缀rolling hash可以计算任意子串rolling hash 匹配的子串hash直接进行替换
    字符的hash选取 可以使用unicode_codepoint ord(c), 也可以与a做差 ord(c) - ord('a')
    de hash = 3 * 31 + 4 =  bcde hash - bc hash * 31^2 = 31^3 + 2*31^2 + 3*31 + 4 - (31 + 2) * 31^2
            = 31^3 + 2 * 31^2 + 3 * 31 + 4 - (31^3 + 2 * 31^2) = 3 * 31 + 4
    s_prefix_hash [0, 1, 31 + 2, 31^2 + 2*31 + 3, 31^3 + 2*31^2 + 3*31 + 4]  前i个字符 前缀substr hash
    base  [1, 31, 31^2, 31^3, 31^4]
    curr_idx = 0, "bc", s_prefix_hash[2] - base[2] * s_prefix_hash[0] 从当前位置开始 计算下长度为当前pattern的子串hash
    curr_idx = 1, "bc", s_prefix_hash[3] - base[2] * s_prefix_hash[1] = 31^2 + 2*31 + 3 - 31^2 * 1

    https://stackoverflow.com/questions/21436334/choosing-radix-and-modulus-prime-in-rabin-karp-rolling-hash
    https://en.wikipedia.org/wiki/Linear_congruential_generator

    # 遍历a数组，找一个能从curr_idx开始 和s串匹配的 最长的pattern:
    # 往前看len(pattern)的window 计算这个window的hash并和pattern比对
    # 计算方法: full str hash - radix^len(pattern) * preceded str hash;         full str = [preceded str | pattern]
    # by precomputed prefix hash we know "full str" hash and "preceded str" hash already
    # abcde = a*31^4 + b*31^3 + c*31^2 + d*31 + e,     ab = a*31 + b
    # pattern = cde = hash(abcde) - 31^3*(a*31 + b) = c*31^2 + d*31 + e
    如何理解这个31^3  ab到前面需要整整3轮乘法 coefficient差radix^len(pattern)
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    from typing import Generator

    def lcg(self, modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
        """Linear congruential generator."""
        while True:
            seed = (a * seed + c) % modulus
            yield seed

    def stringReplace(self, a, b, s):
        # radix: also the seed, polynomial rolling hash is essentially a linear congruential generator
        radix, modulus = 31, 1000000007  # modulus is hash size  # TODO modulus不能太小 否则会哈希冲突 导致过不了
        # 1. compute hash value for each str in a
        a_hash = []
        for pattern in a:
            pattern_hash = 0
            for c in pattern:  # 每轮c都不一样 这里可以不用generator 对于无重复的str 每个generator实际上只next了一次
                pattern_hash = (pattern_hash * radix + ord(c)) % modulus  # pattern_hash = next(self.lcg(modulus=modulus, a=pattern_hash, c=curr_char_unicode_codepoint, seed=radix))
            a_hash.append(pattern_hash)
        # 2. precompute prefix hash & base:   s[i]=前i个字符前缀substr hash,  base_arr[i]=seed^i
        s_prefix_hash, base_arr, prefix_hash, base = [0], [1], 0, 1  # TODO hash 基础值0 base1 因为以append方式往里加 所以需要初始化
        for c in s:
            prefix_hash = (prefix_hash * radix + ord(c)) % modulus  # prefix_hash = next(self.lcg(modulus=modulus, a=prefix_hash, c=curr_char_unicode_codepoint, seed=radix))
            s_prefix_hash.append(prefix_hash)
            base = (base * radix) % modulus  # base = next(self.lcg(modulus=modulus, a=base, c=0, seed=radix))  # 对应当前prefix str的最高次base
            base_arr.append(base)
        # 3. str replace
        ans, curr_idx = "", 0
        while curr_idx < len(s):  # while没有构建完成replaced str
            max_len = 0
            matched_max_len_pattern_idx = -1
            for j, pattern in enumerate(a): # 遍历pattern in a
                if len(pattern) + curr_idx > len(s):  # TODO 跳过太长的pattern 例如 curr_idx = 0, len(s) = 4 最多考虑长度为4的pattern
                    continue  # skip too long pattern,
                len_pattern_window_hash = (s_prefix_hash[curr_idx + len(pattern)] - base_arr[len(pattern)] * s_prefix_hash[curr_idx]) \
                    % modulus  # 通过预计算的前缀hash 做差法 计算从curr_idx开始 长度为此pattern长度的窗口 字符串的hash
                len_pattern_window_hash = (len_pattern_window_hash + modulus) % modulus
                if a_hash[j] % modulus == len_pattern_window_hash and max_len < len(pattern):  # 打擂台记录匹配成功最长pattern长度
                    max_len = len(pattern)
                    matched_max_len_pattern_idx = j
            if matched_max_len_pattern_idx == -1:  # 没有找到匹配成功的，保留s原串的当前字母 指针+1
                ans = ans + s[curr_idx:curr_idx + 1]
                curr_idx += 1
            else:  # 找到匹配的，用b数组对应的字符串替换
                ans = ans + b[matched_max_len_pattern_idx]
                curr_idx += max_len
        return ans
