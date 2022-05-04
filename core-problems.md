# Table of contents

- [Intro](#intro)
- [High Priority Problems list](#high-priority-problems-list)
  - [Essential Data structures](#essential-data-structures)
    - [array](#array)
    - [prefix/suffix array](#prefixsuffix-array)
    - [Hashmap](#hashmap)
    - [LinkedList](#linkedlist)
    - [Heap, Sorting, Order statistics](#heap-sorting-order-statistics)
    - [Intervals / Tuples](#intervals--tuples)
    - [Matrix / 2D Arrays](#matrix--2d-arrays)
    - [Stack & Queue](#stack--queue)
    - [Trie](#trie)
  - [Algorithms and Pattern](#algorithms-and-pattern)
    - [Two pointers](#two-pointers)
    - [Binary Search](#binary-search)
    - [BFS, Connectivity, Topological Sort](#bfs-connectivity-topological-sort)
    - [DFS, Memoized Search](#dfs-memoized-search)
    - [Tree: divide and conquer](#tree-divide-and-conquer)
    - [String](#string)
    - [DP](#dp)
    - [Monotonic Stack/Queue](#monotonic-stackqueue)
- [Low priority Problems list](#low-priority-problems-list)
  - [Bit Manipulation](#bit-manipulation)
  - [Greedy](#greedy)
  - [Union Find](#union-find)
  - [Graph Algorithm](#graph-algorithm)

# Intro

use ✓X to mark a problem needs some review.

- order of importance
  - Array, Prefix / Suffix Array, Stack & Queue, HashMap
  - Two pointers
  - Binary Search
  - LinkedList
  - String
  - Intervals / Tuples
  - Matrix / 2D Arrays
  - BFS, Connectivity, Topological Sort
  - Tree
  - DFS, Memoized Search
  - Monotonic Stack/Queue
  - Heap, order statistics
  - DP

# High Priority Problems list

## Essential Data structures

### array

| problems                                 | problem formulation                                                                         | need review | big idea                                                                                                                                                                                                                                         | link                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| Find All Numbers Disappeared in an Array | input: [n]int s.t. arr[i] in range [1,n] find all natural numbers not in array in O(n) O(1) | ✓ 10/3      | 遍历数组 用值的绝对值-1 做索引 在原数组对应位置上通过变负数标记数 index+1 是否存在 第二次遍历发现正数其 index+1 加到结果                                                                                                                         | https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/ |
| Majority Element                         | find majority element in an array in O(n) (找众数)                                          | X 10/9      | loop to pick a random index and count to check if nums[index] appears at least n/2 times. <br /> Expected #times to pick a majority element = 2, counting to see if is a majority element = O(n) worst case. <br /> Overall O(n) O(1) on average | https://leetcode.cn/problems/majority-element/                         |

### prefix/suffix array

| problems                     | problem formulation                                      | need review | big idea                                                                                                                                                                                                                                                                                                                                                                                                                            | link                                                           |
| ---------------------------- | -------------------------------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Product of Array Except Self | return an array of product of each element except itself | ✓ 9/30      | O(n) space time keep 1 prefix product array 1 suffix product array, compute based on stored info. <br /> Follow up O(1) space: use a single variable for recording up-to-date suffix product, overwrite pre-computed prefix-product array and return as result                                                                                                                                                                      | https://leetcode-cn.com/problems/product-of-array-except-self/ |
| Subarray Sum Equals K        | find # contiguous subarrays that sum to K                | ✓ 10/2      | brute-force O(n^2) Time O(1) Space enumerate start & finish, check if current prefixSum==k, reset sum for new subarray start; <br /> O(n) O(n) 前缀和解法 Traverse input array, use past state dual m[PrefixSum-K] to count like 2Sum, increment current m[prefixSum] counts each loop <br/> use map to store { prefixSum : prefixSum counts}: <br/> special init case m[0]=1 when prefixSum-k=0 is not in array. e.g. [1,1,1] k=2, | https://leetcode.cn/problems/subarray-sum-equals-k/            |

### Hashmap

| problems                     | problem formulation                                                                 | need review | big idea                                                                                                                                                                                                                                                        | link                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Contains Duplicate           | returns true if there is any duplicate in a list                                    | X 9/30      | use a set to mark visited                                                                                                                                                                                                                                       | https://leetcode-cn.com/problems/contains-duplicate/       |
| Longest Consecutive Sequence | find the length of the longest consecutive sequence from an unordered array in O(n) | X 10/9      | O(n) 准备一个 set 将 nums 中数全部添加进去 提供 O(1) 存在查询, 去重<br/>遍历 set 数字:遍历可能的子序列起点 (如果一个数 num 前一个数 num-1 不在集合中 说明他不属于任何连续序列 也就是可以为一个起点)<br/>从此数开始计数子序列长度 1 个 1 个数 打擂台记录最大长度 | https://leetcode.cn/problems/longest-consecutive-sequence/ |

### LinkedList

reorder list, Sort List, Palindrome Linked List, Merge k Sorted Lists 其实都是一道题

| problems                         | problem formulation                                                                     | need review | big idea                                                                                                              | link                                                           |
| -------------------------------- | --------------------------------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| reorder list                     | 交叉重排链表使得 L0 → L1 → … → Ln - 1 → Ln 变为 L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → … | ✓ 10/12     | 快慢指针找到链表偏左中点, 拆分 2 个链表, reverse l2 后合并(interleave)到 l1 里                                        | https://leetcode.cn/problems/reorder-list/                     |
| Sort List                        | sort a linkedlist                                                                       | ✓           | O(nlogn)和 O(1) 类似 merge sort 快慢指针切分链表找到右半开始 递归解决左右半边 合并左右半边结果                        | https://leetcode.cn/problems/sort-list                         |
| Palindrome Linked List           | check if a linkedlist is a palindrome                                                   | ✓           | 找到前半部分链表的尾节点并反转后半部分链表,同向双指针同速前进判断是否回文,还原链表并返回结果                          | https://leetcode.cn/problems/palindrome-linked-list/           |
| Merge k Sorted Lists             | merge k sorted linkedlists                                                              | ✓           | like merge sort, O(Nlogk) O(logk) better space than priority queue solution                                           | https://leetcode.com/problems/merge-k-sorted-lists/            |
| LRU cache                        | implement LRU cache                                                                     | ✓ 10/12     | O(1) average get put                                                                                                  | https://leetcode.cn/problems/lru-cache/                        |
| Linked List Cycle II             | find cycle start point                                                                  | ✓ 10/12     | 快慢指针确定有环后 break 重置 slow 同步同速前进直到 slow 追上 fast, 相遇点即为环的起点                                | https://leetcode.cn/problems/linked-list-cycle-ii/             |
| remove nth node from end of list | 删掉链表倒数第 n 个节点                                                                 | ✓ 10/12     | 2-pass=数链表长度; 1-pass pt1=dummy pt2=head pt2 先走 n 步,再同时前进,这样当 pt2 为 none 时 pt1 为要删节点前一个节点; | https://leetcode.cn/problems/remove-nth-node-from-end-of-list/ |
| Intersection of Two Linked Lists | find intersection of two linkedlist                                                     | ✓ 10/12     | a+b-c=b+a-c while A!=B 同向双指针遍历完自己部分 遍历另一边开始到交点部分                                              | https://leetcode.cn/problems/intersection-of-two-linked-lists/ |
| Add Two Numbers                  | add two numbers represented in linkedlists                                              | X 10/12     | 先取出两个链表表示的数,然后将结果构建为链表                                                                           | https://leetcode.cn/problems/add-two-numbers/                  |
| Reverse Linked List              | reverse a linkedlist                                                                    | X           | keep [prev, cur] ptrs, reverse node by node                                                                           | https://leetcode.cn/problems/reverse-linked-list/              |
| Linked List Cycle                | detect cycle in a linkedlist                                                            | X           | slow(1step) & fast(2step) ptrs meet = has cycle                                                                       | https://leetcode.cn/problems/linked-list-cycle/                |

### Heap, Sorting, Order statistics

| problems                            | problem formulation                                 | need review | big idea                                                                 | link                                                          |
| ----------------------------------- | --------------------------------------------------- | ----------- | ------------------------------------------------------------------------ | ------------------------------------------------------------- |
| Top K Frequent Elements             | find topk frequent elements in an array in O(nlogn) | ✓           | 用 fixed size k-minheap 解决 topk 问题, add 时超过容量淘汰一个最小值出去 | https://leetcode.cn/problems/top-k-frequent-elements/         |
| Kth Largest Element in an Array     | find kth largest element in an array in O(n)        | ✓           | O(n)O(1) quick select with partition                                     | https://leetcode.cn/problems/kth-largest-element-in-an-array/ |
| Find Median from Data Stream [Hard] |                                                     |             |                                                                          | https://leetcode.cn/problems/find-median-from-data-stream/    |

### Intervals / Tuples

| problems                  | problem formulation                                                                                                             | need review | big idea                                                           | link                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------ | -------------------------------------------------------- |
| Meeting Rooms II          | 求满足所有会议最少需要会议室数量 min#rooms to accomodate all meetings                                                           | ✓           |                                                                    | https://leetcode.cn/problems/meeting-rooms-ii/           |
| Merge Intervals           | merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input | ✓           |                                                                    | https://leetcode.cn/problems/merge-intervals/            |
| Non-overlapping Intervals | return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.                    | ✓           |                                                                    | https://leetcode.cn/problems/non-overlapping-intervals// |
| Insert Interval           | insert interval into a list of intervals s.t. orignal properties are preserved : non-overlapping, sorted by start_i             | ✓           |                                                                    | https://leetcode.cn/problems/insert-interval/            |
| Meeting Rooms             | find if we can attend all meetings in a schedule                                                                                |             | 遍历 从第一个开始 相邻的作比较 overlap return False otherwise True | https://leetcode.cn/problems/meeting-rooms/              |

### Matrix / 2D Arrays

| problems          | problem formulation                                            | need review | big idea | link                                            |
| ----------------- | -------------------------------------------------------------- | ----------- | -------- | ----------------------------------------------- |
| Rotate Image      | rotate the matrix 90 degrees clockwise in-place                | ✓           |          | https://leetcode.cn/problems/rotate-image/      |
| Spiral Matrix     | return all elements of the matrix in spiral order (clockwise). | ✓           |          | https://leetcode.cn/problems/spiral-matrix/     |
| Set Matrix Zeroes | if matrix[i][j] == 0 clear row i col j in-place                | ✓           |          | https://leetcode.cn/problems/set-matrix-zeroes/ |

### Stack & Queue

| problems          | problem formulation                                                                | need review | big idea                                                                                                                                                                                                                                                                 | link                                            |
| ----------------- | ---------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| Valid Parentheses | input: a string that only contains (){}[], check if the string is well-formed      | ✓           | use map r2l (right parenthese: left parenthese), traverse string char by char <br /> c = }]): top of the stack should be left and they should match & pop stack top left paren <br/> c = otherwise (left parenthese...): push to stack <br/> All match = len(stack) == 0 | https://leetcode.cn/problems/valid-parentheses/ |
| Decode String     | decode a run-length encoded string. can have nested/composite format like 2[2[cb]] | ✓           | 遍历字符串 s s[i]不是右括号: 当前子问题未完 直接入栈 是右括号: 需要展开整个 k[...] 先构建括号内字串(栈顶!=[就继续) 然后 pop 栈顶[, 再构建倍数 k (栈顶 isdigit 就继续) 将 k 个构建好的 substr 重新入栈开始下轮迭代; <br/> 返回整个 stack 拼接起来的字符串                 | https://leetcode.cn/problems/decode-string/     |
| Min Stack         | Implement a stack that supports O(1) push pop top getMin                           | ✓           | use tuple (val, minimum val at push time) (x, min(x, self.stack[-1][1])) as stack basic element <br /> O(1) space 做法: 栈上保存 push 时 val 与当时 min 的差值                                                                                                           | https://leetcode.cn/problems/min-stack/         |

### Trie

| problems                     | problem formulation | need review | big idea                                                                           | link                                                    |
| ---------------------------- | ------------------- | ----------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Implement Trie (Prefix Tree) | Implement trie      | ✓           | TrieNode 属性 children:map[char]TrieNode, cnt:how many words end here, parent 指针 | https://leetcode.cn/problems/implement-trie-prefix-tree |

## Algorithms and Pattern

### Two pointers

```
Container With Most Water
3Sum
Two Sum
Move Zeroes
Sort Colors
Find the Duplicate Number
```

### Binary Search

```
Search in Rotated Sorted Array
Find Minimum in Rotated Sorted Array
Find First and Last Position of Element in Sorted Array
Search a 2D Matrix II https://leetcode.cn/problems/search-a-2d-matrix/
```

hard

```
Median of Two Sorted Arrays
```

### BFS, Connectivity, Topological Sort

```
Course Schedule
Clone Graph
Number of Connected Components in an Undirected Graph (Leetcode Premium)
Number of Islands
Pacific Atlantic Water Flow
Alien Dictionary
Evaluate Division
Perfect Squares https://leetcode.cn/problems/perfect-squares/
```

Hard

```
Remove Invalid Parentheses

```

### DFS, Memoized Search

```
Generate Parentheses
Combination Sum
Word Search II
Subsets
Permutations
Letter Combinations of a Phone Number
Regular Expression Matching
```

### Tree: divide and conquer

```
Binary Tree Inorder Traversal
Binary Tree Level Order Traversal
Binary Tree Maximum Path Sum
Kth Smallest Element in a BST
Convert BST to Greater Tree
Construct Binary Tree from Preorder and Inorder Traversal
Diameter of Binary Tree
Invert Binary Tree
Flatten Binary Tree to Linked List
Graph Valid Tree (Leetcode Premium)
Lowest Common Ancestor of BST
Lowest Common Ancestor of a Binary Tree
Maximum Depth of Binary Tree
Same Tree
Subtree of Another Tree
Unique Binary Search Trees
Serialize and Deserialize Binary Tree
Merge Two Binary Trees
Symmetric Tree
Validate Binary Search Tree
Design Add and Search Words Data Structure
Path Sum III  https://leetcode.cn/problems/path-sum-iii/
```

### String

https://leetcode.cn/problems/find-all-anagrams-in-a-string/solution/hua-dong-chuang-kou-tong-yong-si-xiang-jie-jue-zi-/

| problems                                       | problem formulation                                                                                            | need review | big idea                                                                                                                                                                                                               | link                                                                         |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Longest Substring Without Repeating Characters |                                                                                                                | ✓           | 滑动窗口                                                                                                                                                                                                               | https://leetcode.cn/problems/longest-substring-without-repeating-characters/ |
| Longest Repeating Character Replacement        |                                                                                                                | ✓           | 滑动窗口                                                                                                                                                                                                               | https://leetcode.cn/problems/longest-repeating-character-replacement/        |
| Find All Anagrams in a String                  | given a str, find all instances of its anagram in itself and return list[int] a list of anagram starting index |             | 滑动窗口                                                                                                                                                                                                               | https://leetcode.cn/problems/find-all-anagrams-in-a-string/                  |
| Group Anagrams                                 | given list[str], group anagrams together return list[list[str]]                                                | ✓           | n=#strs k=max len str Σ=字符集 <br/>用排序好的单词做 key 将不同 anagrams 加到桶中 O(nklogk) O(nk)<br/> 每个字符串做字符频次统计并将这个信息做为 hash key 同为 anagrams 的话这个是一致的 复杂度 O(n(k+\|Σ\|))space&time | https://leetcode.cn/problems/group-anagrams/                                 |
| Valid Anagram                                  | given 2 str, check if they are anagrams (letters reranged in different order)                                  | X           | sort O(nlogn) O(logn), compare frequencies / 第二个字符串在第一个字符串统计的频率表上做差                                                                                                                              | https://leetcode.cn/problems/valid-anagram/                                  |
| Valid Palindrome                               |                                                                                                                | ✓           |                                                                                                                                                                                                                        | https://leetcode.cn/problems/valid-palindrome/                               |

More

```
Minimum Window Substring [Hard] https://leetcode.cn/problems/minimum-window-substring/
Encode and Decode Strings (Leetcode Premium)
```

### DP

```
Coin Change
Best Time to Buy and Sell Stock
Best Time to Buy and Sell Stock with Cooldown
Climbing Stairs
House Robber
House Robber II
House Robber III
Jump Game
Longest Common Subsequence
Longest Increasing Subsequence
Maximum Product Subarray
Maximum Subarray
Unique Paths
Decode Ways
Edit Distance
Word Break
Partition Equal Subset Sum https://leetcode.cn/problems/partition-equal-subset-sum/
Palindromic Substrings  https://leetcode.cn/problems/palindromic-substrings/
Longest Palindromic Substring
Maximal Square   https://leetcode.cn/problems/maximal-square/
Target Sum https://leetcode.cn/problems/target-sum/
Minimum Path Sum https://leetcode.cn/problems/minimum-path-sum/

```

hard

```
Burst Balloons
Longest Valid Parentheses https://leetcode.cn/problems/longest-valid-parentheses/

```

### Monotonic Stack/Queue

```
Daily Temperatures
Trapping Rain Water
Shortest Unsorted Continuous Subarray  https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/
```

hard

```
Largest Rectangle in Histogram https://leetcode.cn/problems/largest-rectangle-in-histogram/
Sliding Window Maximum
Maximal Rectangle https://leetcode.cn/problems/maximal-rectangle/
```

# Low priority Problems list

## Bit Manipulation

```
Hamming Distance
Reverse Bits
Missing Number
Number of 1 Bits
Sum of Two Integers
Counting Bits
Single Number https://leetcode.cn/problems/single-number/

```

## Greedy

```
Queue Reconstruction by Height https://leetcode.cn/problems/queue-reconstruction-by-height/

Task Scheduler https://leetcode.cn/problems/task-scheduler/

```

## Union Find

```

```

## Graph Algorithm

MST, Dijkstra, ...
