class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we store both strings as lists and sort them
        # so that if they are an anagram, they would contain
        # the same elements in the same order
        slist = list(s)
        tlist = list(t)
        slist.sort()
        tlist.sort()
        if slist == tlist:
            return True
        else:
            return False

