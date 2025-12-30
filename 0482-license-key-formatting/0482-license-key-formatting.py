class Solution:
    def licenseKeyFormatting(self,s,k):
        
        s=s.replace("-","").upper()
        first=len(s)%k
        result=s[0:first] if first!=0 else ""
        s_rest=s[first:]
        for i in range(0,len(s_rest),k):
            if result:
                result+="-"
            result+=s_rest[i:i+k]     
        return result
            
        
        



        