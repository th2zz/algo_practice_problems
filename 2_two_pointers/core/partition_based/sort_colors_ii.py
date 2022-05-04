class Solution:
    """
    Description
    Given an array of n objects with k different colors (numbered from 1 to k),
    sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

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
    partition + 递归分治 先整体有序再局部有序
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

