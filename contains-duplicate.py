class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we store the result list as a set 
        # because it does not store duplicates
        result_list = set()
        for i in nums:
            if i in result_list:
                return True
            else:
                result_list.add(i)
        return False