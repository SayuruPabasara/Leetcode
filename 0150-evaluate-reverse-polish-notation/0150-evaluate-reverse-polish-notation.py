#import module.it provides functions corresponding to standard aarithmatic operators.
import operator

#define class
class Solution(object):

    #method to evaluate a reverse polish expression.
    #inputs tokens array which holds operands & operators as string values.
    def evalRPN(self, tokens):

        #dictionary mapping operator symbols to their actual operators.
        ops={
            "+":operator.add,
            "-":operator.sub,
            "*":operator.mul,
            "/":operator.truediv
            }

        #stack which holds the integer operands during evaluation.    
        stack=[]

        #loop through each token
        for i in tokens:

            #check for operators and operands.
            #do if token is operator,
            if i in ops:
                b=stack.pop()
                a=stack.pop()
                stack.append(int(ops[i](a,b)))

            #do if token is operand  
            else:
                stack.append(int(i))

        return stack[0]                
        