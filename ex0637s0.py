#637. Average of Levels in Binary Tree


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = []
        res = []
        
        queue.append(root)
        while queue:
            sum  = 0
            count = 0
            temp = []
            while queue:
                node = queue.pop()
                sum += node.val
                count+=1
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)    
            res.append(sum/count)
            queue = temp
        return res