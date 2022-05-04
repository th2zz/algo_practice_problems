# Study Resources
https://python.plainenglish.io/8-data-structures-every-python-programmer-should-know-acafd46f479b
https://labuladong.gitee.io/algo/

# Interview cases

- 逻辑思维: working solution => optimize it     
- 代码写完没有
- 代码风格
  - 可读性
    - 模块化 缩进超过三层应该考虑抽离逻辑
    - 避免嵌套 多用平行结构 少用else
  - 变量名 函数名 要清晰准确有意义 避免abcd
  - 空格 换行 缩进 style guide
- 边界与异常情况检查
- bug free 避免靠调试写代码   
  - how: improve your coding quality , easier to avoid typos

# How to approach a problem

- 理解问题 复述问题 澄清问题
- 初步想法 实例分析 书写代码
- 测试检验 评判性能 优化解法

## 复杂度重点

- 时间复杂度 - 主要考察点 bigO smallO bigOmega
  - 权衡 如果数据量小要不要那么在意时间效率
  - 时间复杂度是面试中必问的问题。学好时间复杂度，有很多帮助，比如：
    1. 面试官会问你的算法，时间复杂度是多少
    2. 当面试官说，有没有更好的方法时，你知道朝什么样的复杂度优化
    3. 利用时间复杂度倒推算法是面试常用技巧。如 O(logN)的算法几乎可以确定是二分法。
- 空间复杂度 - 次要考察点
- 编程复杂度 - 能看得懂
- 思维复杂度 - 能想得出

### 时间复杂度反推算法

那我们了解时间复杂度有什么用呢？在做题过程中，如果知道题目的数据范围，我们可以通过数据范围估算时间复杂度，再根据时间复杂度估计算法。

算法中，常见的时间复杂度有：

| 复杂度   | 可能对应的语法                                               | 备注                           |
| -------- | ------------------------------------------------------------ | ------------------------------ |
| O(1)     | 位运算                                                       | 常数级复杂度，一般面试中不会有 |
| O(logn)  | 二分法，倍增法，快速幂算法，辗转相除法                       |                                |
| O(n)     | 枚举法，双指针算法，单调栈算法，KMP算法，Rabin Karp，Manacher's Algorithm | 又称作线性时间复杂度           |
| O(nlogn) | 快速排序，归并排序，堆排序                                   |                                |
| O(n^2)   | 枚举法，动态规划，Dijkstra                                   |                                |
| O(n^3)   | 枚举法，动态规划，Floyd                                      |                                |
| O(2^n)   | 与组合有关的搜索问题                                         |                                |
| O(n!)    | 与排列有关的搜索问题                                         |                                |



# GROUP 0 贪心法

为什么学习贪心法没有用？这是一个值得讨论的问题。从我看来，有如下的三个方面的原因：

1. 你能想到的贪心法都是错误的
2. 面试基本不会考
3. 没有通用性

1. 你想得到的贪心法，都是错的。

首先我们需要知道，什么是贪心法。贪心法就好比挑老公时，只看他当前是不是腰缠万贯，不看他未来是否飞黄腾达。而其他的一些算法如动态规划，就好比你通过仔细的调查，发现虽然他现在是一个穷小子，但是是因为身为富二代的他不愿意接受父亲安排，自己出来独自闯荡，但是未来终究要继承千亿家业。

因此，贪心法可以说，是一种目光短浅的算法。一般在算法问题中，可以使用贪心算法的问题，其贪心策略往往都比较复杂，一般人是想不到的。而你容易想到的那些贪心策略，往往都是错的。

举一个实际的例子：

> 求图中A点到B点的最短路径（点与点之间的距离是正整数）。

错误的贪心策略：

> 从A出发，选择里A最近的点X，走到X，然后选择离X最近的点Y，走到Y...

正确的贪心策略（Dijkstra算法）：

> 使用hashmap distance = {} 记录所有点到起点A的最短距离。一开始 distance = {A: 0}，代表目前只有A离起点的最短距离我们是确定知道的。然后在Distance中的点和非distance中的点中找到最小的一对X,Y, 使得 distance[X] + (X到Y的直接连接距离) 最小。其中X在distance里（已经被确认找到了最短距离），Y不在distance里（还没有被确认找到了最短距离）。然后将Y加入distance，并把距离设为 distance[X] + (X到Y的直接连接距离）。

怎么样，正确的贪心算法是不是非常复杂？

2. 面试基本不会考

贪心法的问题，面试基本不会考，因为等同于考智力题或者是背诵题。一个面试官想要自己凭空创造出一个面试题是使用贪心算法的，是非常困难的。（参见LintCode上的贪心算法的题目所占比例可知）。既然如此，如果面试中被问到了贪心算法，那么一定是一道经典的贪心问题，这类问题，我们可以称之为背诵题。因为大多数同学（除了智商很高，或者有算法竞赛经历的那一批），是不可能在面试的时候想得出解法的。

举几个例子：加油站问题 [Gas Station](https://www.lintcode.com/problem/gas-station/)，这个题的做法是，从任意站点出发，走一圈，找到这一圈里剩余Gas最少的那一站，然后从这一站出发走一圈，如果在这一站出发可以顺利走完全程，那么就可以行，否则就不可行。像这样的算法，是需要进行数学证明来证明其正确性的，面试官是没有能力出这样的面试题的。

从另外一个角度来说，贪心算法的题，对于程序的实现能力要求并不高，也违背了**公司通过算法题面试主要是希望考察大家的程序实现能力**这一点。所以面试官和公司也都不倾向于将贪心算法作为面试的算法问题。

3. 没有通用性

二分法，动态规划算法，分治算法，搜索算法等等，很多的算法都是具有通用性的。也就是说，在题目A里，你用了这个算法，在其他的题目B里，你可能完全可以用一样的算法和思路去解决。

而贪心法，他不是“一个算法”，而是“一类算法”的统称，他更多的是一种高屋建瓴的算法思想，而不是具体实施的算法步骤。所以基本的情况就是，你在题目A里用了某个贪心算法解决了这个问题，然后这个题中用到的贪心法，永远也找不到第二个题用类似的方法来解决。

每个题是完全独立的且没有任何联系，这对于学习者来说，无非是背诵越多知道的越多。无法触类旁通，无法举一反三。因此将时间浪费在贪心法上的话，只能是吃力不讨好。

当然，面试中也不是说完全不可能碰到贪心算法，只是几率非常的小，你只需要“背诵”如下的一些几个题的贪心解法就好了：

http://www.jiuzhang.com/qa/2099/

即如下7题

http://www.lintcode.com/problem/majority-number/
http://www.lintcode.com/problem/create-maximum-number/
http://www.lintcode.com/problem/jump-game-ii/
http://www.lintcode.com/problem/jump-game/
http://www.lintcode.com/problem/gas-station/
http://www.lintcode.com/problem/delete-digits/
http://www.lintcode.com/problem/task-scheduler/

# GROUP 1 双指针

## 经典双指针

### 两数之和

https://www.lintcode.com/problem/two-sum/

返回值

- 哈希表方法 O(n) O(n)
- 排序+相向双指针 O(nlogn) O(1)

Follow up

- 如果输入已经排序 哪个更好?   双指针 O(n) O(1)
- 如果要返回索引而不是值 哪个更好 
  - hashmap ! 因为如果是双指针还需要保持排序前值和索引的关系 才能找到值后返回对应索引    这需要额外存储 ;

```python
# two pointers find value 此处无法返回原来的index
class Solution:
    def twoSum(self, numbers, target):
        numbers.sort()
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [numbers[left], numbers[right]]
        return [-1, -1]

# hashtable  find index
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i
        return [-1, -1]

```

Follow up 2

https://www.lintcode.com/problem/two-sum-less-than-or-equal-to-target/

Given an array of integers, find how many pairs in the array such that their sum is `less than or equal to` a specific target number. Please return the number of pairs.

```python
# Input: nums = [2, 7, 11, 15], target = 24. 
# Output: 5. 
# Explanation:
# 2 + 7 < 24
# 2 + 11 < 24
# 2 + 15 < 24
# 7 + 11 < 24
# 7 + 15 < 24

# Input: nums = [1], target = 1. 
# Output: 0. 


class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    naive brute force takes O(n^2) two pass
    O(nlogn) O(1)
    """
    def twoSum5(self, nums, target):
        nums.sort()
        count, left, right = 0, 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1 # decrease sum
            else:
                count += right - left # index @ left+1, ..., right all satisify the condition
                left += 1 # increase sum
        return count


```

### TWO SUM 变种 

#### 607 · Two Sum III - Data structure design

- add: add number to ds   
- find: find if there is a pair that sums to target   

根据具体商业需求设计

naive solution sorted_array + 双指针   time limit exceeded!

- add 插入排序式维护当前顺序 每次add O(m) m=当前元素数量 插入n个元素in total最坏O(n^2) 总额外空间O(n) 
- find 相向双指针O(n)

要先沟通这样做满不满足复杂度要求

方法2 hashmap

- add O(1) 空间O(n) 记一下数出现次数
- find O(n) 遍历每个num 检查target -num是否在hashmap里 O(n*1)

```python
class TwoSum:
    """
    This naive solution will exceed timeout limit
    Description
    Design and implement a TwoSum class. It should support the following operations: add and find.

    add - Add the number to an internal data structure.
    find - Find if there exists any pair of numbers which sum is equal to the value.

    Example
    Example 1:

    add(1); add(3); add(5);
    find(4) // return true
    find(7) // return false
    """
    def __init__(self):
        self.num_to_cnt_map = {}
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        self.num_to_cnt_map[number] = self.num_to_cnt_map.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        for num1 in self.num_to_cnt_map.keys():
            num2 = value - num1
            num2cnt = 2 if num1 == num2 else 1
            if self.num_to_cnt_map.get(num2, 0) >= num2cnt:
                return True
        return False

# a = TwoSum()
# a.add(1)
# a.add(3)
# a.add(5)
# print(a.find(4))
# print(a.find(7))
```

#### 3sum

- 输入没有排好序 不考虑重复
- 可行解 3层暴力循环 O(n^3) O(1)
- 复用two sum 固定一个点A, find two_sum(-A)
  - 固定哪个点 最小 中间 最大值?
    - 中间不合适 会挖空一个点产生两个剩余问题  
      - fixed point [...remaining elements]
      - [remaining element part1...] fixed point [remaining element part2...]
    - 选最小 最大更适合利用two_sum解

```python
class Solution:
    """
    Description
    Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

    Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

    The solution set must not contain duplicate triplets.

    Example
    Example 1:

    Input:

    numbers = [2,7,11,15]
    Output:

    []
    Explanation:

    Cannot find triples such that the sum of three numbers is 0.
    Example 2:

    Input:

    numbers = [-1,0,1,2,-1,-4]
    Output:

    [[-1, 0, 1],[-1, -1, 2]]
    Explanation:

    [-1, 0, 1] and [-1, -1, 2] are two triples.1, 2]]
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # O(n^2 + NlogN) time overall O(k) space k=#solutions
        # 输入没有排好序 不考虑重复
        if not numbers or len(numbers) < 3:
            return []
        numbers = sorted(numbers)
        # 遍历三元组中的最小值 起始位置
        results = []
        for i in range(0, len(numbers) - 2):
            # 和左边一样=考虑过了 跳过  eliminate duplicates
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            # i is first element in triple, find two sum数组起始位置为i + 1
            left, right, target = i + 1, len(numbers) - 1, -numbers[i]
            # 带有去重逻辑的two sum
            self.find_two_sum(numbers, left, right, target, results)
        return results

    def find_two_sum(self, numbers, left, right, target, results):
        # O(n)
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                results.append([-target, numbers[left], numbers[right]])
                right -= 1
                left += 1
                # eliminate duplicates
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif sum > target:
                right -= 1
            else:
                left += 1

```



#### triangle count

```python
class Solution:
    """
    382 · Triangle Count
    Algorithms
    Medium
    Accepted Rate
    41%

    Description
    Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle 
    whose three edges length is the three numbers that we find?

    Example
    Example 1:

    Input: [3, 4, 6, 7]
    Output: 3
    Explanation:
    They are (3, 4, 6),
             (3, 6, 7),
             (4, 6, 7)
    Example 2:

    Input: [4, 4, 4, 4]
    Output: 4
    Explanation:
    Any three numbers can form a triangle.
    So the answer is C(3, 4) = 4
    @param S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        # O(N^2 + NlogN) O(1)
        if not S:
            return 0
        S.sort()  # 必须的因为我们要复用双指针求two sum的解
        # 遍历最大边索引位置 最大边左边寻找两个小边 two_sum
        ans = 0
        for i in range(2, len(S)):
            ans += self.get_triangle_count(S, i)
        return ans

    def get_triangle_count(self, nums, target_index):
        """ 找到target_index 左边  两数之和为target_sum的组合的个数
        """
        # 寻找范围[0, target_index - 1]
        left = 0
        right = target_index - 1
        target_sum = nums[target_index]
        total = 0
        while left < right:
            # 小边之和大于大边
            if nums[left] + nums[right] > target_sum:
                # 一次求出多个可行解的个数 从left 到 right - 1都是满足条件的对 共right - left个
                total += right - left
                right -= 1  # 已经计入right所有可能的情况 减少sum查看下一个right
            else:  # 不够 需要增大sum move left
                left += 1
        return total

```



#### 4sum

https://www.lintcode.com/problem/58/

find unique quadruplets a, b, c, d that sum to target.  Input is not sorted and can have duplicates

- O(n^3 + nlogn)  O(k) k=#solutions
  - 双层for循环固定两个点
  - 双指针扫描后续数组 find two sum unique pairs 

#### 4sum ii

https://www.lintcode.com/problem/976/

给了4个数组 每组里选1个数 使得4sum to 0, find #solutions

- input not sorted
- input has duplicates
- no need to eliminate duplicate answer

```python
class Solution:
    """
    https://www.lintcode.com/problem/976/

    给了4个数组 每组里选1个数 使得4sum to 0, find #solutions

    - input not sorted
    - input has duplicates
    - no need to eliminate duplicate answer
    @param A: a list
    @param B: a list
    @param C: a list
    @param D: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """

    def fourSumCount(self, A, B, C, D):
        # 本题类似two sum iii data structure design
        # - 维护一个ab和出现频次的map
        # - 遍历所有可能cd和的counterpart  cnt累加其在 map中的频次
        table = {}
        for a in A:
            for b in B:
                total = a + b
                table[total] = table.get(total, 0) + 1
        cnt = 0
        for c in C:
            for d in D:
                total = c + d
                cnt += table.get(-total, 0)
        return cnt
```

#### valid palindrome

```python
# https://www.lintcode.com/problem/valid-palindrome/
# 判断是不是回文串 非法字符需跳过
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_char_valid(self, char):
        return char.isdigit() or char.isalpha()
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.is_char_valid(s[left]):
                left += 1
            while left < right and not self.is_char_valid(s[right]):
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
# follow up 可以删除最多一个字符, 没有不合法字符 判断是不是palindrome   巧用子函数避免重复代码
# https://www.lintcode.com/problem/valid-palindrome-ii/
class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """

    def find_first_different_pair(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right

    def validPalindrome(self, s):
        if not s:
            return False
        # left, right 左边右边届index
        s_is_palindrome, left, right = self.is_palindrome(s, 0, len(s) - 1)
        if s_is_palindrome:
            return True
        # 查看左边去掉一个字符 和 右边去掉一个字符的子串是不是palindrome
        return self.is_palindrome(s, left + 1, right)[0] or self.is_palindrome(s, left, right - 1)[0]

    def is_palindrome(self, s, left, right):
        left, right = self.find_first_different_pair(s, left, right)
        return left >= right, left, right
```



#### More

two-sum  `<= >=` target

http://www.lintcode.com/problem/two-sum-less-than-or-equal-to-target/ 

http://www.lintcode.com/en/problem/two-sum-greater-than-target/ 

k-sum [hard] https://www.lintcode.com/problem/89/ 求方案总数   dp  可以dfs 但是杀鸡不要用牛刀 做更难得事情会花更多的时间

k-sum ii [medium] https://www.lintcode.com/problem/90/ 求具体方案 dfs



## 同向双指针

https://www.lintcode.com/problem/610/

https://www.lintcode.com/problem/1870/

https://www.lintcode.com/problem/521/

https://www.lintcode.com/problem/386/

### 同向双指针在数组 链表 字符串中的应用

https://www.lintcode.com/problem/604/

在字符串中要注意的时候就是要好好考虑双指针代表的区间，以及有效的部分的子串数量、长度等边界条件。

https://www.lintcode.com/problem/1246/



链表:

https://www.lintcode.com/problem/102/  带环链表

https://www.lintcode.com/problem/380/  链表交叉

https://www.lintcode.com/problem/228/

#### 链表中点问题

##### 问题描述

求一个链表的中点

##### 问题分析

这个问题可能大家会觉得，WTF 这么简单有什么好做的？你可能的想法是：

> 先遍历一下整个链表，求出长度 L，然后再遍历一下链表找到第 L/2 的那个位置的节点。

但是在你抛出这个想法之后，面试官会追问你：`如果只允许遍历链表一次怎么办？`

可以看到这种 Follow up 并不是让你优化算法的时间复杂度，而是严格的限制了你遍历整个链表的次数。你可能会认为，这种优化有意义么？事实上是很有意义的。因为遍历一次这种场景，在真实的工程环境中会经常遇到，也就是我们常说的数据流问题（Data Stream Problem）。

##### 用双指针算法解决链表中点问题

我们可以使用双指针算法来解决链表中点的问题，更具体的，我们可以称之为快慢指针算法。该算法如下：
Java:

```java
ListNode slow = head, fast = head.next;
while (fast != null && fast.next != null) {
    slow = slow.next;
    fast = fast.next.next;
}

return slow;
```

Python:

```python
slow, fast = head, head.next
while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

return slow
```

在上面的程序中，我们将快指针放在第二个节点上，慢指针放在第一个节点上，while 循环中每一次快指针走两步，慢指针走一步。这样当快指针走到头的时候，慢指针就在中点了。

快慢指针的算法，在下一小节的“带环链表”中，也用到了。

###### 一个小练习

将上述代码改为提供接口的模式，即设计一个 class，支持两个函数，一个是 add(node) 加入一个节点，一个是 getMiddle() 求中间的那个节点。


#### 数据流问题 Data Stream Problem

所谓的数据流问题，就是说，你需要设计一个在线系统，这个系统不断的接受一些数据，并维护这些数据的一些信息。比如这个问题就是在数据流中维护中点在哪儿。（维护中点的意思就是提供一个接口，来获取中点）

类似的一些数据流问题还有：

数据流中位数 http://www.lintcode.com/problem/data-stream-median/

数据流最大 K 项 http://www.lintcode.com/problem/top-k-largest-numbers-ii/

数据流高频 K 项 http://www.lintcode.com/problem/top-k-frequent-words-ii/

这类问题的特点都是，你`没有机会第二次遍历所有数据`。



# GROUP 3 排序

## quick sort

```python
class Solution:
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def sortIntegers2(self, A):
        if not A:
            return A
        temp = [0] * len(A)
        # temp = [0 for _ in range(len(A))]
        self.quick_sort(A, 0, len(A) - 1)

    def quick_sort(self, nums, start, end):
        if start >= end:
            return nums
        pivot = self.partition(nums, start, end)
        self.quick_sort(nums, start, pivot - 1)
        self.quick_sort(nums, pivot + 1, end)
        return nums

    # 比较好记忆的partition实现方式 同向双指针
    # 取pivot
    # pivot换到末尾
    # 同向双指针分区剩余数组为[< pivot | >= pivot]
    # 把右半区间第一个元素与pivot交换 返回pivot index
    
    def partition(self, nums, start, end):
        # or with randint [a,b] randrange [a, b)
        pivot_index = (start + end) // 2
        self.swap(nums, pivot_index, end)
        pivot = nums[end]
        i, j = start, start
        for j in range(start, end):
            if nums[j] < pivot:
                # [< pivot i][ >= pivot]pivot
                self.swap(nums, i, j)
                # i goes to next to-be-swapped pos
                i += 1
        # [< pivot][i >= pivot]pivot
        self.swap(nums, i, end)
        return i
# 解法2 避免切分不均匀的情况
class Solution:
    """
    https://www.lintcode.com/problem/string-sorting/
    @param s: string
    @return: sort string in lexicographical order
    """
    def swap(self, i, j, strings):
        strings[i], strings[j] = strings[j], strings[i]

    def sorting(self, s):
        # reduce the problem to standard quick sorting
        strings = s.split(',')
        self.qsort(0, len(strings) - 1, strings)
        return ','.join(strings)

    def partition(self, start, end, strings):
        left, right = start, end
        pivot = strings[(left + right) // 2]
        while left <= right:
            while left <= right and strings[left] < pivot:
                left += 1
            while left <= right and strings[right] > pivot:
                right -= 1
            if left <= right:
                # swap this pair of inversion
                self.swap(left, right, strings)
                left += 1
                right -= 1
        return left, right

    def qsort(self, start, end, strings):
        if start >= end:
            return
        # use separate variables to preserve original information
        left, right = self.partition(start, end, strings)
        # 此时 two sublists = [start...right]?[left...end]  left 和 right中间有可能还有一个数, left != right
        self.qsort(start, right, strings)
        self.qsort(left, end, strings)


res = Solution().sorting("bb,aa,lintcode,c")
print(res)

```

- quick sort  
  
  - ```python
    # 比较好记忆的partition实现方式 同向双指针
    # 取pivot
    # pivot换到末尾
    # 同向双指针分区剩余数组为[< pivot | >= pivot]
    # 把右半区间第一个元素与pivot交换 返回pivot index
    ```
    
  - O(nlogn) average O(n^2) worst  
    
  - O(1) space in-place 
    
  - Quick Sort, Heap Sort属于不稳定排序 因为元素原始位置取决于不同pivot可能在partition时被打乱
    
  - performance degrade to O(n^2) for a bad pivot : pivot = largest element, smallest element, or when all elements equal
  
    - T(0) = T(1) = 0 (base case)     T(N) = N + T(N-1) 
  
  - 先整体有序再局部有序 T(n) = T(n/2) + O(n) 先完成O(n) 再分治
  
    - left [<= p ] right[>= p]
  
      - 所以和pivot比较不应该囊括 = 的情况 否则left会一直++ / right会一直--, = 不均匀
  
    - 为什么不是left [< p ] right[>= p]  or left [<= p ] right[> p] ？
  
      - 避免排序时出现极端情况 全部一样的input e.g. 11111
  
        - 此时如果用了 < > 会出现不均匀划分
        - 快速排序理想情况是始终左右半接近均分
  
      - 为什么连用4个left <= right: 如果都是< 会stack overflow infinite recursion  
  
        - ```
          [1,2]
           l
           r
           子问题1[1,1] return
           字问题2[1,2] infinite recursion
          ```
  
        - i.e. [start, right], [right + 1, end]。 < 有个核心问题是，left == right 的数可能 < 或 > pivot，因此，子函数时，把这个数放在任何一边都不合适。
  
        - =的时候需要可以正常处理和划分 只要让他们错开就可以了

### 相关问题

kth largest element

- quick select
  - get pivot index and partition around pivot; 第k大数索引为k - 1
  - if pivot index == k - 1  FOUND!
  - else if k - 1 < pivot index,  go to pivot's left
  - else go to pivot's right
- median of two sorted array => kth largest => kth smallest with quick_select => partition

```python
class Solution:
    """ O(n) O(1)
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def quick_select(self, nums, start, end, k):
        # quick select k-th smallest element
        pivot_index = self.partition(nums, start, end)
        if k - 1 == pivot_index:
            return nums[pivot_index]
        elif k - 1 < pivot_index:
            return self.quick_select(nums, start, pivot_index - 1, k)
        else:
            return self.quick_select(nums, pivot_index + 1, end, k)

    def kthLargestElement(self, k, nums):
        if not nums:
            return -1
        if k > len(nums):
            return -1
        # k-th largest = "len(nums) + 1 - k"-th smallest
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) + 1 - k)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def partition(self, nums, start, end):
        # or with randint [a,b] randrange [a, b)
        pivot_index = (start + end) // 2
        self.swap(nums, pivot_index, end)
        pivot = nums[end]
        i, j = start, start
        for j in range(start, end):
            if nums[j] < pivot:
                # [< pivot i][ >= pivot]pivot
                self.swap(nums, i, j)
                # i goes to next to-be-swapped pos
                i += 1
        # [< pivot][i >= pivot]pivot
        self.swap(nums, i, end)
        return i

# 解法2 避免切分不均匀的情况
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if not A or k < 1 or k > len(A):
            return None
        # len(A) - k :: 可以直接当作第索引使用 找到索引为len(A) - k的元素
        return self.quick_select(A, 0, len(A) - 1, len(A) - k)
    
    def partition(self, nums, start, end):
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        return left, right

    def quick_select(self, nums, start, end, k):
        """ find number indexed at k
        During the process, it's guaranteed start <= k <= end
        """
        if start == end:
            return nums[k]
        left, right = self.partition(nums, start, end)
        # 此时 two sublists = [start...right]?[left...end]  left 和 right中间有可能还有一个数, left != right
        if k <= right:
            return self.quick_select(nums, start, right, k)
        if k >= left:
            return self.quick_select(nums, left, end, k)
        return nums[k]
```

#### 快速选择算法的 Partition 的实质：

快速选择/快速排序中的 partition 是 可左可右 的partition，也就是说，对于nums[i] == pivot 时，这个数字既可以放在左边，也可以放在右边。

#### 为什么这样划分数组呢？

原因是为了避免出现类似 [1,1,1,1,1,1] 的数组中的元素，全部被分到一边的情况。我们让 nums[i] == pivot 的情况既不属于左边也不属于右边，这样就能够让 partition 之后的结果稍微平衡一些。
如果 quick select / quick sort 写成了nums[i] < pivot 在左侧，nums[i] >= pivot 在右侧这种形式，就会导致划分不平均，从而导致错误或者超时。

#### 为什么问题《partition array》不能使用同样的代码？

对于问题《partition array》来说，题目的要求是将数组划分为两个部分，一部分满足一个条件，另外一部分不满足这个条件，所以可以严格的把 nums[i] < pivot 放在左侧，把 nums[i] >= pivot 放在右侧，这样子做完一次 partition 之后，就能够将这两部分分开。

```python
class Solution:
    """https://www.lintcode.com/problem/31/ 
    Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.
Example
Example 1:

Input:

nums = []
k = 9
Output:

0
Explanation:

Empty array, print 0.

Example 2:

Input:

nums = [3,2,2,1]
k = 2
Output:

1
Explanation:

the real array is[1,2,2,3].So return 1.

Challenge
Can you partition the array in-place and in O(n)O(n)?
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def partitionArray(self, nums, k):
        if not nums:
            return 0
        start, end = 0, len(nums) - 1
        # 没有必要去取pivot index并交换至末尾了因为不需要 pivot在中间 也不需要他的index 只需要满足 left half < k; right half >= k
        # pivot_index = (start + end) // 2
        # self.swap(nums, pivot_index, end)
        pivot = k
        i, j = start, start
        # end + 1 因为pivot不在末尾了
        for j in range(start, end + 1):
            if nums[j] < pivot:
                # [< pivot i][ >= pivot]
                self.swap(nums, i, j)
                # i goes to next to-be-swapped pos
                i += 1
        # [< pivot][i >= pivot]
        # 这里也没有必要了 因为pivot都不在末尾了
        # self.swap(nums, i, end)
        return i


# print(Solution().partitionArray([3,2,1], 2))
# 同向双指针partition法的一个变种 具体就是不需要取pivot了(当然也就不需要把pivot移动到末尾) 直接用给定的k  j的遍历range注意不再是去掉末尾的range 而是整个range
# 根据invariant 最后i的位置即右半>=pivot开始位置
```

#### interleaving positive and negative numbers

- 可行解
  - 先全部排序 
    - 没有必要 只需要把正负分开
  - 再正负交错 
  - 已知数据确保正负数相差个数不超过1  正数还是负数多有关系吗
    - 负数多 左负右正after partition; left =1, right = length - 1 间隔交换
    - 正数多 left = 0, right = length - 2 间隔交换
    - 一样 left = 0, right = length - 1 间隔交换

```python
class Solution:
    """
    https://www.lintcode.com/problem/144/
    Description
    Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

    You are not necessary to keep the original order of positive integers or negative integers.

    Example
    Example 1

    Input : [-1, -2, -3, 4, 5, 6]
    Outout : [-1, 5, -2, 4, -3, 6]
    Explanation :  any other reasonable answer.
    Challenge
    Do it in-place and without extra memory.
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # O(n) O(1)
        # 输入是否有序 不是
        # 有没有重复数字 影响不大
        # 已知数据确保正负数相差个数不超过1
        # 不需要额外空间
        # 不需要保持正数和负数原来的顺序
        neg_cnt = self.partition(A)
        pos_cnt = len(A) - neg_cnt
        left = 1 if neg_cnt > pos_cnt else 0
        right = len(A) - (2 if pos_cnt > neg_cnt else 1)
        self.interleave(A, left, right)

    def partition(self, A):
        #  after partition two sublists = [start...right]?[left...end]  left 和 right中间有可能还有一个数, left != right
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] < 0:
                left += 1
            while left <= right and A[right] > 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        return left

    def interleave(self, A, left, right):
        while left < right:
            A[left], A[right] = A[right], A[left]
            left, right = left + 2, right - 2

```

#### sort colors in place

[0, 1, 2, 0, 2, 1, 1] => [0, 0, 1, 1, 1, 2, 2]

- naive: sort it, O(NlogN) O(1)
- counting sort  O(N) O(1)
- quick partition
  - two pass partition array by 1, then by 2
  - one pass 0丢左边 2丢右边 1放中间   too complicated, not good for production

```python
class Solution:
    """
    Description
    Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

    You are not suppose to use the library's sort function for this problem.
    You should do it in-place (sort numbers in the original array).

    Example
    Example 1

    Input : [1, 0, 1, 2]
    Output : [0, 1, 1, 2]
    Explanation : sort it in-place
    Challenge
    Could you come up with an one-pass algorithm using only O(1) space?

    DO IT IN O(N) O(1) ?
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def sortColors_counting_sort(self, nums):
        # - 计数排序 统计每种颜色出现次数
        # - 根据统计结果覆盖原数组
        if not nums:
            return
        color_cnts = [0] * 3
        for num in nums:
            color_cnts[num] += 1
        index = 0
        # done counting; fill in original array
        for i in range(len(color_cnts)):
            cnt = color_cnts[i]
            while cnt > 0:
                nums[index] = i
                cnt -= 1
                index += 1

    def sortColors(self, nums):
        # 建议
        self.partition_arrays(nums, 1)
        self.partition_arrays(nums, 2)

    def partition_arrays(self, nums, k):
        if not nums:
            return 0
        start, end = 0, len(nums) - 1
        pivot = k
        i, j = start, start
        for j in range(start, end + 1):
            if nums[j] < pivot:
                self.swap(nums, i, j)
                i += 1
        return i

    def sortColors_one_pass(self, nums):
        # onepass工程角度不推荐 可读性差
        zeroPt = -1
        twoPt = len(nums)
        i = 0
        # i < twoPt 是个很重要的条件
        while i < len(nums) and i < twoPt:
            if nums[i] == 0:
                zeroPt += 1
                nums[zeroPt], nums[i] = nums[i], nums[zeroPt]
                # 没有i-- 因为换过来的只可能是1 不需要再交换了
                # 当前指针左边不可能有2 所有的0也都小于zeroPt +1前的位置
            elif nums[i] == 2:
                twoPt -= 1
                nums[twoPt], nums[i] = nums[i], nums[twoPt]
                i -= 1
            i += 1

```



#### sort k colors / rainbow sort

https://www.lintcode.com/problem/143/

-  partition + 递归分治 先整体有序再局部有序

#### 总结

- 简单的说就是，**想要避免划分不均匀情况版本**的quick select 和 quick sort 的 partition 目标不是将数组 严格的按照 nums[i] < pivot 和nums[i] >= pivot 去拆分开，而是只要能够让左半部分 <= 右半部分即可。这样子 nums[i] == pivot 放在哪儿都无所谓，两边都可以放。
- array + 固定的有限种元素sort + O(N)时间 ====》 有限次快速排序partition

```python
class Solution:
    """
    Description
    Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

    You are not suppose to use the library's sort function for this problem.
    k <= n
    Example
    Example1

    Input:
    [3,2,2,1,4]
    4
    Output:
    [1,2,2,3,4]
    Example2

    Input:
    [2,1,1,2,2]
    2
    Output:
    [1,1,2,2,2]
    Challenge
    A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory. Can you do it O(logk) using extra memory?
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        if not colors or len(colors) < 2:
            return
        self.sort(colors, 1, k, 0, len(colors) - 1)

    def sort(self, colors, color_from, color_to, index_from, index_to):
        # 递归出口 范围内只有1个颜色 或区间为1 无需继续排序
        if color_from == color_to or index_from == index_to:
            return
        # 递归分解 寻找中间色
        mid_color = (color_from + color_to) // 2
        # 分区 左边区域<=中间色 右边>中间色
        left, right = index_from, index_to
        while left <= right:
            while left <= right and colors[left] <= mid_color:
                left += 1
            while left <= right and colors[right] > mid_color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        self.sort(colors, color_from, mid_color, index_from, right)
        self.sort(colors, mid_color + 1, color_to, left, index_to)


```



## merge sort

- merge sort   T(N) = 2 T(N / 2)  + O(N) 递归解决左半 递归解决右半 合并左右
  - O(nlogn) best worst average 
  - O(n) space for temp array to store result (not in-place)
  - 先局部有序再整体有序 (先递归到左右两边 再合并)

```python
class Solution:
    """ https://www.lintcode.com/problem/merge-two-sorted-arrays/
    O(n) merge two separated sorted array with extra space
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        i, j, n, m = 0, 0, len(A) - 1, len(B) - 1
        res = []
        while i <= n and j <= m:
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            elif A[i] >= B[j]:
                res.append(B[j])
                j += 1
        if i >= n:
            res.extend(B[j:m + 1])

        if j >= m:
            res.extend(A[i:n + 1])
        return res
class Solution:
    """ merge sort (temp array initialization in-advance)
    https://www.jiuzhang.com/problem/merge-sort/
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):
        if not A:
            return A
        temp = [0] * len(A)
        # temp = [0 for _ in range(len(A))]
        self.merge_sort(A, 0, len(A) - 1, temp)

    def merge_sort(self, A, start, end, temp):
        if start >= end:
            return
        mid = (start + end) // 2
        self.merge_sort(A, start, mid, temp)
        self.merge_sort(A, mid + 1, end, temp)
        self.merge(A, start, end, temp)

    def merge(self, A, start, end, temp):
        # in-place merge left, right half
        mid = (start + end) // 2
        left, right = start, mid + 1
        index = start
        while left <= mid and right <= end:
            if A[left] < A[right]:
                temp[index] = A[left]
                index += 1
                left += 1
            else:
                temp[index] = A[right]
                index += 1
                right += 1
        while left <= mid:
            temp[index] = A[left]
            index += 1
            left += 1
        while right <= end:
            temp[index] = A[right]
            index += 1
            right += 1
        # 在每一次merge操作的最后，都把这段有序的数字从temp赋给a了
        for i in range(start, end + 1):
            A[i] = temp[i]
#
#
# a = [3,2,1,4,5]
# Solution().sortIntegers2(a)
# print(a)
```

### 相关问题

数逆序对个数 https://www.jiuzhang.com/problem/reverse-pairs/

- merge的过程中数横跨左右数组的逆序对 if A[left] > A[right] cnt += mid - left + 1;

```python
class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """
    def reversePairs(self, A):
        if not A:
            return 0
        temp = [0 for _ in range(len(A))]
        return self.merge_sort(A, 0, len(A) - 1, temp)
    
    def merge_and_count(self, A, start, end, cnt, temp):
        mid = (start + end) // 2
        left, right, index = start, mid + 1, start
        while left <= mid and right <= end:
            if A[left] > A[right]:
                temp[index] = A[right]
                right += 1
                # add count! left sublist中[left,mid] 都和right构成逆序对 批量计数
                cnt += mid - left + 1
            else:
                temp[index] = A[left]
                left += 1
            index += 1
        while left <= mid:
            temp[index] = A[left]
            left += 1
            index += 1
        while right <= end:
            temp[index] = A[right]
            right += 1
            index += 1
        # 在每一次merge操作的最后，都把这段有序的数字从temp赋回给原数组A
        for i in range(start, end + 1):
            A[i] = temp[i]
        return cnt

    def merge_sort(self, A, start, end, temp):
        if start >= end:
            return 0 # base case !
        mid = (start + end) // 2
        # 先递归数两边 再于merge环节中数横跨左右的  横跨左右逆序对判断条件为 = A[left] > A[right]
        left_count = self.merge_sort(A, start, mid, temp)
        right_count = self.merge_sort(A, mid + 1, end, temp)
        total_count = self.merge_and_count(A, start, end, left_count + right_count, temp)
        return total_count

# print(Solution().reversePairs([2,4,1,3,5]))
```



## 外排序和数组合并

外排序算法（External Sorting）
外排序算法是指在内存不够的情况下，如何对存储在一个或者多个大文件中的数据进行排序的算法。外排序算法通常是解决一些大数据处理问题的第一个步骤，或者是面试官所会考察的算法基本功。外排序算法是海量数据处理算法中十分重要的一块。
在学习这类大数据算法时，经常要考虑到内存、缓存、准确度等因素，这和我们之前见到的算法都略有差别

外排序算法分为两个基本步骤：

- 将大文件切分为若干个个小文件，并分别使用内存排好序
- 使用K路归并算法（k-way merge）将若干个排好序的小文件合并到一个大文件中

第一步：文件拆分
根据内存的大小，尽可能多的分批次的将数据 Load 到内存中，并使用系统自带的内存排序函数（或者自己写个快速排序算法），将其排好序，并输出到一个个小文件中。比如一个文件有1T，内存有1G，那么我们就这个大文件中的内容按照 1G 的大小，分批次的导入内存，排序之后输出得到 1024 个 1G 的小文件。

第二步：K路归并算法
K路归并算法使用的是数据结构堆（Heap）来完成的，使用 Java 或者 C++ 的同学可以直接用语言自带的 PriorityQueue（C++中叫priority_queue）来代替。

我们将 K 个文件中的第一个元素加入到堆里，假设数据是从小到大排序的话，那么这个堆是一个最小堆（Min Heap）。每次从堆中选出最小的元素，输出到目标结果文件中，然后如果这个元素来自第 x 个文件，则从第 x 个文件中继续读入一个新的数进来放到堆里，并重复上述操作，直到所有元素都被输出到目标结果文件中。

Follow up: 一个个从文件中读入数据，一个个输出到目标文件中操作很慢，如何优化？
如果我们每个文件只读入1个元素并放入堆里的话，总共只用到了 1024 个元素，这很小，没有充分的利用好内存。另外，单个读入和单个输出的方式也不是磁盘的高效使用方式。因此我们可以为输入和输出都分别加入一个缓冲（Buffer）。假如一个元素有10个字节大小的话，1024 个元素一共 10K，1G的内存可以支持约 100K 组这样的数据，那么我们就为每个文件设置一个 100K 大小的 Buffer， 每次需要从某个文件中读数据，都将这个 Buffer 装满。当然 Buffer 中的数据都用完的时候，再批量的从文件中读入。输出同理，设置一个 Buffer 来避免单个输出带来的效率缓慢。
那下面我们就来熟悉下两路归并和K路归并的算法

https://www.lintcode.com/problem/6/   2路归并排序

https://www.lintcode.com/problem/486/ k路归并



https://www.lintcode.com/problem/839/ merge 2 interval list

https://www.lintcode.com/problem/577/ merge k interval list



https://www.lintcode.com/problem/547/ intersection of 2 arrays

https://www.lintcode.com/problem/654/ sparse matrix multiplication

## 其他排序

- pancake sort (有可能会考~)
- sleep sort
- spaghetti sort
- bogo sort

#### move zeros

0丢到数组末尾 in place, minimize total# operations (一般理解为write operations)

https://www.lintcode.com/problem/539/

- 同向双指针 填充指针指向将被填充的非0位置 前移指针explorer 指向要被填充的非0数
- minimize write by not swapping & clear remaining with 0





# GROUP 4 二分



## 二分法模版

```java
// Java 版本
public class Solution {
    /**
     * @param A an integer array sorted in ascending order
     * @param target an integer
     * @return an integer
     */
    public int findPosition(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }

        int start = 0, end = nums.length - 1;
        // 要点1: start + 1 < end
        while (start + 1 < end) {
     // 要点2：start + (end - start) / 2
            int mid = start + (end - start) / 2;
            // 要点3：=, <, > 分开讨论，mid 不+1也不-1
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

        // 要点4: 循环结束后，单独处理start和end
        if (nums[start] == target) {
            return start;
        }
        if (nums[end] == target) {
            return end;
        }
        return -1;
    }
}

```



```python
# Python 版本
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        # 用 start + 1 < end 而不是 start < end 的目的是为了避免死循环
        # 在 first position of target 的情况下不会出现死循环
        # 但是在 last position of target 的情况下会出现死循环
        # 样例：nums=[1，1] target = 1
        # 为了统一模板，我们就都采用 start + 1 < end，就保证不会出现死循环
        while start + 1 < end:
            # python 没有 overflow 的问题，直接 // 2 就可以了
            # java和C++ 最好写成 mid = start + (end - start) / 2
            # 防止在 start = 2^31 - 1, end = 2^31 - 1 的情况下出现加法 overflow
            mid = (start + end) // 2

            # > , =, < 的逻辑先分开写，然后在看看 = 的情况是否能合并到其他分支里
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target: 
                end = mid
            elif nums[mid] == target:
                end = mid
            

        # 因为上面的循环退出条件是 start + 1 < end
        # 因此这里循环结束的时候，start 和 end 的invariant是相邻关系（1和2，3和4这种）
        # 因此需要再单独判断 start 和 end 这两个数谁是我们要的答案
        # 如果是找 first position of target 就先看 start，否则就先看 end
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1
```



如果你之前写过二分的题目，你会发现在二分问题中，最常见的错误就是死循环。而这个模版一定不会出现死循环。为什么呢？
因为我们这边使用了start + 1 < end, 而不是start < end 或者 start <= end
二分法的模板中，整个程序架构分为两个部分：
通过 while 循环，将区间范围从 n 缩小到 2 （只有 start 和 end 两个点）。
在 start 和 end 中判断是否有解。
而普通的start < end 或者 start <= end 在寻找目标最后一次出现的位置的时候，可能出现死循环。

有同学可能会问为什么明明可以 start = mid + 1 偏偏要写成 start = mid?
大部分时候，mid 是可以 +1 和 -1 的。在一些特殊情况下，比如寻找目标的最后一次出现的位置时，当 target 与 nums[mid] 相等的时候，是不能够使用 mid + 1 或者 mid - 1 的。因为会导致漏掉解。那么为了节省脑力，统一写成 start = mid / end = mid 并不会造成任何解的丢失，并且也不会损失效率——log(n) 和 log(n+1) 没有区别。

## 例题

https://www.lintcode.com/problem/classical-binary-search/

https://www.lintcode.com/problem/last-position-of-target/
```
# 相等时缩小左边界
elif nums[mid] == target:
    start = mid
# 先看end
```

https://www.lintcode.com/problem/first-position-of-target/

```
# 相等时缩小右边界
elif nums[mid] == target:
    end = mid
# 先看start
```

https://www.lintcode.com/problem/maximum-number-in-mountain-sequence/

```python
class Solution:
    """
    Description
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top(Maximum).

Arrays are strictly incremented, strictly decreasing

Example
Example 1:

Input: nums = [1, 2, 4, 8, 6, 3]
Output: 8
Example 2:

Input: nums = [10, 9, 8, 7],
Output: 10
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid + 1]:
                start = mid
            elif nums[mid] > nums[mid + 1]:
                end = mid
            elif nums[mid] == nums[mid + 1]:
                start = mid
        return max(nums[start], nums[end])

print(Solution().mountainSequence([1, 2, 4, 8, 6, 3]))
print(Solution().mountainSequence([10, 9, 8, 7]))
```

如果你解决了这道题，你会发现，二分问题其实并不需要要求数组一定是严格有序的，我们不能根据数组是否有序来判断是否是二分问题。
那我们该如何判断这个问题是否是二分问题呢？大家可以先思考一下。

不知道大家还记不记得，我们在上一节课就讲了一个判断算法的技巧——通过时间复杂度判断算法。在这里就能用到这个技巧。我们知道二分答案的时间复杂度是O(logn)的。所以当你发现有一个问题，用O(N)的时间复杂度非常好做，或者面试官说：“你给我优化一下这个算法。”那么你优化的思路就是优化到O(logn)，也就是尝试使用二分去做，这就是二分算法的判断条件

## Review

- 排序输入集二分

search a 2d matrix    https://www.lintcode.com/problem/28/

https://www.lintcode.com/problem/38/

因为每一次都会删除一行或者一列，在最坏的情况下，要从左下角一直找到右上角，付出的时间就是行的长度加上列的长度，也就是O(n+m)。

- 未排序输入集二分

https://www.lintcode.com/problem/600/

视频中的时间复杂度为O(n*logm + m*logn)，如果m与n相等的话，会变成2*n*logn，但是我们在计算时间复杂度的时候，是不考虑常数的系数的，所以正确的复杂度应该为O(n*logn)。

- 在答案集二分

https://www.lintcode.com/problem/437/

- 练习

https://www.lintcode.com/problem/1536/

能坚持做完题目的你很棒！在做完这些题目后，有没有总结出二分法的一些特征呢？
其实二分法可以被认为是将量级n压缩为量级logn的一种方法，比如最简单的二分查找有序数组中的数字，就是将O(n)复杂度变成了O(logn)，我们刚做完的矩阵查找，则是将 n * n 压缩成 n * logn。在很多时候，二分法都是一种很优美的查找技巧，比如C++中的upper_bound()，其内部就是使用二分法查找的。掌握了这个简单的技巧，一定能帮助你在面试中获得更多的解题灵感，助你先人一步。



# GROUP 5 Queue & interface abc

## 什么是队列（Queue）？

队列（queue）是一种采用先进先出（FIFO，first in first out）策略的抽象数据结构。比如生活中排队，总是按照先来的先服务，后来的后服务。队列在数据结构中举足轻重，其在算法中应用广泛，**最常用的就是在宽度优先搜索(BFS）中，记录待扩展的节点。**

队列内部存储元素的方式，一般有两种，数组（array）和链表（linked list）。两者的最主要区别是：

- 数组对随机访问有较好性能。
- 链表对插入和删除元素有较好性能。

### 用数组实现队列

在使用数组表示队列时，我们首先要创建一个长度为MAXSIZE的数组作为队列。

因为MAXSIZE是数组的长度，那MAXSIZE-1就是队列的最大下标了。

在队列中，除了用一组地址连续的存储单元依次存储从队首到队尾的元素外，还需要附设两个整型变量head和tail分别指示队首和队尾的位置。

我们主要介绍三个操作：

- 初始化队列
- `enqueue()`向队尾插入元素
- `dequeue()`删除并返回队首元素

每次元素入队时，tail向后移动；每次元素出队时，head向后移动。

我们可以将队列视作一个类，通过成员变量数组来表示一组地址连续的存储单元，再定义两个成员变量head和tail，将队列的基本操作定义成类的方法。（注意：为了将重点放在实现队列上，做了适当简化。示范队列仅支持整数类型，若想实现泛型，可用反射机制和object对象传参；此外，可多做安全检查并抛出异常）
java:

```java
public class MyQueue {
    public int head, tail;
    public int MAXSIZE = 100000;
    public int[] queue = new int[MAXSIZE];

    public MyQueue() {
        head = tail = 0;
        // do initialize if necessary
    }

    public void enqueue(int item) {      
        // 队列已满
        if(tail == MAXSIZE){
            return ;
        }

        queue[tail++] = item;
    }

    public int dequeue() {
        // 队列为空
        if (head == tail){
            return -1;
        }

        return queue[head++];      
    }
}
```

python:

```python
class MyQueue(object):

    def __init__(self):
        # do some intialize if necessary
        self.MAXSIZE = 4
        self.queue = [0] * self.MAXSIZE
        self.head, self.tail = 0, 0

    # @param {int} item an integer
    # @return nothing
    def enqueue(self, item):
        queue = self.queue 

        # 队列满 
        if self.tail == self.MAXSIZE:
            return 

        queue[self.tail] = item 
        self.tail += 1 


    # @return an integer
    def dequeue(self):
        queue = self.queue 

        ## 队列为空
        if self.head == self.tail:
            return -1 

        item = queue[self.head]
        self.head += 1 
        return item 
```

但是大家会发现，如果这样实现队列的话，我们考虑MAXSIZE为4的情况，如果我们采取下面的操作

```
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
dequeue()
dequeue()
```

结束后数组的状态时[^, ^, 3, 4], head = 2, tail = 4。（'^'表示该位置为空，即当前元素已经出队）
从我们之前的判断来看，`tail == MAXSIZE` , 当前队列已经满了，不能继续添加元素了，但是实际上我们还可以继续添加元素。因此在使用数组实现队列时，可能会出现空间未有效利用的情况，因此，我们有两种解决方法：

1. 使用链表来实现队列
2. 使用数组来实现循环队列

那么我们就先来看用链表来实现队列的方法：

### 用链表实现队列

链表是由多个节点构成的，一个节点由两部分组成:一个是数据域,一个是指针域.
链表分为:单链表(只能是父节点引用子节点),双链表(相邻的节点可相互引用),循环链表(在双链表的基础上,头尾节点可相互引用).
实现链表,就是在链表里加入节点,使用节点的引用域使节点之间形成连接,可相互调用.
链表队列的实现原理:首先定义一个节点类,节点类包含引用域和数据域.然后定义一个链表类,链表类形成节点间的引用关系.

我们主要介绍三个操作：

- 初始化队列
- `enqueue()`向队尾插入元素
- `dequeue()`删除并返回队首元素

在队列中，我们只要用两个指针head和tail分别指向链表的头部和尾部即可实现基本队列功能

java:

```java
class Node {
    public int val;
    public Node next;
    public Node(int _val) {
        val = _val;
        next = null;
    }
}

public class MyQueue {
    public Node head, tail;

    public MyQueue() {
        head = tail = null;
        // do initialize if necessary
    }

    public void enqueue(int item) {
        if (head == null) {
            tail = new Node(item);
            head = tail;        
        } else {
            tail.next = new Node(item);
            tail = tail.next;
        }
    }

    public int dequeue() {
        if (head != null) {
            int item = head.val;
            head = head.next;
            return item;
        }
        return -1;
    }
}
```

puthon:

```python
class Node():
    def __init__(self, _val):
        self.next = None
        self.val = _val

class MyQueue(object):

    def __init__(self):
        # do some intialize if necessary
        self.head, self.tail = None, None

    # @param {int} item an integer
    # @return nothing
    def enqueue(self, item):
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    # @return an integer
    def dequeue(self):
        if self.head is not None:
            item = self.head.val
            self.head = self.head.next
            return item
        return -1
```

可以发现链表可以轻松地避免“假溢出”的问题，因为在每次需要新增元素时，只需要新建一个ListNode就可以了。 当然，我们也可以用循环队列来解决这个问题，接下来我们就来看一下循环队列如何实现队列。
### 用循环队列实现队列

队列是一种先进先出的线性表，它只允许在表的一端进行插入，而在另一端删除元素。允许插入的一端称为队尾，允许删除的一端称为队首。但是我们之前也提到了，数组实现的队列会导致“虽然数组没满，但是tail已经指向了数组末尾，返回数组已满，队列溢出的错误信号”，我们称之为“假溢出”。

为充分利用向量空间，克服"假溢出"现象的方法是：将向量空间想象为一个首尾相接的圆环，并称这种向量为循环向量。存储在其中的队列称为循环队列（Circular Queue）。循环队列是把顺序队列首尾相连，把存储队列元素的表从逻辑上看成一个环，成为循环队列。

我们主要介绍三个操作：

- 初始化循环队列
- `enqueue()`向队尾插入元素
- `dequeue()`删除并返回队首元素

在循环队列中，除了用一组地址连续的存储单元依次存储从队首到队尾的元素外，还需要附设两个整型变量head和tail分别指示队首和队尾的位置。

我们可以将循环队列视作一个类，通过成员变量数组来表示一组地址连续的存储单元，再定义两个成员变量head和tail，将循环队列的基本操作定义成类的方法，循环效果则用“模”运算实现，以此来实现循环队列。

每当tail到达末尾的时候，将tail对MAXSIZE取模，使其回到队首。但是如果这样我们会发现一个问题，队列为空和队列已满的条件都成了tail == head。

为了避免这种无法判断的情况，我们规定当循环队列只剩一个空位的时候，就认为队列已满。这样队列已满的条件就成了 `(tail + 1) % MAXSIZE == head`。

java:

```java
public class MyQueue {
    public int head, tail;
    public int SIZE = 4;
    public int[] queue = new int[SIZE];

    public MyQueue() {
        head = tail = 0;
        // do initialize if necessary
    }
    //压入一个元素
    public void enqueue(int item) {
        // 队列已满
        if ((tail + 1) % SIZE == head){
            return ;
        }

        queue[tail++] = item;
        tail %= SIZE;
    }
    //弹出一个元素
    public int dequeue() {
        // 队列为空
        if (head == tail){
            return -1;
        }

        int item = queue[head++];
        head %= SIZE;
        return item;

    }
}
```

python:

```python
class MyQueue(object):

    def __init__(self):
        # do some intialize if necessary
        self.SIZE = 100000
        self.queue = [0] * self.SIZE
        self.head, self.tail = 0, 0

    # @param {int} item an integer
    # @return nothing
    # 压入队列
    def enqueue(self, item):
        queue = self.queue 

        # 队列满 
        if (self.tail + 1) % self.SIZE == self.head:
            return 

        queue[self.tail] = item 
        self.tail = (self.tail + 1) % self.SIZE


    # @return an integer
    # 弹出元素
    def dequeue(self):
        queue = self.queue 

        ## 队列为空
        if self.head == self.tail:
            return -1 

        item = queue[self.head]
        self.head = (self.head + 1) % self.SIZE
        return item 
```

### 算法面试中不需要自己实现队列

如果不是题目要求实现一个队列，我们都可以使用语言自带的队列数据结构，因为这些题目，面试官并不是想考察你是否能够实现队列，而是想考察其他的算法，如果现场实现队列，时间可能会不够。

比如在Java中我们就可以调用Queue接口来实现队列，给我们的代码带来许多便利。那接口到底是什么呢，我们一起来学习一下吧。

（这部分是Java语言专属的特性，其他语言的同学可以跳过）

接下来我们来学习一下Java的接口（Interface），其他语言的同学可以跳过这一部分。

Java接口(Interface)是一系列方法的声明，是一些方法特征的集合，一个接口只有方法的特征没有方法的实现，因此这些方法可以在不同的地方被不同的类实现，而这些实现可以具有不同的行为。打一个比方，接口好比一个戏中的角色，这个角色有一些特定的属性和操作，然后实现接口的类就好比扮演这个角色的人，一个角色可以由不同的人来扮演，而不同的演员之间除了扮演一个共同的角色之外，并不要求其它的共同之处。

#### Java面试常用的Interface

##### Set

Set注重独一无二,该体系集合可以知道某物是否已经存在于集合中,不会存储重复的元素。Set的实现类在面试中常用的是：**HashSet** 与 **TreeSet**

- HashSet
  - 无重复数据
  - 可以有空数据
  - 数据无序

```java
Set<String> set = new HashSet<>();
for (int i = 1; i < 6; i ++) {
	set.add(i + "");
}
set.add("1"); //不会重复写入数据
set.add(null);//可以写入空数据
Iterator<String> iter = set.iterator();
while (iter.hasNext()) {
	system.out.print(iter.next() + " ");//数据无序 
}// 输出(无序)为 3 4 1 5 null 2
```

- TreeSet
  - 无重复数据
  - 不能有空数据
  - 数据有序

```java
Set<String> set = new TreeSet<>();
for (int i = 1; i < 6; i ++) {
	set.add(i + "");
}
set.add("1"); //不会重复写入数据
//set.add(null);//不可以写入空数据
Iterator<String> iter = set.iterator();
while (iter.hasNext()) {
	system.out.print(iter.next() + " ");//数据有序
}// 输出(有序)为 1 2 3 4 5
```



##### Map

Map用于存储具有映射关系的数据。Map中存了两组数据(key与value),它们都可以是任何引用类型的数据，key不能重复，我们可以通过key取到对应的value。Map的实现类在面试中常用是：**HashMap** 和 **TreeMap**.

- HashMap
  - key 无重复，value 允许重复
  - 允许 key 和 value 为空
  - 数据无序

```java
public class Solution {
    public static void main(String[] args){
        Map<String, String> map = new HashMap<>();
        for (int i = 5; i > 0; i --) {
            map.put(i + "", i + "");
        }
        map.put("1","1");//key无重复
        map.put("11","1");//value可以重复
        map.put(null, null);//可以为空
        for (Iterator i = map.keySet().iterator(); i.hasNext(); ) {
            String key = (String)i.next();
            String value = map.get(key);
            System.out.println("key = " + key + ", value = " + value);
        }
    }
}
//输出
/*
key = 11, value = 1
key = null, value = null
key = 1, value = 1
key = 2, value = 2
key = 3, value = 3
key = 4, value = 4
key = 5, value = 5
*/
//输出顺序与输入顺序无关
```

- TreeMap
  - key 无重复，value 允许重复
  - 不允许有null
  - 有序(存入元素的时候对元素进行自动排序，迭代输出的时候就按排序顺序输出)

```java
public class Solution {
    public static void main(String[] args){
        Map<String, String> map = new TreeMap<>();
        for (int i = 5; i > 0; i --) {
            map.put(i + "", i + "");
        }
        map.put("1","1");//key无重复
        map.put("11","1");//value可以重复
        //map.put(null, null);//不可以为空
        for (Iterator i = map.keySet().iterator(); i.hasNext(); ) {
            String key = (String)i.next();
            String value = map.get(key);
            System.out.println("key = " + key + ", value = " + value);
        }
    }
}
//输出
/*
key = 1, value = 1
key = 11, value = 1
key = 2, value = 2
key = 3, value = 3
key = 4, value = 4
key = 5, value = 5
*/
//输出顺序位String排序后的顺序
```

##### List

一个 List 是一个元素有序的、可以重复(这一点与Set和Map不同)、可以为 null 的集合，List的实现类在面试中常用是：**LinkedList** 和 **ArrayList**

- LinkedList
  - 基于链表实现
- ArrayList
  - 基于动态数组实现
- LinkedList 与 ArrayList 对比：
  - 对于随机访问get和set，ArrayList绝对优于LinkedList，因为LinkedList要移动指针
  - 对于新增和删除操作add和remove，在已经得到了需要新增和删除的元素位置的前提下，LinkedList可以在O(1)的时间内删除和增加元素，而ArrayList需要移动`增加或删除元素之后的所有元素`的位置，时间复杂度是O(n)的，因此LinkedList优势较大

##### Queue

队列是一种比较重要的数据结构，它支持FIFO(First in First out)，即尾部添加、头部删除（先进队列的元素先出队列），跟我们生活中的排队类似。

- PriorityQueue
  - 基于堆(heap)实现
  - 非FIFO(最先出队列的是优先级最高的元素)
- 普通 Queue
  - 基于链表实现
  - FIFO



# GROUP 6 Hashtable

欢迎来到『九章算法班 2021 版』的第18节课，今天我们一起来学习『哈希表的原理』

在本章中，我们将深入学习哈希表这种数据结构，主要讲解哈希表原理、冲突、扩容的相关知识，希望同学认真学习。

本章关键字：Hash（哈希）。

- hashmap vs hashset

首先得看java最基本的两种数据结构：数组和链表的区别：

数组易于快速读取（通过for循环），不便存储（数组长度有限制）；链表易于存储，不易于快速读取。

**哈希表的出现是为了解决链表访问不快速的弱点，哈希表也称散列表**。

HashSet是通过HashMap来实现的，HashMap的输入参数有Key、Value两个组成，在实现HashSet的时候，保持HashMap的Value为常量，相当于在HashMap中只对Key对象进行处理。

HashMap的底层是一个数组结构，数组中的每一项对应了一个链表，这种结构称“链表散列”的数据结构，即数组和链表的结合体；也叫散列表、哈希表。

想要了解HashMap和HashSet这样两个不同存储结构的区别，就得熟知他们的存储过程

**一、HashMap存储对象的过程**

1、对HashMap的Key调用hashCode()方法，返回int值，即对应的hashCode；

2、把此hashCode作为哈希表的索引，查找哈希表的相应位置，若当前位置内容为NULL，则把HashMap的Key、Value包装成Entry数组，放入当前位置；

3、若当前位置内容不为空，则继续查找当前索引处存放的链表，利用equals方法，找到Key相同的Entry数组，则用当前Value去替换旧的Value；

4、若未找到与当前Key值相同的对象，则把当前位置的链表后移（Entry数组持有一个指向下一个元素的引用），把新的Entry数组放到链表表头；

**二、HashSet存储对象的过程**

往HashSet添加元素的时候，HashSet会先调用元素的hashCode方法得到元素的哈希值 ，

然后通过元素 的哈希值经过移位等运算，就可以算出该元素在哈希表中 的存储位置。

情况1： 如果算出元素存储的位置目前没有任何元素存储，那么该元素可以直接存储到该位置上。

情况2： 如果算出该元素的存储位置目前已经存在有其他的元素了，那么会调用该元素的equals方法与该位置的元素再比较一次

，如果equals返回的是true，那么该元素与这个位置上的元素就视为重复元素，不允许添加，如果equals方法返回的是false，那么该元素运行添加。

**答案总结：HashSet和HashMap的区别**

| HashMap                          | HashSet                                                      |
| -------------------------------- | ------------------------------------------------------------ |
| 实现了Map接口                    | 实现Set接口                                                  |
| 存储键值对                       | 仅存储对象                                                   |
| 调用put（）向map中添加元素       | 调用add（）方法向Set中添加元素                               |
| HashMap使用键（Key）计算Hashcode | HashSet使用成员对象来计算hashcode值，对于两个对象来说hashcode可能相同，所以equals()方法用来判断对象的相等性，如果两个对象不同的话，那么返回false |

哈希表（Java 中的 HashSet / HashMap，C++ 中的 unordered_map，Python 中的 dict）是面试中非常常见的数据结构。它的主要考点有两个：
1.是否会灵活的使用哈希表解决问题
2.是否熟练掌握哈希表的基本原理

HashSet实现了Set接口，其内部不允许出现重复的值，如果我们将一个对象存入HashSet，必须重写equals()和hashCode()方法，这样才能确保集合中不存在同一个元素。HashSet的内部是无序的，因此不能使用 hashset.get(index) 来获取元素。
HashMap实现了Map接口，其内容是键值对的映射（key->value），不允许出现相同的键（key）。在查询的时候会根据给出的键来查询对应的值。
我们可以认为，HashSet和HashMap增查操作的时间复杂度都是常数级的。
下面就请一起跟着老师学习哈希的基础知识

冲突（Collision），是说两个不同的 key 经过哈希函数的计算后，得到了两个相同的值。解决冲突的方法，主要有两种：

1. 开散列法（Open Hashing）。是指哈希表所基于的数组中，每个位置是一个 Linked List 的头结点。这样冲突的 <key, value> 二元组，就都放在同一个链表中。
2. 闭散列法（Closed Hashing）。是指在发生冲突的时候，后来的元素，往下一个位置去找空位。

https://www.lintcode.com/problem/hash-function/

https://www.lintcode.com/problem/rehashing/

# GROUP 7 Divide and Conquer, Tree

## BST增删查改

本章关键字：Divide and Conquer（分治法），BST（Binary Search Tree，二叉查找树）

https://www.lintcode.com/problem/11/

https://www.lintcode.com/problem/689/

https://www.lintcode.com/problem/701/

### 什么是二叉搜索树(Binary Search Tree)

二叉搜索树可以是一棵空树或者是一棵满足下列条件的二叉树:

- 如果它的左子树不空，则左子树上所有节点值均小于它的根节点值。
- 如果它的右子树不空，则右子树上所有节点值均大于它的根节点值。
- 它的左右子树均为二叉搜索树(BST)。
- 严格定义下BST中是没有值相等的节点的(No duplicate nodes)。
  根据上述特性，我们可以得到一个结论：BST中序遍历得到的序列是升序的。

### BST基本操作——增删改查(CRUD)

对于树节点的定义如下：
Java:

```java
class TreeNode{
	int val;
	TreeNode left;
	TreeNode right;
	pubic TreeNode(int val) {
		this.val = val;
		this.left = this.right = null;
	}
}
```

Python:

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
```

### 基本操作之查找(Retrieve)

#### 思路

查找值为val的节点，如果val小于根节点则在左子树中查找，反之在右子树中查找

#### 代码实现

Java:

```java
public TreeNode searchBST(TreeNode root, int val) {
	if (root == null) {
		return null;
	}// 未找到值为val的节点
	if (val < root.val) {
		return searchBST(root.left, val);//val小于根节点值，在左子树中查找
	} else if (val > root.val) {
		return searchBST(root.right, val);//val大于根节点值，在右子树中查找
	} else {
		return root;//找到了
	}
}
```

Python:

```python
def searchBST(root, val):
    if not root:
        return None # 未找到值为val的节点
    if val < root.val:
        return searchBST(root.left, val) # val小于根节点值，在左子树中查找哦
    elif val > root.val:
        return searchBST(root.right, val) # val大于根节点值，在右子树中查找
    else:
        return root
        
```



### 基本操作之修改(Update)

#### 思路

修改仅仅需要在查找到需要修改的节点之后，更新这个节点的值就可以了，(假如修改过后整棵树还满足BST的性质)

#### 代码实现

Java:

```java
public void updateBST(TreeNode root, int target, int val) {
	if (root == null) {
		return;
	}// 未找到target节点
	if (target < root.val) {
		updateBST(root.left, target, val);//target小于根节点值，在左子树中查找
	} else if (target > root.val) {
		updateBST(root.right, target, val);//target大于根节点值，在右子树中查找
	} else { //找到了
		root.val = val;
	}
}
```

Python:

```python
def updateBSTBST(root, target, val):
    if not root:
        return  # 未找到target节点
    if target < root.val:
        updateBST(root.left, target, val) # target小于根节点值，在左子树中查找哦
    elif target > root.val:
        updateBST(root.right, target, val) # target大于根节点值，在右子树中查找
    else:  # 找到了
        root.val = val
```





### 基本操作之增加(Create)

#### 思路

- 根节点为空，则待添加的节点为根节点
- 如果待添加的节点值小于根节点，则在左子树中添加
- 如果待添加的节点值大于根节点，则在右子树中添加
- 我们统一在树的叶子节点(Leaf Node)后添加

#### 代码实现

Java:

```java
public TreeNode insertNode(TreeNode root, TreeNode node) {
    if (root == null) {
        return node;
    }
    if (root.val > node.val) {
        root.left = insertNode(root.left, node);
    } else {
        root.right = insertNode(root.right, node);
    }
    return root;
}
```

Python:

```python
def insertNode(root, node):
    if not root:
        return node
    if root.val > node.val:
        root.left = insertNode(root.left, node)
    else:
        root.right = insertNode(root.right, node)
    return root
```



### 基本操作之删除(Delete)

#### 思路(最为复杂)

- 考虑待删除的节点为叶子节点，可以直接删除并修改父亲节点(Parent Node)的指针，需要区分待删节点是否为根节点
- 考虑待删除的节点为单支节点(只有一棵子树——左子树 or 右子树)，与删除链表节点操作类似，同样的需要区分待删节点是否为根节点
- 考虑待删节点有两棵子树，可以将待删节点与左子树中的最大节点进行交换，由于左子树中的最大节点一定为叶子节点，所以这时再删除待删的节点可以参考第一条
  详细的解释可以看 http://www.algolist.net/Data_structures/Binary_search_tree/Removal

#### 代码实现

Java:

```java
public TreeNode removeNode(TreeNode root, int value) {
    TreeNode dummy = new TreeNode(0);
    dummy.left = root;
    TreeNode parent = findNode(dummy, root, value);
    TreeNode node;
    if (parent.left != null && parent.left.val == value) {
        node = parent.left;
    } else if (parent.right != null && parent.right.val == value) {
        node = parent.right;
    } else {
        return dummy.left;
    }
    deleteNode(parent, node);
    return dummy.left;
}

private TreeNode findNode(TreeNode parent, TreeNode node, int value) {
    if (node == null) {
        return parent;
    }
    if (node.val == value) {
        return parent;
    }
    if (value < node.val) {
        return findNode(node, node.left, value);
    } else {
        return findNode(node, node.right, value);
    }
}

private void deleteNode(TreeNode parent, TreeNode node) {
    if (node.right == null) {
        if (parent.left == node) {
            parent.left = node.left;
        } else {
            parent.right = node.left;
        }
    } else {
        TreeNode temp = node.right;
        TreeNode father = node;
        while (temp.left != null) {
            father = temp;
            temp = temp.left;
        }
        if (father.left == temp) {
            father.left = temp.right;
        } else {
            father.right = temp.right;
        }
        if (parent.left == node) {
            parent.left = temp;
        } else {
            parent.right = temp;
        }
        temp.left = node.left;
        temp.right = node.right;
    }
}
```

Python:

```python
def removeNode(root, value):
    dummy = TreeNode(0)
    dummy.left = root
    parent = findNode(dummy, root, value)
    node = None
    if parent.left and parent.left.val == value:
        node = parent.left
    elif parent.right and parent.right.val == value:
        node = parent.right
    else:
        return dummy.left
    deleteNode(parent, node)
    return dummy.left

def findNode(parent, node, value):
    if not node:
        return parent
    if node.val == value:
        return parent
    if value < node.val:
        return findNode(node,node.left, value)
    else:
        return findNode(node, node.right, value)

def deleteNode(parent, node):
    if not node.right:
        if parent.left == node:
            parent.left = node.left
        else:
            parent.right = node.left
    else:
        temp = node.right
        father = node
        while temp.left:
            father = temp
            temp = temp.left
        if father.left == temp:
            father.left = temp.right
        else:
            father.right = temp.right
        if parent.left == node:
            parent.left = temp
        else:
            parent.right = temp
        temp.left = node.left
        temp.right = node.right
        
```



## 二叉树中序遍历非递归实现

- BST中最小的节点是从根节点一直往左走遇见的叶子节点，它不一定在树的最底层；BST的特征就是中序遍历是严格递增的，所以D是错误的；如果这颗BST是一条链，那么找到最小值节点的算法是O(n)的，除非这个BST是一个满二叉树，所以C是错误的。

https://www.lintcode.com/problem/binary-search-tree-iterator/

https://www.lintcode.com/problem/closest-binary-search-tree-value/

https://www.lintcode.com/problem/closest-binary-search-tree-value-ii/

## 非递归后序遍历 & morris traversal

在第13章的学习中，我们掌握了如何使用非递归形式获得二叉树的前序、中序遍历。而在这节课中，我们将继续使用非递归形式求出二叉树的后序遍历。然后我们将学习另外一类遍历二叉树的算法——Morris算法。

本章关键字：前序遍历（Preorder Traversal），中序遍历（Inorder Traversal），后序遍历（Postorder Traversal）。

与前序、中序的非递归方式相同，二叉树的非递归后序遍历也需要借助栈来完成，遍历顺序为左、右、根

大致思路如下：
1、如果根节点非空，将根节点加入到栈中。
2、如果栈不空，取栈顶元素（暂时不弹出），
a.如果（左子树已访问过或者左子树为空），且（右子树已访问过或右子树为空），则弹出栈顶节点，将其值加入数组，
b.如果左子树不为空，且未访问过，则将左子节点加入栈中，并标左子树已访问过。
c.如果右子树不为空，且未访问过，则将右子节点加入栈中，并标右子树已访问过。
3、重复第二步，直到栈空。

https://www.lintcode.com/problem/68/

java版本：

```java
public ArrayList<Integer> postorderTraversal(TreeNode root) {
    ArrayList<Integer> result = new ArrayList<Integer>();
    Stack<TreeNode> stack = new Stack<TreeNode>();
    TreeNode prev = null; // previously traversed node
    TreeNode curr = root;
    if (root == null) {
        return result;
    }

    stack.push(root);
    while (!stack.empty()) {
        curr = stack.peek();
        if (prev == null || prev.left == curr || prev.right == curr) { // traverse down the tree
            if (curr.left != null) {
                stack.push(curr.left);
            } else if (curr.right != null) {
                stack.push(curr.right);
            }
        } else if (curr.left == prev) { // traverse up the tree from the left
            if (curr.right != null) {
                stack.push(curr.right);
            }
        } else { // traverse up the tree from the right
            result.add(curr.val);
            stack.pop();
        }
        prev = curr;
    }
    return result;
}
```

python版本

```python
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        result = []
        stack = []
        prev, curr = None, root

        if not root:
            return result

        stack.append(root)
        while len(stack) > 0:
            curr = stack[-1]
            if not prev or prev.left == curr or prev.right == curr:  # traverse down the tree
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
            elif curr.left == prev:  # traverse up the tree from the left
                if curr.right:
                    stack.append(curr.right)
            else:  # traverse up the tree from the right
                result.append(curr.val)
                stack.pop()
            prev = curr

        return result
```

### 什么是 Morris 算法

与递归和使用栈空间遍历的思想不同，Morris 算法使用二叉树中的叶节点的right指针来保存后面将要访问的节点的信息，当这个right指针使用完成之后，再将它置为null，但是在访问过程中有些节点会访问两次，所以与递归的空间换时间的思路不同，Morris则是使用时间换空间的思想。

#### 节点定义

Java:

```java
class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    pubic TreeNode(int val) {
        this.val = val;
        this.left = this.right = null;
    }
}
```

Python:

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
```

可以尝试用morris traversal进行前中后序遍历

https://www.lintcode.com/problem/66/

https://www.lintcode.com/problem/67/

https://www.lintcode.com/problem/68/



![Morris1](https://raw.githubusercontent.com/th2zz/typora_img_host/master/img/Morris1.jpeg)

### 用 Morris 算法进行中序遍历(Inorder Traversal)

#### 思路

1. 如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。
2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
   1. 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。
   2. 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空（恢复树的形状）。输出当前节点。当前节点更新为当前节点的右孩子。
3. 重复1、2两步直到当前节点为空。

上图为每一步迭代的结果（从左至右，从上到下），cur代表当前节点，深色节点表示该节点已输出。

#### 示例代码

Java:

```java
public class Solution {
    /**
     * @param root: A Tree
     * @return: Inorder in ArrayList which contains node values.
     */

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> nums = new ArrayList<>();
        TreeNode cur = null;

        while (root != null) {
            if (root.left != null) {
                cur = root.left;
                while (cur.right != null && cur.right != root) {
                    cur = cur.right;
                }

                if (cur.right == root) {
                    nums.add(root.val);
                    cur.right = null;
                    root = root.right;
                } else {
                    cur.right = root;
                    root = root.left;
                }               
            } else {
                nums.add(root.val);
                root = root.right;
            }
        }

        return nums;
    } 

}
```

Python:

```python
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        nums = []
        cur = None
    
        while root:
            if root.left:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right
                
                if cur.right == root:
                    nums.append(root.val)
                    cur.right = None
                    root = root.right
                else:
                    cur.right = root
                    root = root.left
            else:
                nums.append(root.val)
                root = root.right
                
        return nums
        
```

![Morris2](https://raw.githubusercontent.com/th2zz/typora_img_host/master/img/Morris2.jpeg)



### 用 Morris 算法实现先序遍历(Preorder Traversal)

#### 思路

1. 如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。
2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
   1. 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。**输出当前节点**（与中序遍历唯一一点不同）。当前节点更新为当前节点的左孩子。
   2. 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空。当前节点更新为当前节点的右孩子。
3. 重复1、2两步直到当前节点为空。

#### 示例代码

Java:

```java
public class Solution {
    /**
     * @param root: A Tree
     * @return: Preorder in ArrayList which contains node values.
     */
    public List<Integer> preorderTraversal(TreeNode root) {
        // morris traversal
        List<Integer> nums = new ArrayList<>();
        TreeNode cur = null;
        while (root != null) {
            if (root.left != null) {
                cur = root.left;
                // find the predecessor of root node
                while (cur.right != null && cur.right != root) {
                    cur = cur.right;
                }
                if (cur.right == root) {
                    cur.right = null;
                    root = root.right;
                } else {
                    nums.add(root.val);
                    cur.right = root;
                    root = root.left;
                }
            } else {
                nums.add(root.val);   
                root = root.right;
            }
        }
        return nums;
    } 
}
```

Python:

```python
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        nums = []
        cur = None
        
        while root:
            if root.left:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right
                if cur.right == root:
                    cur.right = None
                    root = root.right
                else:
                    nums.append(root.val)
                    cur.right = root
                    root = root.left
            else:
                nums.append(root.val)
                root = root.right
                
        return nums
```

### 用 Morris 算法实现后序遍历(Postorder Traversal)

#### 思路

后序遍历其实可以看作是和前序遍历左右对称的，此处，我们同样可以利用这个性质，基于前序遍历的算法，可以很快得到后序遍历的结果。我们只需要将前序遍历中所有的左孩子和右孩子进行交换就可以了。

#### 示例代码

Java:

```java
public class Solution {
    /**
     * @param root: A Tree
     * @return: Postorder in ArrayList which contains node values.
     */
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> nums = new ArrayList<>();
        TreeNode cur = null;
        while (root != null) {
            if (root.right != null) {
                cur = root.right;
                while (cur.left != null && cur.left != root) {
                    cur = cur.left;
                }
                if (cur.left == root) {
                    cur.left = null;
                    root = root.left;
                } else {
                    nums.add(root.val);
                    cur.left = root;
                    root = root.right;
                }
            } else {
                nums.add(root.val);
                root = root.left;
            }
        }
        Collections.reverse(nums);
        return nums;
    } 
}
```

Python:

```python
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        nums = []
        cur = None

        while root:
            if root.right != None:
                cur = root.right
                while cur.left and cur.left != root:
                    cur = cur.left
                if cur.left == root:
                    cur.left = None
                    root = root.left
                else:
                    nums.append(root.val)
                    cur.left = root
                    root = root.right
            else:
                nums.append(root.val)
                root = root.left
                
        nums.reverse()
        return nums
        
```



# GROUP 8 HEAP

这一章我们来学习“堆”的相关知识。堆(Heap)是一种重要的数据结构，是实现优先队列(Priority Queues)首选的数据结构。堆有很多种变体，包括二项式堆、斐波那契堆等，但是这里只考虑最常见的二叉堆。

本章关键字：Heap（堆），Priority Queues（优先队列）。

堆是一棵满足如下性质的二叉树：
1、父节点的键值总是不大于它的孩子节点的键值（小顶堆）。
2、父节点的键值总是不小于它的孩子节点的键值（大顶堆）。
由于堆是一棵形态规则的二叉树，因此堆的父节点和孩子节点存在如下关系（根节点编号为0）：
设父节点的编号为 i, 则其左孩子节点的编号为2*i+1, 右孩子节点的编号为2*i+2
设孩子节点的编号为i, 则其父节点的编号为(i-1)/2
由于上面的性质，父节点一定比他的儿节点小（大），所以整个树的树根的值一定是最小（最大）的，那么我们就能在O(1)的时间内，获得整个堆的极值。
现在有没有发现堆和我们曾经遇到过的优先队列具有很相似的特点，那么二者究竟有何联系呢？

优先队列是一种抽象的数据类型，它和堆的关系类似于，List和数组、链表的关系一样；我们常常使用堆来实现优先队列，因此很多时候堆和优先队列都很相似，它们只是概念上的区分。
优先队列的应用场景十分的广泛，常见的应用有：

- Dijkstra’s algorithm（单源最短路问题中需要在邻接表中找到某一点的最短邻接边，这可以将复杂度降低。）
- Huffman coding（贪心算法的一个典型例子，采用优先队列构建最优的前缀编码树(prefixEncodeTree)）
- Prim’s algorithm for minimum spanning tree

在java，python中都已经有封装了的Priority Queue(Heaps)
优先队列是一个至少能够提供插入（Insert）和删除最小（DeleteMin）这两种操作的数据结构。对应于队列的操作，Insert相当于Enqueue，DeleteMin相当于Dequeue。
用堆实现优先的过程中，需要注意最大堆只能对应最大优先队列，最小堆则是对应最小优先队列。

现在我们借助下面的问题，来理解shiftup和shiftdown的思想。
给定一个数组A[]，我们的目的是要将 A[] 堆化，也就是让A[]满足以下要求：

- A[i * 2 + 1] >= A[i]
- A[i * 2 + 2] >= A[i]

基于 shiftup的版本 O(nlogn)
Java版本：

```java
public class Solution {
    /**
     * @param A: Given an integer array
     * @return: void
     */
    private void siftup(int[] A, int k) {
        while (k != 0) {
            int father = (k - 1) / 2;
            if (A[k] > A[father]) {
                break;
            }
            int temp = A[k];
            A[k] = A[father];
            A[father] = temp;
            
            k = father;
        }
    }
    
    public void heapify(int[] A) {
        for (int i = 0; i < A.length; i++) {
            siftup(A, i);
        }
    }
}
```

Python版本：

```python
class Solution:
    # @param A: Given an integer array
    # @return: void
    def siftup(self, A, k):
        while k != 0:
            father = (k - 1) // 2
            if A[k] > A[father]:
                break
            A[k], A[father] = A[father], A[k]
            k = father
            
    def heapify(self, A):
        for i in range(len(A)):
            self.siftup(A, i)
```

算法思路：
对于每个元素A[i]，比较A[i]和它的父亲结点的大小，如果小于父亲结点，则与父亲结点交换。
交换后再和新的父亲比较，重复上述操作，直至该点的值大于父亲。
时间复杂度分析：
对于每个元素都要遍历一遍，这部分是 O(n)
每处理一个元素时，最多需要向根部方向交换 logn次。
因此总的时间复杂度是 O(nlogn)

除了上面的代码，我们也可以使用更有效率的O(n)的算法。
基于 Siftdown 的版本 O(n)
Java版本：

```
public class Solution {
    /**
     * @param A: Given an integer array
     * @return: void
     */
    private void siftdown(int[] A, int k) {
        while (k * 2 + 1 < A.length) {
            int son = k * 2 + 1;   // A[i] 的左儿子下标。
            if (k * 2 + 2 < A.length && A[son] > A[k * 2 + 2])
                son = k * 2 + 2;     // 选择两个儿子中较小的。
            if (A[son] >= A[k])      
                break;
            
            int temp = A[son];
            A[son] = A[k];
            A[k] = temp;
            k = son;
        }
    }
    
    public void heapify(int[] A) {
        for (int i = (A.length - 1) / 2; i >= 0; i--) {
            siftdown(A, i);
        }
    }
}
```

Python版本：

```
import sys
import collections
class Solution:
    # @param A: Given an integer array
    # @return: void
    def siftdown(self, A, k):
        while k * 2 + 1 < len(A):
            son = k * 2 + 1    #A[i]左儿子的下标
            if k * 2 + 2 < len(A) and A[son] > A[k * 2 + 2]:
                son = k * 2 + 2    #选择两个儿子中较小的一个
            if A[son] >= A[k]:
                break
                
            temp = A[son]
            A[son] = A[k]
            A[k] = temp
            k = son
    
    def heapify(self, A):
        for i in range((len(A) - 1) // 2, -1, -1):
            self.siftdown(A, i)
```

算法思路：
初始选择最接近叶子的一个父结点，与其两个儿子中较小的一个比较，若大于儿子，则与儿子交换。
交换后再与新的儿子比较并交换，直至没有儿子。
再选择较浅深度的父亲结点，重复上述步骤。
时间复杂度分析
这个版本的算法，乍一看也是 O(nlogn)， 但是我们仔细分析一下，算法从第 n/2 个数开始，倒过来进行 siftdown。也就是说，相当于从 heap 的倒数第二层开始进行 siftdown 操作，倒数第二层的节点大约有 n/4 个， 这 n/4 个数，最多 siftdown 1次就到底了，所以这一层的时间复杂度耗费是 O(n/4)，然后倒数第三层差不多 n/8 个点，最多 siftdown 2次就到底了。所以这里的耗费是 O(n/8 * 2), 倒数第4层是 O(n/16 * 3)，倒数第5层是 O(n/32 * 4) ... 因此累加所有的时间复杂度耗费为：
T(n) = O(n/4) + O(n/8 * 2) + O(n/16 * 3) ...
然后我们用 2T - T 得到：
2 * T(n) = O(n/2) + O(n/4 * 2) + O(n/8 * 3) + O(n/16 * 4) ...
T(n) = O(n/4) + O(n/8 * 2) + O(n/16 * 3) ...

2 * T(n) - T(n) = O(n/2) +O (n/4) + O(n/8) + ...
= O(n/2 + n/4 + n/8 + ... )
= O(n)
因此得到 T(n) = 2 * T(n) - T(n) = O(n)

## 堆排序

运用堆的性质，我们可以得到一种常用的、稳定的、高效的排序算法————堆排序。堆排序的时间复杂度为O(n*log(n))，空间复杂度为O(1)，堆排序的思想是：对于含有n个元素的无序数组nums, 构建一个堆(这里是小顶堆)heap，然后执行extractMin得到最小的元素，这样执行n次得到序列就是排序好的序列。
如果是降序排列则是小顶堆；否则利用大顶堆。

### Trick

由于extractMin执行完毕后，最后一个元素last已经被移动到了root，因此可以将extractMin返回的元素放置于最后，这样可以得到sort in place的堆排序算法。
当然，如果不使用前面定义的heap，则可以手动写堆排序，由于堆排序设计到建堆和extractMin， 两个操作都公共依赖于siftDown函数，因此我们只需要实现siftDown即可。(trick:由于建堆操作可以采用siftUp或者siftDown，而extractMin是需要siftDown操作，因此取公共部分，则采用siftDown建堆)。

### 升序堆排序（JAVA）

```java
public class Solution {
    private void siftdown(int[] A, int left, int right) {
        int k = left;
        while (k * 2 + 1 <= right) {
            int son = k * 2 + 1;
            if (son + 1 <= right && A[son] < A[son + 1]) {
                son = k * 2 + 2;
            }
            if (A[son] <= A[k]) {
                break;
            }
            int tmp = A[son];
            A[son] = A[k];
            A[k] = tmp;
            k = son;
        }
    }
    
    public void heapify(int[] A) {
        for (int i = (A.length - 1) / 2; i >= 0; i--) {
            siftdown(A, i, A.length - 1);
        }
    }
    
    void sortIntegers(int[] A) {
        heapify(A);
        for (int i = A.length - 1; i > 0; i--) {
            int tmp = A[0];
            A[0] = A[i];
            A[i] = tmp;
            siftdown(A, 0, i - 1);
        }
    }
}
```

堆是实现优先队列的一种数据结构，故C错；堆排序是稳定的nlogn的时间复杂度，故D错。

堆排不稳定 O(nlogn) O(1) 二叉堆最深深度O(logn)

https://www.lintcode.com/problem/heapify

# GROUP 8.5 DATA STRUCTURE DESIGN

https://www.lintcode.com/problem/12/     min stack

https://www.lintcode.com/problem/859/   max stack

https://www.lintcode.com/problem/40/    用栈实现队列

https://www.lintcode.com/problem/494/  双队列实现栈



# GROUP 9 BFS

- BFS的三种适用场景
  - 分层遍历 level order traversal of a graph/tree/matrix
  - 简单图的最短路径 uniformed cost search
  - connected components 连通块问题
    - 通过图中一个点找到所有其他连通的点
    - 找到所有方案 问题中 非递归的实现方式
  - 拓扑排序 比dfs的实现更简单
    - 任意topological order
    - has topological order 
    - 字典序最小的拓扑序 
    - 是否存在唯一的拓扑序
  - 例子
    - 二叉树的层次遍历 
    - 求出边长均为5的图的最短路径
    - 求出01矩阵上最大的全0块
    - 10个数中任意拿出5个的所有方案 非递归实现
    - 先序遍历通常使用递归方式来实现，即使使用非递归方式，也是借助栈来实现的，所以并不适合BFS，而层次遍历因为是一层一层的遍历，所以是BFS十分擅长的；边长一致的图是简单图，所以可以用BFS；矩阵连通块也是BFS可以处理的问题，求出最大块只需要维护一个最大值即可； 求所有方案问题，因此可以用BFS来处理，但是并不是唯一的解决方式。

## 二叉树的层次遍历

- 单队列 
- 双队列
- dummy node  + 单队列  None used to mark end of a level in traversal results

## 图

什么是图（Graph）？
图在离线数据中的表示方法为 <E, V>，E表示 Edge，V 表示 Vertex。也就是说，图是顶点（Vertex）和边（Edge）的集合。
图分为：
有向图（Directed Graph）
无向图（Undirected Graph）
BFS 大部分的时候是在图上进行的。
BFS 在两种图上都适用。另外，树（Tree）也是一种特殊的图。

如何定义一个图的数据结构？
有很多种方法可以存储一个图，最常用的莫过于：
1.邻接矩阵
2.邻接表
而邻接矩阵因为耗费空间过大，我们通常在工程中都是使用邻接表作为图的存储结构



邻接矩阵 Adjacency Matrix
[
[1,0,0,1],
[0,1,1,0],
[0,1,1,0],
[1,0,0,1]
]
例如上面的矩阵表示0号点和3号点有连边。1号点和2号点有连边。
当然，每个点和自己也是默认有连边的。
图中的 0 表示不连通，1 表示连通。
我们也可以用一个更具体的整数值来表示连边的长度。
邻接矩阵我们可以直接用一个二维数组表示，如
int[][] matrix;
这种数据结构因为耗费 O(n^2) 的空间，所以在稀疏图上浪费很大，因此并不常用。

邻接表 (Adjacency List)
[
[1],
[0,2,3],
[1],
[1]
]
这个图表示 0 和 1 之间有连边，1 和 2 之间有连边，1 和 3 之间有连边。即每个点上存储自己有哪些邻居（有哪些连通的点）。
这种方式下，空间耗费和边数成正比，可以记做 O(m)，m代表边数。m最坏情况下虽然也是 O(n^2)，但是邻接表的存储方式大部分情况下会比邻接矩阵更省空间。
可以用自定义的类来实现邻接表
Java:
class DirectedGraphNode {
int label;
List neighbors;
...
}
Python:
def DirectedGraphNode:
def **init**(self, label):
self.label = label
self.neighbors = [] # a list of DirectedGraphNode's



也可以使用 HashMap 和 HashSet 搭配的方式来存储邻接表

Java:

Map<T, Set> = new HashMap<Integer, HashSet>();

Python:

假设nodes为节点标签的列表: 使用了Python中的dictionary comprehension语法

adjacency_list = {x:set() for x in nodes}

or

adjacency_list = {}
for x in nodes:
adjacency_list[x] = set()
其中 T 代表节点类型。通常可能是整数(Integer)。
这种方式虽然没有上面的方式更加直观和容易理解，但是在面试中比较节约代码量。
而自定义的方法，更加工程化，所以在面试中如果时间不紧张题目不难的情况下，推荐使用自定义邻接表的方式。

## 二叉树的BFS vs 图的BFS
二叉树中进行 BFS 和图中进行 BFS 最大的区别就是二叉树中无需使用 HashSet（C++: unordered_map, Python: dict) 来存储访问过的节点（丢进过 queue 里的节点）
因为二叉树这种数据结构，上下层关系分明，没有环（circle），所以不可能出现一个节点的儿子的儿子是自己的情况。
但是在图中，一个节点的邻居的邻居就可能是自己了

## 为什么 BFS 可以搜索到最短路？

因为BFS是按照层级进行搜索，所以搜到答案时，一定是最短的一条路径。

我们可以使用反证法进行证明：

我们假设当前搜索到的路径 Y 不是最短的，那就说明存在一条更短的路径 X（即 X < Y）。

令路径 X 中的所有点是 {x1,x2,...,xx}。

那么x1是起点，且为 BFS 的第一层，x2为第二层......xx为第x层，

此时的结果与BFS中第Y层初次遇到xx点产生矛盾。

因此不存在任何一条比Y短的路径能找到终点。

## 例题

https://www.lintcode.com/problem/137/ clone graph

https://www.lintcode.com/problem/friend-circles/

https://www.lintcode.com/problem/knight-shortest-path-ii/

https://www.lintcode.com/problem/word-ladder/

## 本章小结
我们首先了解了宽度优先搜索的适用场合（分层遍历，连通块问题，拓扑排序）；
然后我们学习了三种BFS的实现方式（单队列，双队列，DummyNode）；
最后我们接触到了一种全新的知识——图，并对图的存储方式有了一定了解。
下章预告：
接下来的一章，我们将着重学习另一种搜索方式深度优先搜索（DFS），以及掌握实现DFS所使用的通常技巧——递归。
最后的最后，请各位同学认真复习本章知识，坚持就是胜利！

## Review

https://www.lintcode.com/problem/17/   全子集

```
全子集搜索树 假设有一个含有4个元素的集合，根据这个集合画出的四叉树和二叉树的节点数分别是多少？
n叉树的节点数为（2^n），有16个；二叉树的节点数为（(2^n)* 2 - 1），有31个。
```

https://www.lintcode.com/problem/761/   最小子集

https://www.lintcode.com/problem/7/ 二叉树BFS序列化

https://www.lintcode.com/problem/1235/ 序列化反序列化BST

## 双向BFS

https://www.lintcode.com/problem/611/

https://www.lintcode.com/problem/630/

https://www.lintcode.com/problem/120/

https://www.lintcode.com/problem/121/

# GROUP 10 DFS

在第11章中，我们主要讲解了BFS的实现和使用。在本章的学习中，我们讲解一种编程中的技巧——递归，以及可以利用递归实现的另一种搜索方法，深度优先搜索（简称DFS）。然后学习对DFS的应用，体会遍历与分治的思想。

在过去的学习中，同学应该已经对递归有了一定的认识。
下面就让老师来系统的讲解一下，递归，深度优先搜索和回溯这三者的联系与区别在哪里

- 回溯法 = dfs;    dfs即便是不手动回溯 递归参数本身也在回溯 如 fib(n) = fib(n-1) + fib(n-2)   n-1 => n
- 回溯操作 **让一些状态参数回到递归之前的状态**
- DFS可以使用非递归来实现；使用递归函数的时候，我们使用的是操作系统中的栈，所以不需要手动建立栈；DFS和BFS的搜索顺序是截然不同的，除非是在一条链上搜索。
- 在上一个视频中，我们了解了回溯法和回溯操作。
  同学们可能会有疑问：什么时候应该进行“回溯”呢？
  老师准备了两段代码，让我们来看看具体应该什么时候在搜索中加入“回溯”操作吧！

https://www.lintcode.com/problem/binary-tree-paths/

- 遍历与分治
  - 分治法是一种将大问题分解为小问题的思想，不一定是二分的；分治在某些情况上来看是一种特殊的遍历，所以他们之间并非没有联系。

https://www.lintcode.com/problem/balanced-binary-tree/

https://www.lintcode.com/problem/maximum-depth-of-binary-tree/

https://www.lintcode.com/problem/maximum-subtree/

https://www.lintcode.com/problem/median-of-two-sorted-arrays/

能做出 median of two sorted arrays 的小伙伴们看来已经掌握了分治法的真谛，对任何题目都束手无策的同学建议多加复习和思考，感受分而治之的思想带来的灵感。

课上的时间总是那么短暂，又到了章末总结啦，让我们想想这章都学了什么？
首先我们认识了递归、DFS和回溯的的关联和区别；接下来了解了使用回溯的时机，并从两个不同的角度：遍历（亲力亲为）和分治（分配任务）来看待问题；最后我们一起对分治法这个重点知识进行了实战训练。





# GROUP 11 组合类DFS

在非二叉树上的深度优先搜索（Depth-first Search）中，90%的问题，不是求组合（Combination）就是求排列（Permutation）。特别是组合类的深度优先搜索的问题特别的多。而排列组合类的搜索问题，本质上是一个“隐式图”的搜索问题。

本章关键字：DFS（Depth First Search，深度优先搜索），Combination（组合），Subset（子集）。

在本章的学习中，我们将使用DFS来解决在隐式图上的组合问题。

一个问题如果没有明确的告诉你什么是点，什么是边，但是又需要你进行搜索的话，那就是一个隐式图搜索问题了。所以对于这类问题，我们首先要分析清楚什么是点什么是边。
关于分析的过程，我们下面的视频中进行讲解。

https://www.lintcode.com/problem/subsets/

在攻克了上面的问题之后，请同学思考下这个问题：如果所给的集合是[1,2,2,3]，并且我输出的子集中还不允许出现两个[1,2,3]，这时我们该怎么改动搜索过程呢？
这个问题是一个经典的全子集问题的follow up，稍加思考过后，来看看老师对这种带有重复元素的集合是怎么处理的吧。

对于“选代表”的方法来说，我们采取的办法是从若干个数字相同但顺序不同的小集合中拿出一个有序的集合作为代表，将剩下的无序集合舍弃。
那有没有一种数据结构，可以完成去重工作呢？答案自然是hash，所以我们可以对所有的集合进行哈希，每次将当前搜索到的集合subset放入结果集合subsets中的时候，只需将这个集合看做是key，如果对应的value不存在，就证明这个集合是个没出现过的新集合，这时再把新的集合放入subsets中即可。

```java
//在这段代码中，我们选择将subset从集合变成字符串，从而实现对集合的哈希。

public class Solution {
    /**
     * @param nums: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<>();
        HashMap<String, Boolean> visited = new HashMap<String, Boolean>();
        Arrays.sort(nums);
        dfs(nums, 0, new ArrayList<>(), subsets, visited);
        
        return subsets;
    }
    
    String getHash(List<Integer> subset) {
        String hashString = "";
        for (int i = 0;i < subset.size(); i++) {
            hashString += subset.get(i).toString();
            hashString += "_";
        }
        
        return hashString;
    }
    
    void dfs(int[] nums, 
             int startIndex, 
             List<Integer> subset,
             List<List<Integer>> subsets,
             HashMap<String, Boolean> visited) {
        String hashString = getHash(subset);
        
        if (visited.containsKey(hashString)) {
            return ;
        }
        
        visited.put(hashString, true);
        subsets.add(new ArrayList<Integer>(subset));
        for (int i = startIndex;i < nums.length; i++) {
            subset.add(nums[i]);
            dfs(nums, i + 1, subset, subsets, visited);
            subset.remove(subset.size() - 1);
        }
        
    }
    
}
```



使用Python的小伙伴可以在下面的九章题解链接中查看Python的相关代码。
对于此题其他的做法（如BFS、非递归方法）也能在下面的链接中查看。
https://www.jiuzhang.com/solution/subsets-ii/

# GROUP 12 排列类DFS

在这一章的学习中，我们将继续上一节课的内容，对排列类问题的DFS解法进行探讨。
此外，我们将研究一种十分有名的NP问题：TSP问题。

本章关键字：DFS（Depth First Search，深度优先搜索），Permutations（排列），Graph（图）。

我们回顾一下隐式图：没有明确的告诉你什么是点，什么是边，但是需要去搜索。
此时我们需要自己去解析这张图，分析什么是点与边。

全排列问题
全排列问题是“排列式”深度优先搜索问题的鼻祖。很多搜索的问题都可以用类似全排列的代码来完成。包括我们前面学过的全子集问题的一种做法。在这一小节中我们需要掌握：

- 普通的全排列问题怎么做
- 有重复的全排列问题怎么做？如何在搜索类问题中去重？
  首先，我们来学习排列问题的搜索树是什么样的吧。

第二步让我们来分析下全排列问题的代码和时间复杂度，并由老师手把手带着一起写出Java和Python的代码

有的同学可能会有疑惑：递归和循环的区别到底是什么？我们可不可以用大量循环来实现呢

接下来，我们一起来研究著名的旅行商问题。
我们将使用3种思路来分别分析、解释。
每种思路都使用两种语言分别进行讲解（python与java）。
下面请看第一种思路（暴力搜索与剪枝优化）



任何数异或0等于它本身，故 0 ^ 10 = 10，并且异或符合交换律（0 ^ 10 = 10 ^ 0）。
任何数异或它自己都是0，故 10 ^ 10 = 0。
3(011) ^ 7(111) = 4(100)，括号内为对应的二进制。
异或具有“知一得三”的性质，已知 A ^ B = C，一定能得到 A ^ C = B 和 B ^ C = A。



状压DP的主要思想就是利用一个二进制足够长的整数，使用相应的二进制位的状态（0或1）来记录某个点是否被走过，是一种十分精妙的思想。

如果TSP问题中城市数量为10个，那么我最好用下列哪个范围来进行状态压缩呢

10个城市，也就是2^10 = 1024种状态。
在二进制中，长度为10的数字为：0 000 000 000 ~ 1 111 111 111，也就是`[0, 1023]`。

https://www.lintcode.com/problem/traveling-salesman-problem/

https://www.lintcode.com/problem/permutations/

https://www.lintcode.com/problem/permutations-ii/



# GROUP 13 非递归的方式实现排列和组合类DFS

在前面的学习中我们学习了递归实现排列组合问题，在本章中我们将学习非递归的实现

本章关键字：Combination（组合），Permutations（排列），Binary（二进制）

用非递归（Non-recursion / Iteration）的方式实现全子集问题，有两种方式：

- 进制转换（binary）
- 宽度优先搜索（Breadth-first Search）



## subsets - 基于进制转换的方法

https://www.lintcode.com/problem/17/

思路就是使用一个 正整数的二进制表示 的第 i 位是 1 还是 0 来代表集合的第 i 个数取或者不取。因为从 0 到 2^n - 1 总共 2^n 个整数，正好对应集合的 2^n 个子集。
比如 {1，2，3} 的子集可以用 0 到 7 来表示。

```
0 -> 000 -> {}
1 -> 001 -> {3}
2 -> 010 -> {2}
3 -> 011 -> {2,3}
4 -> 100 -> {1}
5 -> 101 -> {1,3}
6 -> 110 -> {1,2}
7 -> 111 -> {1,2,3}
```

参考代码：

python代码：

```python
class Solution:
    def subsets(self, nums):
        result = []
        n = len(nums)
        nums.sort()
        for i in range(1 << n):
            subset = []
            for j in range(n):
                if (i & (1 << j)) != 0:
                    subset.append(nums[j])
            result.append(subset)
        return result
```

java代码：

```java
class Solution {
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        int n = nums.length;
        Arrays.sort(nums);
        for (int i = 0; i < (1 << n); i++) {
            List<Integer> subset = new ArrayList<Integer>();
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {
                    subset.add(nums[j]);
                }
            }
            result.add(subset);
        }
        
        return result;
    }
}
```

C++代码：

```c++
class Solution {
public:
    /**
     * @param nums: A set of numbers
     * @return: A list of lists
     */
    vector<vector<int>> subsets(vector<int> &nums) {
        vector<vector<int>> result;
        const int n = nums.size();
        sort(nums.begin(), nums.end());
        for (int i = 0; i < (1 << n); i++) {
            vector<int> subset;
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {
                    subset.push_back(nums[j]);
                }
            }
            result.push_back(std::move(subset));
        }
        
        return result;
    }
};
```

## subsets - 基于 BFS 的方法

在 BFS 那节课的讲解中，我们很少提到用 BFS 来解决找所有的方案的问题。事实上 BFS 也是可以用来做这件事情的。
用 BFS 来解决该问题时，层级关系如下：

```
第一层: []
第二层: [1] [2] [3]
第三层: [1, 2] [1, 3], [2, 3]
第四层: [1, 2, 3]
```

每一层的节点都是上一层的节点拓展而来。

参考代码：

python代码：

```python
class Solution:
    def subsets(self, nums):
        results = []

        if not nums:
            return results

        nums.sort()

        # BFS
        queue = deque()
        queue.append([])

        while queue:
            subset = queue.popleft()
            results.append(subset)

            for i in range(len(nums)):
                if not subset or subset[-1] < nums[i]:
                    nextSubset = list(subset)
                    nextSubset.append(nums[i])
                    queue.append(nextSubset)

        return results
```

java代码：

```java
public class Solution {
    
    /*
     * @param nums: A set of numbers
     * @return: A list of lists
     */
    public List<List<Integer>> subsets(int[] nums) {
        // List vs ArrayList （google）
        List<List<Integer>> results = new LinkedList<>();
        
        if (nums == null) {
            return results; // 空列表
        }
        
        Arrays.sort(nums);
        
        // BFS
        Queue<List<Integer>> queue = new LinkedList<>();
        queue.offer(new ArrayList<Integer>());
        
        while (!queue.isEmpty()) {
            List<Integer> subset = queue.poll();
            results.add(subset);
            
            for (int i = 0; i < nums.length; i++) {
                if (subset.size() == 0 || subset.get(subset.size() - 1) < nums[i]) {
                    List<Integer> nextSubset = new ArrayList<Integer>(subset);
                    nextSubset.add(nums[i]);
                    queue.offer(nextSubset);
                }
            }
        }
        
        return results;
    }
}
```

C++代码：

```c++
class Solution {
public:
    /*
     * @param nums: A set of numbers
     * @return: A list of lists
     */
    vector<vector<int>> subsets(vector<int> &nums) {
        vector<vector<int>> results;
        sort(nums.begin(), nums.end());
        
        // BFS
        queue<vector<int>> que;
        que.push({});
        
        while (!que.empty()) {
            vector<int> subset = que.front();
            que.pop();
            results.push_back(subset);
            
            for (int i = 0; i < nums.size(); i++) {
                if (subset.size() == 0 || subset.back() < nums[i]) {
                    vector<int> nextSubset = subset;
                    nextSubset.push_back(nums[i]);
                    que.push(nextSubset);
                }
            }
        }
        
        return results;
    }
};
```

## 求下一个排列

https://www.lintcode.com/problem/52/

在学习全排列的解决方法之前，我们先来学习如何求 下一个排列

问题：给定一个若干整数的排列，给出按整数大小进行字典序从小到大排序后的下一个排列。若没有下一个排列，则输出字典序最小的序列。
从末尾往左走，如果一直递增，例如 {...9,7,5} ，那么下一个排列一定会牵扯到左边更多的数，直到一个非递增数为止，例如 {...6,9,7,5} 。对于原数组的变化就只到 6 这里，和左侧其他数再无关系。6 这个位置会变成6右侧所有数中比 6 大的最小的数，而 6 会进入最后 3 个数中，且后 3 个数必是升序数组。
所以算法步骤如下：

- 从右往左遍历数组 nums，直到找到一个位置 i ，满足 nums[i] > nums[i - 1] 或者 i 为 0 。
- i 不为 0 时，用j再次从右到左遍历 nums ，寻找第一个 nums[j] > nums[i - 1] 。而后交换 nums[j] 和 nums[i - 1] 。注意，满足要求的 j 一定存在！且交换后 nums[i] 及右侧数组仍为降序数组。
- 将 nums[i] 及右侧的数组翻转，使其升序。

可能会有同学有些疑问：
Q：i为0怎么办？
A：i为0说明整个数组是降序的，直接翻转整个数组即可。

Q：有重复元素怎么办？
A：在遍历时只要严格满足 nums[i] > nums[i - 1] 和 nums[j] > nums[i - 1] 就不会有问题。

Q：元素过少是否要单独考虑？
A：当元素个数小于等于1个时，可以直接返回。

python参考代码：

```python
class Solution:
    # 用于翻转nums[i]到nums[j]，包含两端的这一小段数组
    def swapList(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        n = len(nums)
        if n <= 1:
            return
        
        i = n-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1

        if i != 0:
            j = n-1
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[j], nums[i-1] = nums[i-1], nums[j]
        self.swapList(nums, i, n-1)
```

java参考代码：

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers that's next permuation
    */
    // 用于交换nums[i]和nums[j]
    public void swapItem(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    // 用于翻转nums[i]到nums[j]，包含两端的这一小段数组
    public void swapList(int[] nums, int i, int j) {
        while (i < j) {
            swapItem(nums, i, j);
            i ++; 
            j --;
        }
    }
    public void nextPermutation(int[] nums) {
        int len = nums.length;
        if ( len <= 1) {
            return;
        }
        int i = len - 1;
        while (i > 0 && nums[i] <= nums[i - 1]) {
            i --;
        }
        if (i != 0) {
            int j = len - 1;
            while (nums[j] <= nums[i - 1]) {
                j--;
            }
            swapItem(nums, j, i-1);
        }
        swapList(nums, i, len - 1);
    }
}
```

在学习了 下一个排列 的算法之后，对于全排列问题，我们只需要不断调用这个算法的函数就可以啦。
一些可以做得更细致的地方：
为了确定何时结束，建议在迭代前，先对输入nums数组进行升序排序，迭代到降序时，就都找完了。有心的同学可能还记得在 nextPermutation 当中，当且仅当数组完全降序，那么从右往左遍历的指针 i 最终会指向 0 。所以可以为 nextPermutation 带上布尔返回值，当 i 为 0 时，返回 false，表示找完了。要注意，排序操作在这样一个 NP 问题中，消耗的时间几乎可以忽略。
当数组长度为 1 时，nextPermutation 会直接返回 false ；当数组长度为 0 时， nextPermutation 中 i 会成为 -1 ，所以返回 false 的条件可以再加上 i 为 -1 。
Java中，如果输入类型是 int[] ，而输出类型是 List<List> ，要注意，并没有太好的方法进行类型转换，这是由于 int 是基本类型。建议还是自行手动复制，实际工作中还可使用 guava 库。

java示例代码：

```java
public class Solution {
    /*
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    public List<List<Integer>> permute(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        
        boolean next = true;  // next 为 true 时，表示可以继续迭代
        while (next)  {
            List<Integer> current = new ArrayList<>();  // 进行数组复制
            for (int num : nums) {
                current.add(num);
            }
            
            result.add(current);
            next = nextPermutation(nums);
        }
        return result;
    }
    // 用于交换nums[i]和nums[j]
    public void swapItem(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    // 用于翻转nums[i]到nums[j]，包含两端的这一小段数组
    public void swapList(int[] nums, int i, int j) {
        while (i < j) {
            swapItem(nums, i, j);
            i ++; 
            j --;
        }
    }
    public boolean nextPermutation(int[] nums) {
        int len = nums.length;
        int i = len - 1;
        while (i > 0 && nums[i] <= nums[i - 1]) {
            i--;
        }
        if (i <= 0) {
            return false;
        }
        
        int j = len - 1;
        while (nums[j] <= nums[i - 1]) {
            j--;
        }
        swapItem(nums, j, i - 1);
        
        swapList(nums, i, len - 1);
        
        return true;
    }
    
}
```

python示例代码：

```python
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        nums.sort()
        result = []


        hasNext = True  # hasNext 为 true 时，表示可以继续迭代
        while hasNext:
            current = list(nums)  # 进行数组复制
            result.append(current)
            hasNext = self.nextPermutation(nums)
        
        return result


    def swapList(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
    def nextPermutation(self, nums):
        n = len(nums)
        if n <= 1:
            return
        
        i = n - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1


        if i <= 0:
            return False


        j = n-1
        while nums[j] <= nums[i-1]:
            j -= 1
        nums[j], nums[i-1] = nums[i-1], nums[j]
        
        self.swapList(nums, i, n-1)


        return True
```

## 全排列

https://www.lintcode.com/problem/15/

https://www.lintcode.com/problem/197/   Permutation Index

题目：给出一个不含重复数字的排列，求这些数字的所有排列按字典序排序后该排列的编号，编号从1开始。例如排列 [1, 2, 4] 是第 1 个排列。

### 算法描述

只需计算有多少个排列在当前排列A的前面即可。如何算呢?举个例子，[3,7,4,9,1]，在它前面的必然是某位置i对应元素比原数组小，而i左侧和原数组一样。也即 [3,7,4,1,X] ， [3,7,1,X,X] ， [3,1或4,X,X,X] ， [1,X,X,X,X] 。
而第 i 个元素，比原数组小的情况有多少种，其实就是 A[i] 右侧有多少元素比 A[i] 小，乘上 A[i] 右侧元素全排列数，即 A[i] 右侧元素数量的阶乘。 i 从右往左看，比当前 A[i] 小的右侧元素数量分别为 1,1,2,1，所以最终字典序在当前 A 之前的数量为 1×1!+1×2!+2×3!+1×4!=39 ，故当前 A 的字典序为 40。

### 具体步骤：

用 permutation 表示当前阶乘，初始化为 1,result 表示最终结果，初始化为 0 。由于最终结果可能巨大，所以用 long 类型。
i从右往左遍历 A ，循环中计算 A[i] 右侧有多少元素比 A[i] 小，计为 smaller ，result += smaller * permutation。之后 permutation *= A.length - i ，为下次循环 i 左移一位后的排列数。
已算出多少字典序在 A 之前，返回 result + 1 。

### 参考代码

java代码：

```java
public class Solution {
    /**
     * @param A: An array of integers
     * @return: A long integer
     */
    public long permutationIndex(int[] A) {
        // write your code here
        long permutation = 1;
        long result = 0;
        for (int i = A.length - 2; i >= 0; --i) {
            int smaller = 0;
            for (int j = i + 1; j < A.length; ++j) {
                if (A[j] < A[i]) {
                    smaller++;
                }
            }
            result += smaller * permutation;
            permutation *= A.length - i;
        }
        return result + 1;
    }
}
```

python代码：

```python
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        permutation = 1
        result = 0
        for i in range(len(A) - 2, -1, -1):
            smaller = 0
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    smaller += 1
            result += smaller * permutation
            permutation *= len(A) - i
        return result + 1
```

### 常见QA：

Q：为了找寻每个元素右侧有多少元素比自己小，用了O(n^2)的时间，能不能更快些？
A：可以做到O(nlogn)，但是很复杂，这是另外一个问题了，可以使用BST，归并排序或者线段树：http://www.lintcode.com/zh-cn/problem/count-of-smaller-number-before-itself/
Q：元素有重复怎么办？
A：好问题！元素有重复，情况会复杂的多。因为这会影响 A[i] 右侧元素的排列数，此时的排列数计算方法为总元素数的阶乘，除以各元素值个数的阶乘，例如 [1, 1, 1, 2, 2, 3] ，排列数为
6! ÷ (3! × 2! × 1!) 。为了正确计算阶乘数，需要用哈系表记录 A[i] 及右侧的元素值个数，并考虑到 A[i] 与右侧比其小的元素 A[k] 交换后，要把 A[k] 的计数减一。用该哈系表计算正确的阶乘数。而且要注意，右侧比 A[i]小 的重复元素值只能计算一次，不要重复计算！



## DFS经典题精讲

在n=4的皇后问题中，我们能得到多少种解呢？n=4时，皇后问题的可行解只有（2，4，1，3）和（3，1，4，2）

求方案总数的问题90%都是什么算法？  方案总数大多数情况都是动态规划问题，比如经典的爬台阶问题。

isValid可以用Hash来达到O(1)查询某一行或某一列或某个对角是否有皇后占据。

虽然我们看上去优化了一个n的数量级，但是最深层的循环没有被优化，因此复杂度在实际上并没有被降低，所以这种优化的意义并不大。

https://www.lintcode.com/problem/33/

https://www.lintcode.com/problem/34/

https://www.lintcode.com/problem/802/  sudoku solver



# GROUP 14 MEMOIZED SEARCH

从这一章开始，我们逐步学习动态规划这个重要的算法思想。
本章的主要内容是从搜索向动态规划进行过渡，学习记忆化搜索的相关知识。

本章关键字：Recursion（递归）、Memoization（记忆化搜索）、 Dynamic Programming（DP、动态规划）

首先我们先来利用遍历与分治解决这道数字三角形问题

```
在下面的数字三角形中，从顶端走到底端所能获得的最小路径长是多少？
[
[3],
[4,1],
[2,7,2],
[5,3,4,6]
]
3 + 1 + 2 + 4 = 10（从根开始，右右左）。而此时算法的时间复杂度应该是多少？

所有的路径数量是2^n，没有任何实质上的剪枝，所以仍然是O(2^n)。
在下面的数字三角形中，从顶端走到底端所能获得的最小路径长是多少？
[
[3],
[4,1],
[2,7,2],
[5,3,4,6]
]
3 + 1 + 2 + 4 = 10（从根开始，右右左）。所有的路径数量是2^n，没有任何实质上的剪枝，所以仍然是O(2^n)。

我们发现无论是我们学过的遍历还是分治，都无法得到理想状态的时间复杂度。
如果能把我计算过的路径记录下来，是不是会更快呢？
我们一起来看下面的视频。
用记忆化搜索实现数字三角形
因为我们已经以一种方式（HashMap）记录了所有路径。所以每一对x和y只出现了一次，也就是 n^2 级别，相当于每一对起点终点都计算了一次，也就是 O(n^2) 。

并不是所有的算法都适用于所有的问题，那么记忆化搜索可能会出现什么样的问题呢?
下面让老师借用一道经典的巴什博弈（Bash Game）来说明。
A 运行时间无法接受
B 递归深度过高
C 边缘数据没有判断
D 没问题
这个问题的时间复杂度是 O(n) 级别，所以时间上我们可以接受，但是因为时间是 O(n)，最差情况的递归深度就变成了 O(n)，这是很容易爆栈（stack overflow）的。
而递归出口就是边缘数据的判断，因此不存在选项C的情况。

```

https://www.lintcode.com/problem/bash-game/

https://www.lintcode.com/problem/triangle/

# GROUP 15 DP

在这节课中，我们来学习一下动态规划（Dynamic Programming)的基础知识。首先，我们先来看一下到底什么是动态规划，它的基本思想是什么，它和贪心法又有什么区别。

每个算法都需要用代码来进行实现，那么我们怎么实现动态规划呢。其实在上一节课中我们已经讲到了它的一种实现方式——记忆化搜索。那么这次，我们来讲讲它的另一种实现方式——递推。

接下来，我们来看一下我们在写动态规划的时候可以从哪几个方面入手，它和递归又有怎样的联系，一起来看动态规划的四要素吧

接下来我们用一个比较简单的题目来练习一下动态规划吧。Java的同学可以看接下来的两个视频了解一下思路，在最后一个视频中，会讲到如何使用Java实现这道题的 。

UNIQUE PATHS 同样，我们也可以用自底向上的方法来实现这个问题，大家可以自己先尝试一下，再来看视频哦

好了，在这个章节中，我们讲到了动态规划的基本概念，动态规划的实现方式和动态规划的四要素。动态规划问题讲究的还是熟悉，如果一开始比较困难，多做一些题，总是可以变得熟练的。那我们就下一节课再见咯。



求全部具体方案的问题，虽然有时可以通过动态规划减少一定的运行时间，但是时间复杂度是没法降低的。比如说word break II。因为这种类型的问题，总时间复杂度是与方案总数有关的。其他三种都可以用dp降低时间复杂度。

那么现在我们就来看一下，如果我们知道了是哪种动态规划，我们该如何判断出动态规划的状态方程

上一个视频中，我们讲到了坐标型动态规划，划分型动态规划，匹配型动态规划，区间型动态规划这几种动态规划的常见的dp方程。可以回忆一下，看能否回忆起来。接下来我们就用三个小问题来实践一下。

## 坐标型DP

首先是一道坐标型动态规划的经典问题

https://www.lintcode.com/problem/115/

https://www.lintcode.com/problem/630/

https://www.lintcode.com/problem/116/

好啦，在这一节课中我们就学到了动态规划的基础知识和坐标型动态规划的例题，也算是给我们动态规划的学习开了个头，在下一节课中，我们就来讲一讲另一个非常常见的动态规划问题：背包型动态规划。





## 背包型DP

在这一章中，我们就要来学习背包了，这一节课我们会讲到01背包与多重背包两种类型，其中01背包就是，每种物品只有一个的背包。而多重背包就是每种物品有几个，你可以选择其中的任意个放入背包。那么我们先来看看01背包问题的解法吧。

在这里数据的先后顺序是没有关系的，就像你有一个苹果一个橙子，只要背包够大，先放苹果和先放橙子都能把这两个物品装进去。

我们刚才说，01背包还有另外一种状态方程的表示方法，我们也顺便一起来看一下吧

同时我们也会发现动态规划的时间复杂度是多项式级别的，而如果用我们之前学的深度优先搜索去做，时间复杂度是指数级别的，那么是不是动态规划一定比搜索要好呢？一起来看一下吧

总而言之，只有在m>>2^n的时候，动态规划才弱于搜索，所以大部分情况下，动态规划都是一个最优的选择。那么接下来我们就来看一下01背包的几种题型吧

接下来，我们再来看一下一个01背包的变型版本，给定物品数量的背包——多重背包。

https://www.lintcode.com/problem/92/

https://www.lintcode.com/problem/125/

https://www.lintcode.com/problem/563/









## 区间型DP

今天我们来学习区间型动态规划。
这是一种不算常见并且不算容易的题型，但我们也有将其掌握的必要。

什么样的字眼可能是在暗示区间型动态规划? 子数组 substring subsequence 方案/答案总数

下面的代码段中存在什么样的问题？ 可以看出dp[i]依赖于dp[i+1]，而我们先求到的是dp[i]，所以出现了错误的依赖。

```
# python3
for i in range(n):
	for j in range(i + 2, n):
		dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
// java
for (int i = 0; i < n; i++) {
	for (int j = i + 2, j < n; j++) {
		dp[i][j] = dp[i + 1][j - 1] && s.charAt(i) == s.charAt(j);
	}
}
```

是否可以使用滚动数组和DP类型无关，和DP的转移方程有直接关联，如果DP状态的依赖关系较简单：如 i 依赖 i-1 就可以用，如果 i 依赖 0,1,2,...,(i-1) 就没必要使用。

https://www.lintcode.com/problem/476/

https://www.lintcode.com/problem/168/

https://www.lintcode.com/problem/741/    [题目blog](https://blog.csdn.net/xiaocong1990/article/details/79678360?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control)

## 匹配型DP

https://www.lintcode.com/problem/192/ wildcard matching

https://www.lintcode.com/problem/77/   LCS

https://www.lintcode.com/problem/119/    edit distance

https://www.lintcode.com/problem/154/  regex matching

## 划分型DP

划分型动态规划本质上是一种前缀型动态规划，一般情况下，它的状态都定义为诸如“前i个字符”，“前i个数字”等。

https://www.lintcode.com/problem/107/    word break

https://www.lintcode.com/problem/512/     decode ways

https://www.lintcode.com/problem/437/     copy books



## 接龙型DP

LIS二分解法 偏贪心 https://www.lintcode.com/problem/76/

https://www.lintcode.com/problem/602/   Russian Doll Envelopes

https://www.lintcode.com/problem/603/   Largest Divisible Set

## 树型DP





# GROUP 16 字符串

## 字符串常用函数

```python
Java中
String demo = "Hello,world!";
1.int length = demo.length(); //获取字符串的长度
2.boolean equals = demo.equals("Hello,world"); // 比较两个字符串相等
3.boolean contains = demo.contains("word"); // 是否包含子串
4.String replace = demo.replace("Hello,", "Yeah@"); // 将指定字符串(或正则表达式)替换，返回替换后的结果
5.char little = demo.charAt(5); // 查找字符串中索引为5的字符（索引从0开始）
6.String trim = demo.trim(); // 将字符串左右空格去除，返回去除空格后的结果
7.String concat = demo.concat("Great!"); // 拼接字符串，返回拼接结果
8.char[] charArray = demo.toCharArray(); // 返回该字符串组成的字符数组
9.String upperCase = demo.toUpperCase(); // 返回该字符串的大写形式
10.String lowerCase = demo.toLowerCase(); // 返回该字符串的小写形式

Python中
s = "Hello,World"
1.print(s[1]) # 'e', 取出某个位置的字符
2.print(s[1:6]) # 'ello,' ，字符串切片
3.print(len(s)) # 11, 返回字符串的长度
4.print("e" in s) # True, 返回字符是否在字符串中
5.print(s.lower()) # 'hello,world', 将字符串所有元素变为小写
6.print(s.upper()) # 'HELLO,WORLD', 将字符串所有元素变为大写
7.s += '...' # Hello,World... ，字符串拼接，在字符串后拼接另一个字符串
8.print(s.find('lo')) # 3, 返回第一次找到指定字符串的起始位置（从左往右找）
9.print(s.swapcase()) # hELLO,wORLD..., 将大小写互换
10.print(s.split(',')) # ['Hello', 'World...'], 将字符串根据目标字符分割
11.isdigit() isalpha()

```



## KMP Manacher Rabin Karp Bayer Moore ?

大部分题不需要高级算法完成 可以通过双指针 dp等方式解决 高级算法的唯一的意义就是能拿到strong hire  但其实并不符合面试场景

### Longest Palindromic substring (assume unique)

- 最长回文子串

- Eg. lps("abcdzdcab") = "cdzdc";  lps("aba") = "aba";

- 一个长度为n的字符串的子串(substring)的数量级是O(n^2)

  - substring子串 必须是连续的 

    - abcd:     a, b, c, d;    ab, bc, cd;  abc, bcd;  abcd   从长度为1至n共 n+n-1+...+1= (n+1)*n/2个子序列 故O(n^2)

  - subsequence子序列 非连续字符 如ac

    - 子序列不需要是连续的(可以跳跃), 但只能从原序列中删除/不删  不可以旋转   参考LCS最长公共子序列问题
      - A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

    - 因此对于长度为n的字符串的子序列，每个字符都有选或不选两种可能。 因此其子序列的数量是指数级别O(2^n)的  size of power set

- brute force

  - ```python
    for 起点  O(n)
        for 终点  O(n)
            if is_palindrome(子串(起点, 终点)):    O(n)
                record longest one seen so far
                
    # 相向型双指针
    双指针
    - 相向
    - 同向
    - 背向(逆向)
    def is_palindrome():
         abca
          ^^
          LR  如果相等 相向同步内移指针
    
    brute force O(n^3)
    简单优化 按substring长度和起点遍历
    # GOOD STYLE EXAMPLE 
    class Solution:
        """if they meet, then there s is palindrome"""
        def is_palindrome(self, s, left, right):
            while left < right and s[left] == s[right]:
                    left += 1
                    right -= 1
            return left >= right
        """
        @param s: input string
        @return: a string as the longest palindromic substring
        """
        def longestPalindrome(self, s):
            if not s:
                return None
            # range (左闭,右开,step) 从大到小枚举长度
            for substr_len in range(len(s), 0, -1): 
                # counterpart_len = len(s) - substr_len 枚举起点位置 留够后面空间
                for start_index in range(len(s) - substr_len + 1):
                    if self.is_palindrome(s, start_index, start_index + substr_len - 1):
                        return s[start_index:start_index + substr_len] # 找到的第一个即为最长子串
            # no palindrome substr
            return ""
    # 这也是一个典型的区间型动态规划 (区间作为状态);  状态转移公式
    # i..j子串是不是palindrome 取决于端点字符和去掉端点字符的子串
    is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]
    # 至少为2个字符 n - 1 >= i + 1 > 0   i = 0;  初始化 单个字符是回文串 空串也是回文串
    is_palindrome[i][i] = True
    is_palindrome[i][i - 1] = True
    # 索引的依赖关系决定 i要从大到小遍历 j根据其本身定义 取值范围[i, n-1]
    for i in range(len(s), -1, -1):
        for j in range(i, n, 1):
            pass
    # 区间型动态规划 可以按长度先从小到大枚举 然后for循环起点 终点计算出来 j = i + length - 1    O(n^2) time space
    class Solution:
        """
        @param s: input string
        @return: a string as the longest palindromic substring
        """
        def longestPalindrome(self, s):
            if not s:
                return ""
            n = len(s)
            # deep copy, avoid copied arr points to the same arr
            is_palindrome = [[False] * n for _ in range(n)]
            for i in range(n):
                is_palindrome[i][i] = True
            # empty string / invalid string
            for i in range(1, n):
                is_palindrome[i][i - 1] = True
            start, longest = 0, 1
            # 填表顺序遍历 从小到大 长度
            for length in range(2, n + 1):
                for i in range(n - length + 1): # 遍历起始位置
                    j = i + length - 1
                    is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]
                    if is_palindrome[i][j] and length > longest:
                        start, longest = i, length
            return s[start:start + longest]
    ```

- Manacher's Algorithm O(n) 最优解 但不适合面试场景 能写出来也只能说背过 没意义 面试官自己也不一定会 但是可以拿strong hire

- 常规dp解可以拿hire

- 经典问题的最优解 如有人名的 不要去背诵




  #### Related Problems

1. follow up: substring => subsequence; find the longest palindromic subsequence's length

```python
class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    bbbab res bbbb 4
    bbbbb res bbbbb 5
    brute force O(n * 2^n) 
    https://leetcode-cn.com/problems/longest-palindromic-subsequence/solution/zi-xu-lie-wen-ti-tong-yong-si-lu-zui-chang-hui-wen/
    """
    def longestPalindromeSubseq(self, s):
        if not s: 
            return 0
        n = len(s)
        length = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            length[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    length[i][j] = length[i + 1][j - 1] + 2
                else:
                    length[i][j] = max(length[i + 1][j], length[i][j - 1])
        return length[0][n - 1]
```



### Implement strStr

 子串匹配

output the first index(from `0`) of target string in the source string, if not exist return -1     O(n^2)   Follow up O(n)

- KMP可以拿strong hire但是没必要KMP  
- 这题不是考直接调官方库解决问题 没意义
- 注意 Java取substring 会不会越界   取substring取到的是个全新str 占内存

```python
class Solution:
    """
    O(n^2) brute force best practice  for循环起始位置 一个一个字符比较 等则继续不等抛弃 查看下一个起始位置
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        if not target:
            return 0
        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] == target[j]:
                    if j == len(target) - 1:
                        return i
                else:
                    break
        return -1
```

 Follow up O(n)   1% 比较低的几率会要求O(n) 除非找人非常严格 - Rabin Karp

- ```python
  abcde   find cde
  cde
   cde
    cde
  abc => bcd 判断是否等于cde 需要O(m)一个一个字符串比较  如何加速?    如何O(1)完成字符串变换并判断是否相等?
  use hash function to map str to int      k=>v 1:1 injective
  先用个简单的方式: 进制转换方式做hash function\
  31 = magic number base   (big number) % hash size
  hash size = 10^6 越大越不易hash collision
  abcde = (a*31^4 + b*31^3 + c*31^2 + d*31 + e) % 10^6 
  避免overflow  加减乘前后的取模的结果是一样的。在实现的时候做到应模尽模就可以了 其实不会错乱结果的； 如果变成了负数 再加一遍ba se
  (a + b) % c = (a % c + b % c) % c
  (a * b) % c =(a % c) * (b % c) % c
  （其中a,b是整数）
  循环过程中的当前window hash变化 abc => bcd  增加d 删掉a 
  [ (x * 31 + d) % 10^6 - a * 31^3] % 10^6
  hashcode相等 double check是否真的想等 O(m)  总时间复杂度取决于冲突的次数 均摊O(n + m) 
  class Solution:
      """
      @param: source: A source string
      @param: target: A target string
      @return: An integer as index
      """
      def strStr2(self, source, target):
          if source is None or target is None:
              return -1
          if target == "":
              return 0
          BASE = 1000000
          m, n = len(target), len(source)
          power = 1
          # 31^m
          for i in range(m):
              power = (power * 31) % BASE
          # target
          target_code = 0
          for i in range(m):
              target_code = (target_code * 31 + ord(target[i])) % BASE
          hash_code = 0
          for i in range(n):
              #  abc +d
              hash_code = (hash_code * 31 + ord(source[i])) % BASE
              # 不够m个字符 继续
              if i < m - 1:
                  continue
              elif i >= m:
                  # abcd -a
                  #    i
                  hash_code = (hash_code - ord(source[i - m]) * power) % BASE
                  if hash_code < 0:
                      hash_code += BASE
              if hash_code == target_code:
                  if source[i - m + 1:i + 1] == target:
                      return i - m + 1
          return -1
  ```

​    

# GROUP 17 时间复杂度低于O(n)的算法

```
在上一章中，我们讲到了一个O(logn)时间复杂度的算法，二分算法。只需要O(logn)的时间就可以成功进行搜索。而我们在第四章的时候，就已经讲到了，我们可以通过时间复杂度来推测算法，当我们发现需要时间复杂度为<O(N)的算法时，我们可以考虑使用二分搜索来解决问题。但是如果题目不能用二分搜索来解决，我们该使用什么算法来解决呢？
    今天我们就来看一下几种同为logn时间复杂度的算法——快速幂算法、辗转相除法以及另外两种小于O(N)时间复杂度的算法——质因数分解和分块检索法。
```

- 快速幂 https://www.lintcode.com/problem/140/

## 辗转相除法

https://www.lintcode.com/problem/845/

### 算法介绍

辗转相除法， 又名欧几里德算法， 是求最大公约数的一种方法。它的具体做法是：用**较大的数**除以**较小的数**，再用**除数**除以出现的**余数**（第一余数），再用**第一余数**除以出现的**余数**（第二余数），如此反复，直到最后余数是0为止。如果是求两个数的最大公约数，那么最后的除数就是这两个数的最大公约数。

### 代码

Java:

```
public int gcd(int big, int small) {
    if (small != 0) {
        return gcd(small, big % small);
    } else {
        return big;
    }
}
```

Python:

```
def gcd(big, small):
    if small != 0:
        return gcd(small, big % small)
    else:
        return big
```

C++:

```
int gcd(int big, int small) {
    if (small != 0) {
        return gcd(small, big % small);
    } else {
        return big;
    }
}
```

## 两个排序数组的中位数

https://www.lintcode.com/problem/65/

### 题目描述

在两个排序数组中，求他们合并到一起之后的中位数
时间复杂度要求：O(log(n+m))，其中 n, m 分别为两个数组的长度

### 解法

1. 基于 FindKth 的算法。整体思想类似于 median of unsorted array 可以用 find kth from unsorted array 的解题思路。
2. 基于二分的方法。二分 median 的值，然后再用二分法看一下两个数组里有多少个数小于这个二分出来的值。

### 算法描述
1. 先将找中点问题转换为找第 k 小的问题，这里直接令k = (n + m) / 2。那么目标是在 logk = log((n+m)/2) = log(n+m) 的时间内找到A和B数组中从小到大第 k 个。
2. 比较 A 数组的第 k/2 小和 B 数组的第 k/2 小的数。谁小，就扔掉谁的前 k/2 个数。
3. 将目标寻找第 k 小修改为寻找第 (k-k/2) 小
4. 回到第 2 步继续做，直到 k == 1 或者 A 数组 B 数组里已经没有数了。

### F.A.Q
Q: 如何 O(1) 时间移除数组的前 k/2 个数？

A: 给两个数组一个起始位置的标记参数（相当于一个offset，偏移位），把这个起始位置 + k/2 就可以了。

Q: 不是让我们找中点么？怎么变成了找第 k 小？

A: 找第 k 小如果能在 log(k) 的时间内解决，那么找中点就可以在 log( (n+m)/2 ) 的时间内解决。

Q.如何证明谁的第 k/2 个数比较小就扔掉谁的前 k/2 个数这个理论？

A: 直观的，我们看一个例子

A=[1,3,5,7]
B=[2,4,6,8]
假如我们要找第 4 小。也就是 k = 4。算法会去比较两个数组中第 2 小的数。也就是 A[1]=3 和 B[1]=4 这两个数的大小。然后会发现，3比较小，然后就决定扔掉 A 的前 k/2 = 2 个数。也就是，接下来，需要去找

A=[5,7]
B=[2,4,6,8]
中的第 k-k/2=2 小的数。这里我们扔掉了 [1,3]，扔掉的这些数中，一定不会包含我们要找的第 4 小的数——4。因为从位置上，他们在 A 和 B合并到一起之后，都会排在 4 的前面。

抽象的证明一下：

我们需要回顾一下 Merge Two Sorted Arrays 这道题目。算法的做法是，每一次比较两个数组中比较小的数，然后谁小，谁先被拿出来，放到最后的合并结果中。那么假设 A 和 B中 A[k/2 - 1] <= B[k/2 - 1]（反之同理）。我们会决定扔掉A[0..k/2-1]，因为这些数在 A 与 B 做简单的 Merge 的过程中，会优先于目标第 k 个数现出来。为什么？因为既然A[k/2-1] <= B[k/2-1]，那么当我们用最简单的 Merge Two Sorted Arrays 的算法一个个从A和B里拿数出来的时候，当 A[k/2 - 1] 出来的时候，B[k/2 - 1] 一定还没有被拿出来，那么此时A里出来了 k/2 个数，B里出来的数一定不够 k/2 个（因为第 k/2 个数都还没出来），所以加起来总共出来的数肯定不够k个，所以第k小的数一定还留在AB数组中。

因此我们证明了：扔掉较小的一部分的前 k/2 个数，不会扔掉要找的第 k 小的数。

### 二分法 算法描述
我们需要先确定二分的上下界限，由于两个数组 A, B 均有序，所以下界为 min(A[0], B[0])，上界为 max(A[A.length - 1], B[B.length - 1]).
判断当前上下界限下的 mid(mid = (start + end) / 2) 是否为我们需要的答案；这里我们可以分别对两个数组进行二分来找到两个数组中小于等于当前 mid 的数的个数cnt1与 cnt2，sum = cnt1 + cnt2 即为 A 跟 B 合并后小于等于当前mid的数的个数.
如果 sum < k，即中位数肯定不是 mid，应该大于 mid，更新 start 为 mid，否则更新 end 为 mid，之后再重复第二步
当不满足 start + 1 < end 这个条件退出二分循环时，再分别判断一下start跟 end ，最终返回符合要求的那个数即可
### 二分法 算法详解
如果对该算法有点疑问，我们下面来详细讲解一下：

这一题如果用二分法来做，其实就是一个二分答案的过程
首先我们已经得到了上下界限，那么答案必定是在这个上下界限中的，需要实现的就是从这个歌上下界限中找出答案
我们每次取的 mid，其实就是我们每次在假设答案为 mid，二分的过程就是不断的推翻这个假设，然后再假设新的答案
需要满足的条件为：
上面算法描述中的 sum 需要等于 k，这里的 k = (A.length + B.length) / 2. 如果 sum < k，很明显当前的 mid 偏小，需要增大，否则就说明当前的 mid 偏大，需要缩小.
最终在 start 与 end 相邻的时候退出循环，判断 start 跟 end 哪个符合条件即可得到最终结果7

## 分解质因数

https://www.lintcode.com/problem/235/

以 sqrt{n} 为时间复杂度的算法并不多见，最具代表性的就是分解质因数了。

### 具体步骤

1. 记up = sqrt{n}，作为质因数k的上界, 初始化k=2。
2. 当k <= up 且 n不为1 时，执行步骤3，否则执行步骤4。
3. 当n被k整除时，不断整除并覆盖n，同时结果中记录k，直到n不能整出k为止。之后k自增，执行步骤2。
4. 当n不为1时，把n也加入结果当中，算法结束。

### 几点解释

- 不需要判定k是否为质数，如果k不为质数，且能整出n时，n早被k的因数所除。故能整除n的k必是质数。
- 为何引入up？为了优化性能。当k大于up时，k已不可能整除n，除非k是n自身。也即为何步骤4判断n是否为1，n不为1时必是比up大的质数。
- 步骤2中，也判定n是否为1，这也是为了性能，当n已为1时，可早停。

### 代码

Java:

```
public List<Integer> primeFactorization(int n) {
    List<Integer> result = new ArrayList<>();
    int up = (int) Math.sqrt(n);
    
    for (int k = 2; k <= up && n > 1; ++k) {
        while (n % k == 0) {
            n /= k;
            result.add(k);
        }
    }
    
    if (n > 1) {
        result.add(n);
    }
    
    return result;
}
```

Python:

```
def primeFactorization(n):
    result = []
    up = int(math.sqrt(n));
    
    k = 2
    while k <= up and n > 1: 
        while n % k == 0:
            n //= k
            result.append(k)
        k += 1
            
    if n > 1:
        result.append(n)
        
    return result
```

C++:

```
vector<int> primeFactorization(int n) {
    vector<int> result;
    int up = (int)sqrt(n);
    
    for (int k = 2; k <= up && n > 1; ++k) {
        while (n % k == 0) {
            n /= k;
            result.push_back(k);
        }
    }
    
    if (n > 1) {
        result.push_back(n);
    }
    
    return result;
}
```

### 复杂度分析

- 最坏时间复杂度O(sqrt (n) )。当n为质数时，取到其最坏时间复杂度。
- 空间复杂度O(log(n)), 当n质因数很多时，需要空间大，但总不会多于O(log(n))个

### 延伸

质因数分解有一种更快的算法，叫做Pollard Rho快速因数分解。该算法时间复杂度为O(n^{1/4})，其理解起来稍有难度，有兴趣的同学可以进行自学，[参考链接](https://wenku.baidu.com/view/3db5c7a6ad51f01dc381f156.html)。

## 分块检索

https://www.lintcode.com/problem/249/

```
在数组中，二分找到插入位置，将需要插入的数字插入到该位置中，时间复杂度是多少。
二分的时间复杂度是O(logn),但是在某个位置上插入一个元素需要把其之后的所有元素往后移动，时间复杂度是O(N)级别的。因此，总时间复杂度是O(n+logn), 即O(n).
能不能通过链表，使得每次插入一个数字后，二分找到这个数字所在的位置，并O(1)进行插入，这样插入的时间复杂度就会变成O(logn)?
虽然改成链表能够将插入的时间复杂度降低到O(1),但是链表上是没法二分的，因为链表无法按下标访问，时间复杂度仍然是O(N)
分块检索的优化版本——线段树算法
```











