class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_table = {}
        freq = [[] for i in range(len(nums) + 1)]


        for num in nums:
            if number_table.get(num, None) is None:
                number_table[num] = 1
            else:
                number_table[num] += 1

        for num, frequency in number_table.items():
            freq[frequency].append(num)
            
        #print(freq)
        k_lim = k
        k_freq = []
        for i in range(len(freq)-1, 0, -1):
            if freq[i] == []:
                continue

            for j in freq[i]:
                if k_lim > 0:
                    k_freq.append(j)
                    k_lim -= 1
                else:
                    break
            



        return k_freq

