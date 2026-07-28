class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
                continue
            else:
                if len(stack) != 0:
                    popped_char = stack.pop()
                    if char == ")":
                        if popped_char == "(":
                            continue
                        else:
                            return False
                        
                    if char == "}":
                        if popped_char == "{":
                            continue
                        else:
                            return False

                    if char == "]":
                        if popped_char == "[":
                            continue
                        else:
                            return False
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False