import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:  # find all anagrams of pattern p in s, return list of start idx
        res = []
        left = 0
        right = 0
        matched = 0
        window = collections.defaultdict(int)
        pattern_char_freq_map = {c: p.count(c) for c in p}

        while right < len(s):
            cr = s[right]
            if cr in pattern_char_freq_map.keys():
                window[cr] += 1
                if window[cr] == pattern_char_freq_map[cr]:
                    matched += 1
            right += 1

            while matched == len(pattern_char_freq_map):
                if right - left == len(p):
                    res.append(left)
                cl = s[left]
                if cl in pattern_char_freq_map.keys():
                    window[cl] -= 1
                    if window[cl] < pattern_char_freq_map[cl]:
                        matched -= 1
                left += 1
        return res
