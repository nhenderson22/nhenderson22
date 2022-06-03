
class Solution:
    def sol(self,n):
        
        ans = []
        for num in range(1,n+1):
            divBy3 = (num % 3 == 0)
            divBy5 = (num % 5 == 0)
            if divBy3 and divBy5:
                ans.append("FizzBuzz")
            elif divBy3:
                ans.append("Fizz")
            elif divBy5:
                ans.append("Buzz")
            else:
                ans.append(str(num))
        return ans


fb = Solution()
print(fb.sol(60))
