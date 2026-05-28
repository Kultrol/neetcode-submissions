class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        replaced_arr = []

        for i in range(1, len(arr)):
            temp = arr[i:]
            temp.sort(reverse=True)
            num_a = temp[0]
            replaced_arr.append(num_a)

        replaced_arr.append(-1)

        return replaced_arr