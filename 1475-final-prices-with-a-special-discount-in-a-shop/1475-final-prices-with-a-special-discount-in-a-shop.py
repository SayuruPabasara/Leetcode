class Solution(object):
    def finalPrices(self, prices):
        answer=list(prices)
        stack=[]
        for i in range(len(prices)):
            while stack and answer[stack[-1]]>=prices[i]:
                index=stack.pop()
                answer[index]-=prices[i]
            stack.append(i)  
        return answer  
            

        