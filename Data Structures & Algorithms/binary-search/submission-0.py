class Solution:
    def search(self, nums,target):

        #para força bruta nós usariamos um loop para comparar o valor do num[i] com o target. Isso nos daria
        # uma complexidade de tempo de O(n). E uma complexidade de espaço de O(1). Se o array estivesse ordenado usar a busca linear seria a soluçao otima para o problema 
    

        #podemos melhorar essa complexidade usando a busca binaria. A ideia vai ser dividir a lista ao meio e ver se o elemento do meio bate com o nosso target
        # se o valor bater, ja achamos o indice. Se o meio>target , decrementamos 1, se meio<target incrementamos 1. 


        baixo = 0
        cima = len(nums) - 1

        while baixo<=cima: 

            meio = (baixo+cima) // 2 #em outras linguagens como c++ e java essa operação traria problemas com overflow, mais em python esse problema ja é tratdo na propria operação 
            chute = nums[meio]

            if chute == target: 
                return meio

            if chute> target: 
                cima = meio -1

            if chute<target:
                baixo = meio + 1 
        return - 1
            

