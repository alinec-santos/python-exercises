class Solution:
    def hasDuplicate(self, nums):
        # para esse problema podemos usar o set para verificar se os números estao repetidos.
        vistos = set()
        for i in nums:

            if i in vistos:
                return True


            else:
                vistos.add (i)

        return False

# Com esse código, temos um complexidade:
#- Tempo: O (n) - pois percorremos a lista uma vez
#- Espaço: O (n) - pois usamos o set como memória extra e no pior dos casos ele vai armazenar os n números
# Se estivessemos usando força bruta , o codigo teria uma complexidade de tempo de O(n^2) pois iriamos comparar indice por indice. E a de espaço seria O(1) pois nao usariamos nenhuma memoria extra. 
#Aqui fizemos uma troca aceitavel de tempo em memoria que nao vai afetar tanto o nosso algoritmo. Se quisessimos manter a memoria como constante e melhorando um pouco a complexidade em relaçao a força bruta, nos ordenariamos a lista e olhariamos o proximo elemento para ver se repetem. Isso nos daria uma complexidade de tempo de O(n*log n) e de espaço O(1)