class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        # res = []
        # for num in range(1,n+1):
            
        #     if num%3==0 and num%5==0:
        #         #res += ["FizzBuzz"]
        #         res.append("FizzBuzz")
        #     elif num%3 == 0:
        #         # res +=["Fizz"]
        #         res.append("Fizz")
        #     elif num%5 == 0:
        #         #res +=["Buzz"]
        #         res.append("Buzz")
        #     else:
        #         #res +=[str(num)]
        #         res.append(str(num))

        #     # elif i%3 == 0:
        #     #     res.append(["Fizz"])
        #     # elif i%5 == 0:
        #     #     res.append(["Buzz"])
         
        # return res
        
        res = []
        for num in range(1,n+1):
            res1 = ""
            if num%3==0 and num%5==0:
                res1 += "FizzBuzz"
            elif num%3 == 0:
                res1 += "Fizz"
            elif num%5 == 0:
                res1 +="Buzz"
            else:
                res1 = str(num)
            res.append(res1)
        return res


