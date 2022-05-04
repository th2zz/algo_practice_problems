class Solution:
    """https://www.lintcode.com/problem/13/?_from=collection&fromId=161
    解法1: 暴力O(n^2) for循环起始位置 一个一个字符比较 等则继续不等抛弃并查看下一个起始位置 匹配则返回
    解法2: RabinKarp O(n + m) O(1)
    计算每一个target长度滑动窗口的hashcode 和target hashcode比较 相同进行二次校验 找到即返回
    Description
For a given source string and a target string, you should output the first index(from 0) of target string in the source
string.If the target does not exist in source, just return -1.

Do I need to implement KMP Algorithm in a real interview?

Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your
basic implementation ability. But make sure you confirm how to implement with the interviewer first.
Example
Example 1:

Input:

source = "source"
target = "target"
Output:

-1
Explanation:

If the source does not contain the target's content, return - 1.

Example 2:

Input:

source = "abcdabcdefg"
target = "bcd"
Output:

1
Explanation:

If the source contains the target's content, return the location where the target first appeared in the source.

Challenge
O(nm) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)


    - KMP可以拿strong hire但是没必要KMP
    - 这题不是考直接调官方库解决问题 没意义
    O(n^2) brute force best practice  for循环起始位置 一个一个字符比较 等则继续不等抛弃 查看下一个起始位置
    Follow up O(n) : KMP (too complicated) /  Rabin Karp (better for interview case)

    @param source:
    @param target:
    @return: return the starting index of the first occrrence of target str in source str if not exist return -1
    找到target串在source串中的起始index
    """

    def str_str(self, source, target):
        if not target:
            return 0
        for i in range(len(source) - len(target) + 1):  # traverse start pos
            for j in range(len(target)):  # look at this window and match target str char by char
                if source[i + j] == target[j]:  # matched curr char at j
                    if j == len(target) - 1:  # full match and reach the end return
                        return i
                else:  # not matched change start pos
                    break
        return -1

    def str_str2(self, source, target):
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

        # abcd -a 目标找到bcd m=3 power=31^3;
        #    i
        # i = 3, 上面已经*31 +d hashcode = a*31^3 + b*31^2 + c*31 + d, power = 31^3,  source[i - m] = a
        """
        if not target:
            return 0
        power, radix, modulus, n, m = 1, 31, 1000007, len(source), len(target)

        for _ in range(m):  # TODO 计算减去当前window前一个字符的 hash中 的系数     radix^m
            power = (power * radix) % modulus

        target_hash = 0  # TODO 注意滚动哈希都是从0开始算
        for i in range(m):  # compute hash code for target str
            target_hash = (target_hash * radix + ord(target[i])) % modulus

        curr_hash = 0
        for i in range(n):  # TODO 这里不是遍历起始位置 滑动窗口hash的计算依赖当前i的位置 要把i真的移动起来 才能算 不能到最后一个window开始就结束 不能range(n - m + 1)
            curr_hash = (curr_hash * radix + ord(source[i])) % modulus  # add cur char @i to our current hash code
            if i <= m - 2:  # TODO 不够m个字符 继续
                continue
            elif i >= m:  # TODO 判断是不是第二个window (第一个window 0...m-1) i在m-1 只有第二个window才需要开始考虑删字符
                curr_hash = (curr_hash - power * ord(source[i - m])) % modulus  # 要删的window前一个字符表达式中相关项为 radix^m * hash(c)
                if curr_hash < 0:
                    curr_hash += modulus
            if curr_hash == target_hash:  # hash is the same, can still have collision, verify if actually found
                curr_str = source[i - m + 1:i + 1]  # i-m是window前一个字符位置, i-m+1为当前window开始位置 i为结束位置 i是刚加进来的字符
                if curr_str == target:
                    return i - m + 1
        return -1
