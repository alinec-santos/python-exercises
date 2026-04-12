class Solution:
    def isPalindrome(self, s):
        esquerdo,direito = 0, len(s)-1
        while esquerdo<direito:
            while esquerdo <direito and not s[esquerdo].isalnum():
                    esquerdo += 1
            while esquerdo <direito and not s[direito].isalnum():
                    direito -= 1 
            if s[esquerdo].lower() != s[direito].lower():
                return False
            esquerdo += 1 
            direito -= 1
        return True


#COMPLEXIDADE DE TEMPO: O(N)
#COMPLEXIDADE DE ESPAÇO: O(N)

#ESTRUTURA DE DADOS: STRING
#ALGORITMO : TWO POINTERS