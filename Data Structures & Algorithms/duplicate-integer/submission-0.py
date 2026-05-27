class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_length = len(nums)

        nums_hash_table = {}
        for i in range(0,nums_length):
            if nums_hash_table.get(f"{nums[i]}") is True:
                return True
            nums_hash_table[f"{nums[i]}"] = True
        
        return False