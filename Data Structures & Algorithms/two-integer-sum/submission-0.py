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

