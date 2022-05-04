
class Solution:  # https://leetcode-cn.com/problems/combination-sum/
    """
给定一个无重复candidates列表 一个目标int, 返回能够sum to target的无重复组合 (可以以任何顺序返回)
同一个数可以被重复选中无限次,
find all unique combs that sum to target, dup choice ok

stop condition: sums to target / remaining target=0
                                                           []  target=7
				                       / pick2            \ pick3                \6,E      \7,S
			                      [2],5                  [3],4
		                   / pick2  \ pick3          / pick3  \ do not pick 3,E
	                 [2,2],3      [2,3],2,E  [3.3],1,E    
				/ pick2 \ pick3             
	[2,2,2],1,E             [2,2,3],0,S  
			
choose candidate in order, cannot choose **backward**
E: remainTarget<all remain candidate. no choice / no solution
S: solution!

    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        result = []
        self.dfs(candidates=sorted(list(set(candidates))), start_idx=0, target=target, comb=[], result=result)  # do not sort place
        return result

    # 组合的dfs一般是index based, 排列一般需要visited set
    def dfs(self, candidates, start_idx, target, comb, result):  # 找到以comb位前缀 sum to target的无重复组合
        if target == 0:
            result.append(list(comb))  # deep copy
            return
        for i in range(start_idx, len(candidates)):  # no looking back on candidate choice
            if candidates[i] > target:
                return  # no need to look after this
            comb.append(candidates[i])
            self.dfs(candidates, i, target - candidates[i], comb, result)  # recurse start from i
            comb.pop()



class Solution2:
    """https://www.lintcode.com/problem/135/?_from=collection&fromId=161
    Description
Given a set of candidate numbers candidates and a target number target. Find all unique combinations in candidates
where the numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

All numbers (including target) will be positive integers.
Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
Different combinations can be in any order.
The solution set must not contain duplicate combinations.
Example
Example 1:

Input: candidates = [2, 3, 6, 7], target = 7
Output: [[7], [2, 2, 3]]
Example 2:

Input: candidates = [1], target = 3
Output: [[1, 1, 1]]
给定一个数集 和 目标数 求所有能够sums to target的独特的组合； 候选数集中 数可以选无限次    组合必须为不下降序列
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    """ 搜索树
            2
       /  |  |  \
       22 23 26 27                        23 children: 233 236 237
    222 223  没有226 227 (可行性剪枝)   
    排序并去重candidates
    递归的定义 每一次递归调用 从candidates start_idx位置开始(inclusive 这样实现“可重复选同个数”) 往后看 找到能够sum to remaining target的组合
    可行性剪枝 如果当前剩余需满足target不足 break 后面没必要看了 因为candidate是sorted
    尝试将当前candidate 加入组合 递归解决子问题: 以新的comb为前缀 sum to target - candidates[i]的组合
        dfs(candidates, i, comb, target - candidates[i], res)
        因为candidates已经排序了, 这里的i是为了实现 不降序的 可重复的选择 只看刚选的以及剩余的candidates
        最上层 循环递归调用 实际上在 求解 不同的candidate为curr_comb的开始的所有组合  
        递归过程中
            如果sum to target存在 且找得到 则一定会返回  因为我们每次都向出口递进
            如果不存在 则大循环会退出并返回  
            递归的拆解 按不降序 尝试过当前candidate后回溯 去尝试下一个candidate
        这样数可以不重不漏; 
    
    """

    def combinationSum(self, candidates, target):
        res = []
        if not candidates:
            return res
        self.dfs(sorted(list(set(candidates))), 0, [], target, res)  # TODO 去重加排序 保证组合不降序 选择的时候也不降序的选
        return res

    def dfs(self, candidates, start_idx, comb, target, res):  # 递归的定义: 在candidate start_idx位置开始 找到所有以comb为前缀 sum to target的组合
        if target == 0:  # 递归的出口 remaining sum target = 0 构造出了一组解
            res.append(list(comb))  # TODO deep copy, otherwise modifying current may change res
            return
        for i in range(start_idx, len(candidates)):  # 递归的拆解和递进: 从当前位置开始,逐个尝试candidate中元素 加到comb中 并递归解决子问题: 以新的comb为前缀 sum to target - candidates[i]的组合
            if candidates[i] > target:  # pruning 后面不用看了 因为candidates是sorted
                return
            comb.append(candidates[i])  # dfs recurse on remaining problem, i没有变化 代表选过的仍然可以再选
            self.dfs(candidates, i, comb, target - candidates[i], res)
            comb.pop()  # backtrack latest try on candidates[i], target is call by value
