class Solution(object):
    def maskPII(self, s):
        # EMAIL
        if s[0].isalpha():
            s = s.lower()
            name, domain = s.split("@")
            return name[0] + "*****" + name[-1] + "@" + domain
        
        # PHONE
        digits = "".join(ch for ch in s if ch.isdigit())
        local = "***-***-" + digits[-4:]
        
        if len(digits) == 10:
            return local
        else:
            country = "+" + "*" * (len(digits) - 10)
            return country + "-" + local
                
                


        