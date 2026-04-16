class Solution:
    def threeSum(self, nums):

        res = []
        nums.sort()

        for i in range(len(nums)-2):

            if i>0 and nums[i] == nums[i-1]:
                continue
            
            esquerdo,direito = i+1, len(nums) - 1 

            while esquerdo<direito:

                soma= nums[i] + nums[esquerdo] + nums[direito]

                if soma == 0:
                    res.append([nums[i],nums[esquerdo],nums[direito]])

                    while esquerdo <direito and nums[esquerdo] == nums[esquerdo+1]:
                        esquerdo += 1
                    while esquerdo<direito and nums[direito] == nums[direito - 1 ]:
                        direito -= 1 
                    esquerdo += 1 
                    direito -= 1 

                elif soma < 0: 
                    esquerdo += 1 

                else: 
                    direito -= 1 
        return res 

# Complexidade de Tempo: O (n ao quadrado) - gasto O (n) para percorrer o array e O(n) para o par de ponteiros que tbm percorre o array
# Complexidade de Espaço Auxiliar : O(1)
#Complexidade de espaço total incluindo a saida: O(m) onde m é o numero de triplas encontradas. 