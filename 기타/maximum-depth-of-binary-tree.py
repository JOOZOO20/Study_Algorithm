class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0

        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)
        if (l is 0) and (r is 0):
            return 1
        elif (l is not 0) and (r is not 0):
            return max(l,r)+1
        else:
            if l is not 0:
                return l+1
            else:
                return r+1