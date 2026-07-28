class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        n = len(self.stack)
        return self.stack[n-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        low_s = "".join(char.lower() for char in s if char.isalnum())
        if len(low_s) % 2 == 0:
            valid_palindrome_stack = Stack()
            for i in range(0, int(len(low_s)/2)):
                valid_palindrome_stack.push(low_s[i])
            
            for i in range(int(len(low_s)/2), len(low_s)):
                if valid_palindrome_stack.pop() != low_s[i]:
                    return False
            
            return True
        else:
            valid_palindrome_stack = Stack()
            for i in range(0, int((len(low_s) - 1)/2)):
                valid_palindrome_stack.push(low_s[i])
            
            for i in range(int((len(low_s)+1)/2), len(low_s)):
                if valid_palindrome_stack.pop() != low_s[i]:
                    return False
            
            return True