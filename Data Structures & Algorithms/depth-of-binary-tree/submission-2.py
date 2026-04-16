# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        esquerda = self.maxDepth(root.left)
        direita = self.maxDepth (root.right)

        return 1 + max(esquerda, direita)
        

#Complexidades : 
    #A complexidade de tempo é O(n) pois visitamos todos os nós. A complexidade de espaço é O(h), 
 # onde h é a altura da árvore. No pior caso de uma árvore linear, isso degrada para O(n), 
  #mas em uma árvore balanceada, o espaço é otimizado para O(log n) devido ao comportamento da pilha de recursão.