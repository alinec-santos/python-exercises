class Solution:
    def groupAnagrams(self, s):
        
        dicionario = {}

        for i in s:
            s_ordenado = "".join(sorted(i))

            if s_ordenado not in dicionario: 
                dicionario[s_ordenado] = []

            dicionario[s_ordenado].append(i)

        return list(dicionario.values())


#Complexidade de tempo: O(n k log k ) - percorremos a string com um loop e ordenamos as palavras
#Complexidade de espaço: O(k) -sendo k o numero de palavras