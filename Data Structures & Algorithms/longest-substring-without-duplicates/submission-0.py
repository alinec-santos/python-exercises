class Solution:
    def lengthOfLongestSubstring(self, s): 
        esquerdo = 0 
        max_comprimento = 0
        char_set = set()

        for direito in range(len(s)):
            while s[direito] in char_set:

                char_set.remove(s[esquerdo])
                esquerdo += 1 

            char_set.add(s[direito])

            janela_atual = direito - esquerdo + 1 

            max_comprimento = max(max_comprimento,janela_atual)

        return max_comprimento
        