#100. Same Tree

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        tree1 = []
        tree2 = []
        visited = []
        def dfs(visited,node,arr):
            if not node:
                return
            if node not in visited:
                arr.append(node.val)
                visited.append(node)
                if node.left:
                    dfs(visited,node.left,arr)
                if node.right and not node.left:
                    arr.append(None)
                    dfs(visited,node.right,arr)
                if node.right and node.left:
                    dfs(visited,node.right,arr)
                
                if not node.left and not node.right:
                    return 
                
        dfs(visited,p,tree1)
        visited = []
        dfs(visited,q,tree2)
        
        if tree1 == tree2:
            return True
        else:
            return False
                