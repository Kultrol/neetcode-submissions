class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        # Step 1: Instantiate and Populate hash table
        # The keys are the numbers found in nums
        # The values are arrays whose elements are the indicies in which the associated key is found within the nums list.
        # This step takes len(nums) steps.
        nums_hash_table = {} 
        for i in range(0, len(nums)):
            if nums[i] in nums_hash_table: 
                nums_hash_table[nums[i]].append(i)
            else:
                nums_hash_table[nums[i]] = [i]
        
        # Step 2: Finding and returning the index pair.
        # This step takes(at most) len(nums) steps.
        for i in range(0, len(nums)):
            num_diff = target - nums[i]
            

            
            if num_diff in nums_hash_table:
                num_diff_list = nums_hash_table[num_diff]
                if num_diff == nums[i] and len(num_diff_list) > 1:
                    return [num_diff_list[0],num_diff_list[1]]
                
                num_list = nums_hash_table[nums[i]]
                if num_diff_list[0] > num_list[0]:
                    return [num_list[0],num_diff_list[0]]
                elif nums_hash_table[num_diff][0] < nums_hash_table[nums[i]][0]:
                    return [num_diff_list [0], num_list[0]]
        
        
            

            
       
            
        