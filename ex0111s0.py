#111.Minimum depth of binary tree

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        queue = []
        count = 0
        queue.append(root)
        
        while queue:
            temp = []
            count +=1
            while queue:
                n = queue.pop()
                
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
                    
                elif not n.left and not n.right:
                    return count
            queue = temp
            