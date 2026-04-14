class Solution:
    def characterReplacement(self, s,k):

        dicionario = {}
        esquerdo,resultado,maior = 0,0,0


        for direito in range(len(s)):

            dicionario[s[direito]] = dicionario.get(s[direito],0)+1

            maior = max(maior,dicionario[s[direito]])
            janela = direito - esquerdo + 1

            while janela - maior> k:
                dicionario[s[esquerdo]] -= 1
                esquerdo += 1 

                janela = direito - esquerdo + 1

            resultado = max(resultado,direito-esquerdo + 1)

        return resultado


        #complexidade de tempo:O (n)
        # complexidade de espaço: O (k) -> maximo de caracteres que vai armazenar 