# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root):

        if not root : 
            return None

        root.left,root.right = root.right,root.left #Tuple Unpacking.

        self.invertTree(root.left)
        self.invertTree(root.right)

        return  root
    #Complexidades:
        #Tempo: O(n) : percorre todos os nós da árvore
        #Espaço: O(h) - altura
        #Pior caso espaço: O(n) - arvore desbalanceada (a plia armazena todos os nós)
        #Caso médio O(log n ) - arvore balenceada