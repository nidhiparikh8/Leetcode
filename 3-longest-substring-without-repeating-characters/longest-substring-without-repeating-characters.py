class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # s = "abcabcbb"
        # chars = set()
        # res = 0
        # l = 0
        # for r in range(len(s)):
        #     while s[r] in chars:
        #         chars.remove(s[l])
        #         l += 1
        #     chars.add(s[r])
        #     res = max(res,r-l+1)   
            
        # return res

        

    #bruteforce

        # def check(i,j):
        #     chars = set()
        #     for i in range(i,j+1):
        #         c = s[i]
        #         if c in chars:
        #             return False
        #         chars.add(c)
        #     return True

        # res = 0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         if check(i,j):
        #             res = max(res,j-i+1)
        # return res  


        #two pointers with hmap approach
        hmap ={} 
        maxlength = 0
        i = 0
        for j in range(len(s)):

            if s[j] in hmap and hmap[s[j]] >= i:

                i = hmap[s[j]] + 1
                
        
            hmap[s[j]] = j
            maxlength = max(maxlength,j-i+1)
        return maxlength

            
            
