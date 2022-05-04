class Solution:
    # https://leetcode.cn/problems/group-anagrams/
    # 通过词频做tuple key来当作hashmap  O(N*K) Timespace
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            mp[tuple(counts)].append(
                st
            )  # 需要将 list 转换成 immutable tuple 才能进行哈希
        return list(mp.values())

    # 通过排序后的单词当hash key;适合单词较短情况 O(N*K*logK) O(NK)
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in table:
                table[sorted_word] = [word]  # init, add word to anagram group
            else:
                table[sorted_word].append(word)  # add to anagram group
        return list(table.values())
