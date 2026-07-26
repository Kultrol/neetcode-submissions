class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet_table = {
            "" : 0,
            "a" : 1,
            "b" : 2,
            "c" : 3,
            "d" : 4,
            "e" : 5,
            "f" : 6,
            "g" : 7,
            "h" : 8,
            "i" : 9,
            "j" : 10,
            "k" : 11,
            "l" : 12,
            "m" : 13,
            "n" : 14,
            "o" : 15,
            "p" : 16,
            "q" : 17,
            "r" : 18,
            "s" : 19,
            "t" : 20,
            "u" : 21,
            "v" : 22,
            "w" : 23,
            "x" : 24,
            "y" : 25,
            "z" : 26
            } 

        word_table = {}
        for word in strs:
            alphabet_list = [0] * 27
            for char in word:
                char_num = alphabet_table[char]
                alphabet_list[char_num] += 1
            
            if word_table.get(tuple(alphabet_list), None) is None:
                word_table[tuple(alphabet_list)] = [word]
            else:
                word_table[tuple(alphabet_list)].append(word)
        
        word_list = []
        for value in word_table.values():
            word_list.append(value)
        
        return word_list