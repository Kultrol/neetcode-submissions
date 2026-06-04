class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash_table = {} # Instantiate the hash-table
        for i in range(0, len(nums)): # Populate the hash table
            if nums[i] in nums_hash_table: #Keys are the numbers and values are arrays that contain the indicies in which those values appear in nums
                nums_hash_table[nums[i]].append(i)
            else:
                nums_hash_table[nums[i]] = [i]
        
        for i in range(0, len(nums)):
            num_diff = target - nums[i]
            
            
            if num_diff in nums_hash_table:
                if num_diff == nums[i] and len(nums_hash_table[nums[i]]) > 1:
                    return [nums_hash_table[nums[i]][0],nums_hash_table[nums[i]][1]]
                
                if nums_hash_table[num_diff][0] > nums_hash_table[nums[i]][0]:
                    return [nums_hash_table[nums[i]][0],nums_hash_table[num_diff][0]]
                elif nums_hash_table[num_diff][0] < nums_hash_table[nums[i]][0]:
                    return [nums_hash_table[num_diff][0],nums_hash_table[nums[i]][0]]
        
        #print(nums_hash_table)
            

            
       
            
        