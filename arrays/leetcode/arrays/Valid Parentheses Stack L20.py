class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] # creating a python list
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" } # creating hashmap with each pair, "answer" : "question"
        

        for c in s: # c is each value in string s
            if c in closeToOpen: # checks through keys in hashmap to see if c is matching
                if stack and stack[-1] == closeToOpen[c]: # checks if stack is not empty and if the last value in stack matches the corresponding opening bracket (c)
                    stack.pop() # removes last value in stack if it matches
                else:
                    return False # otherwise false
            else:
                stack.append(c) # if c is not in the hashmap keys, it is an opening bracket, so we add it to the stack
        return True if not stack else False # if stack is empty, all brackets were properly closed, so return true, otherwise false
