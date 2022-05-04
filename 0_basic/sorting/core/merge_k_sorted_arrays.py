class Solution:
    """https://www.lintcode.com/problem/486/
    N is the total number of integers.
    k is the number of arrays.
    assume m = expected length of an array << N
    掌握 解法1 类似归并排序 分治解决左半边 右半边 合并左右两个数组, 复用归并排序中merge 2 sorted array
    复杂度: time： k个数组 log2k次取中点 reach base case start == end 递归树logk层  对于第j层来说 有2^j个子问题 子问题规模k/2^j个数组
    假设期望长度m=N/k     在第j层一个子问题中merge 2半边需要 O(km/2^j) 整个j层O(km) 整个树O(kmlogk) = O(Nlogk)
    space: O(Nlogk + k) Nlogk同时间 每层O(km), 栈空间取决于多少次递归调用 2+4+。。。+k/2  (1-2^k/2)/-1


    掌握 OPTIMAL 解法2 k路归并with minheap， heap entry (arr[i], array#, i) array当前元素值, array编号, array内当前index
        先klogk建堆: 每个非空array[0]相关3元组入堆
        只要堆非空 循环poll one item消费 取出arr[i] append到结果中
        只要i还未越界 入堆此array下一个heap entry (arr[i+1], array#, i+1)
    复杂度: O(NlogK) O(k) with heapq 因为每个元素只被push & pop一遍 只会有k个entry

    解法3 持续迭代法 每一轮两两相邻合并并准备下一轮迭代用 arrays 直到收敛为1个大数组
    复杂度: O(NlogK); Space O(NlogN) 每轮两两合并O(N)

Given k sorted integer arrays, merge them into one sorted array.
Example
Example 1:

Input:
  [
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
  ]
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Example 2:

Input:
  [
    [1,2,3],
    [1,2]
  ]
Output: [1,1,2,2,3]

Challenge
Do it in O(N log k).



Tags Heap, Sort
Related Problems
- 839 Merge Two Sorted Interval Lists Easy
- 104 Merge K Sorted Lists Medium

    @param arrays: k sorted integer arrays
    @return: a sorted array


外排序算法分为两个基本步骤：

- 将大文件切分为若干个个小文件，并分别使用内存排好序
- 使用K路归并算法（k-way merge）将若干个排好序的小文件合并到一个大文件中

第一步：文件拆分
根据内存的大小，尽可能多的分批次的将数据 Load 到内存中，并使用系统自带的内存排序函数（或者自己写个快速排序算法），将其排好序，
并输出到一个个小文件中。比如一个文件有1T，内存有1G，那么我们就这个大文件中的内容按照 1G 的大小，
分批次的导入内存，排序之后输出得到 1024 个 1G 的有序小文件。

第二步：K路归并算法
K路归并算法使用的是数据结构堆（Heap）来完成的

我们将 K 个文件中的第一个元素加入到堆里，假设数据是从小到大排序的话，那么这个堆是一个最小堆（Min Heap）。每次从堆中选出最小的元素，
输出到目标结果文件中，然后如果这个元素来自第 x 个文件，则从第 x 个文件中继续读入一个新的数进来放到堆里，
并重复上述操作，直到所有元素都被输出到目标结果文件中。

Follow up: 一个个从文件中读入数据，一个个输出到目标文件中操作很慢，如何优化？
如果我们每个文件只读入1个元素并放入堆里的话，总共只用到了 1024 个元素，这很小，没有充分的利用好内存, 内存利用率低。
另外，单个读入和单个输出的方式也不是磁盘的高效使用方式。因此我们可以为输入和输出都分别加入一个缓冲（Buffer）。
假如一个元素有10个字节大小的话，1024 个元素一共 10K，1G的内存可以支持约 100K 组这样的数据，
那么我们就为每个文件设置一个 100K 大小的 Buffer， 每次需要从某个文件中读数据，都将这个 Buffer 装满。
当然 Buffer 中的数据都用完的时候，再批量的从文件中读入。输出同理，设置一个 Buffer 来避免单个输出带来的效率缓慢。
    """

    # DIVIDE AND CONQUER TOP DOWN
    def mergekSortedArrays(self, arrays):
        return self.merge_helper(arrays, 0, len(arrays) - 1)

    def merge2SortedArrays(self, A, B):  # same one in merge sort
        i, j, n, m = 0, 0, len(A) - 1, len(B) - 1
        res = []
        while i <= n and j <= m:
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            elif A[i] >= B[j]:
                res.append(B[j])
                j += 1
        if i <= n:
            res.extend(A[i:])
        if j <= m:
            res.extend(B[j:])
        return res

    def merge_helper(self, arrays, start, end):  # merge arrays from start to end
        if start == end:  # base case 1 array, no merge
            return arrays[start]
        mid = (start + end) // 2  # start + (end - start) // 2
        left = self.merge_helper(arrays, start, mid)
        right = self.merge_helper(arrays, mid + 1, end)
        return self.merge2SortedArrays(left, right)  # merge left and right res

    # bottom up iteration: merge 2 arrays at a time till converge
    def mergekSortedArrays2(self, arrays):  # O(NlogK); Space O(NlogN) 每轮两两合并O(N)
        while len(arrays) > 1:  # converge condition
            next_arrays = []
            for i in range(0, len(arrays), 2):  # 两两相邻合并
                if i + 1 < len(arrays):  # if not exceed bound, merge neighboring array
                    array = self.merge2SortedArrays(arrays[i], arrays[i + 1])
                else:  # exceed bound = there is only one left
                    array = arrays[i]
                next_arrays.append(array)  # 把本轮合并完的加进去下轮迭代用的"arrays", 下一轮迭代用的"arrays"规模变小了
            arrays = next_arrays  # 设置下轮迭代用的"arrays"
        return arrays[0]  # result

    # optimal: O(NlogK) O(k) with heapq 因为每个元素只被push & pop一遍 只会有k个entry
    def mergekSortedArrays2(self, arrays):
        import heapq
        result = []
        heap = []
        # heap 排序: 优先按array内当前元素大小排序 其次按array索引 array内位置索引排序
        # klogk 建堆 把每个数组第一个值入堆 只考虑非空数组
        for i, arr in enumerate(arrays):
            if arr:
                heapq.heappush(heap, (arr[0], i, 0))  # 当前array当前位置元素值, array编号(当前), 当前array内当前元素位置索引
                # similar to merge 2 sorted array,
                # 这代表排序优先级 优先按当前值大小
                # 再按array编号 相同最小值 优先取前面的array
                # 再按array内部位置 相同最小值 相同array 优先取前面的位置
                # 或者说 不同数组优先按当前位置最小值取 同一个数组内优先取前面位置
        while heap:  # 循环消费 把当前消费的数组下个元素入堆
            curr_val, arr_idx, curr_val_idx = heapq.heappop(heap)  # fetch smallest element
            curr_arr = arrays[arr_idx]
            result.append(curr_val)  # build merged res by adding current smallest element
            if curr_val_idx + 1 < len(curr_arr):  # insert next triple that has a next element in this array
                heapq.heappush(heap, (curr_arr[curr_val_idx + 1], arr_idx, curr_val_idx + 1))
        return result
