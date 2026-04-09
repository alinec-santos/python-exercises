class Solution:
    def twoSum(self, nums, target):

        #Para uma solução otimizada vamos utilizar o HashMap.  A ideia é utilizar um par (Chave:Valor) onde a nossa chave seria o númeroda vez e o valor seria o seu indice. E como ideia principal , podemos fazer uma subtraç~ca: target -num[i] e verificar se esse resultado da sub esta no meu dicionario. Se estiver, eu retorno o valor da chave do meu pare e o meu i.      

        seed = {}
        
        for i, num in enumerate(nums):

            sub = target - num

            if sub in seed:
                return [seed[sub],i]
            else:
                seed[num] = i

    #teremos uma complexidade de tempo de O(n) para esse algoritmo pois percorremos a lista apenas uma vez. E Teremos a complexidade de espaço como O(n) também. Pois no pior caso vamos armazenar os n elementos dentro do dicionário. 