class Solution(object):
    def calPoints(self, operations):
        stack=[]
        for i in range(len(operations)):
            if operations[i]!='C' and operations[i]!='D' and operations[i]!='+':
                stack.append(int(operations[i]))
            elif operations[i]=='+':
                stack.append(int(stack[-1] + stack[-2]))
            elif operations[i]=='D':
                stack.append(int(2*stack[-1]))
            elif operations[i]=='C':
                stack.pop(-1)    
        return sum(stack)        


        
        