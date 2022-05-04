class Solution:
    """ sort string by quick sort
    https://www.lintcode.com/problem/string-sorting/
    @param s: string
    @return: sort string in lexicographical order
    """
    def swap(self, left, right, strings):
        tmp = strings[left]
        strings[left] = strings[right]
        strings[right] = tmp

    def sorting(self, s):
        # reduce the problem to standard quick sorting
        strings = s.split(',')
        self.qsort(0, len(strings) - 1, strings)
        return ','.join(strings)

    def partition(self, start, end, strings):
        left, right = start, end
        pivot = strings[(left + right) // 2]
        while left <= right:
            # two ptr move inward: skip elements that are already in order relative to pivot
            while left <= right and strings[left] < pivot:  # TODO < 快速排序partition只需要 左边整体<=右边 =pivot情况既不属于左也不属于右 使用<> =pivot的情况会比较平均的分配到左右
                left += 1
            while left <= right and strings[right] > pivot:  # TODO > 如果放=的情况严格划分到左或右 会退化到n^2 e.g. [1111]pivot=1 partition的非常偏 递归下来是个等差数列=O(n^2)
                right -= 1
            if left <= right:
                # swap this pair of inversion and move ptr
                self.swap(left, right, strings)
                left += 1
                right -= 1
        return left, right # 终止时 left > right

    def qsort(self, start, end, strings):  # O(NlogN) inplace O(1) not stable
        if start >= end:
            return
        # use separate variables to preserve original information
        left, right = self.partition(start, end, strings)
        # 此时 two sublists = [start...right][left...end]
        self.qsort(start, right, strings)
        self.qsort(left, end, strings)


res = Solution().sorting("bb,aa,lintcode,c")
print(res)
