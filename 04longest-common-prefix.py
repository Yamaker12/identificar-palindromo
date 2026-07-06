#Problem: https://leetcode.com/problems/longest-common-prefix/
#Difficulty: Eazy
#Time: 10 min
#Date: 06/07/2026
class Solution(object):
    def longestCommonPrefix(self, strs):
        import os
        prefixo = os.path.commonprefix(strs) # Ele retorna apenas um, que é o maior prefixo comum entre todas as strings da lista
        return prefixo
#Não gostei desse desafio porque se tiver mais de um prefixo o comando commonprefix não vai conseguir responder pois ele so 1 prefixo 
