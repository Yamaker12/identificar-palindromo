class Solution(object):
    def isPalindrome(self, x): 
       s = str(x) # Transformando x numa String para poder identificar as indices
       if set(s[0]) == set(s[-1]) : # Aqui fala se o primeiro indice de x e o ultimo for igual e também se o numero de algarimos for impar então é um palindromo (ex: 1212121)
        if len(s) % 2 == 1 :
           return True
       else: 
          return False
       

    
sol = Solution()
print(sol.isPalindrome(121))
