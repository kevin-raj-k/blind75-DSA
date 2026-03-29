def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap to store values and their index
        prevMap = {} 
        
        # iterate over all elements of the list
        for i, n in enumerate(nums):
            diff = target - n
            # look for difference in the hashmap, if found returns index of current element and diff index
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i