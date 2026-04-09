class Solution:
    def isAnagram(self, s,t):

        #Pensando primeiro no algoritmo que usariamos como força bruta para depois pensarmos em como podemos otimizar. 
        #Sabendo que um anagrama deve conter a mesma frequencia de letras e o mesmo comprimento. Poderiamos começar
        #conferindo se as palavras sao do mesmo tamanho. Se nao forem ja encerramos o programa. Em seguida, poderiamos ordenar ambas as palavras e fazer
        #a comparação delas, se ambas ordenadas forem iguais elas sao um anagrama. Nossa complexidade de tempo seria O(n log n ) pois iriamos percorrer a string pelo menos duas vezes para ordenar e 1 vez para fazer a comparação. 
        #E de espaço seria O(n) tambem pois o sorted cria uma copia da string na memoria (o tamanho dessa nova copia é proporcional ao tamanho n da lista). Para uma string muito grande isso seria um problema
        
        #Podemos otimizar nosso codigo usando hashMap.A ideia é usar a mesma contextualização de uma balança
        # Quando eu acho uma letra na minha palavra s eu armazeno ela no meu dicionario como um par (chave:valor) onde chave seria a minha letra e valor a frequencia que ela aparece
        # na minha palavra s eu somo 1 a frequencia, na palavra t eu subtraio 1 na frequencia. Assim , se todos os valores do meu dicionario terminarem zerados , eu tenho um anagrama perfeito. 


        if len(s) != len(t):
            return False

        seed = {}
        for i in range(len(s)):

            seed[s[i]] = seed.get(s[i], 0) + 1
            seed[t[i]] = seed.get(t[i], 0) - 1 

        for val in seed.values():
            if val!= 0:
                return False
        return True
        

        #Com isso, nossa complexidade de tempo passa a ser O(2n), 2n pq somamos os dois loops pois eles nao estao aninhados
        # e o 2 some pois é constante . Entao nossa complexidade de tempo fica O(n) e a de espaço fica O(n) pois no pior caso eu armazeno todos os n elementos no meu dicionario