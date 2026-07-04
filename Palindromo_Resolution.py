#Date: 02/07/2026
#Difficulty: Eazy
#Problem link: https://leetcode.com/problems/palindrome-number/description/
#Duration: 2 hours💀💀

class Solution(object):
    def isPalindrome(self, x):
        number = str(x) # Transformando o número int em uma string pra poder conseguir usar os colchetes
        if number == number[::-1]: # Se o número for igual ao número de traz para frente então é um palíndromo
            return True
        else: # Se a string não for uma palíndromo então é falso
            return False

sol = Solution()
print(sol.isPalindrome(1221))
# Essa foi a resposta
# A resolução era muito mais simples que parecia😭😭
