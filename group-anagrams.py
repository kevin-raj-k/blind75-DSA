class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we store the count of characters of each word 
        # and join similar ones together
        # return the entire list
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())