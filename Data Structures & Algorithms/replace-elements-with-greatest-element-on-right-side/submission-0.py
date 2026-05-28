class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        replaced_arr = []

        for i in range(1, len(arr)):
            temp = arr[i:]
            #print(f"Temp: {temp}")
            temp.sort(reverse=True)
            #print(f"Sorted Temp: {temp}")
            #print(f"Max_value: {temp[0]}")
            num_a = temp[0]
            replaced_arr.append(num_a)

        replaced_arr.append(-1)

        return replaced_arr