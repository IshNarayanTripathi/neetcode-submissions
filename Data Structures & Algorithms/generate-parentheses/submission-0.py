class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        def backtrack(no,nc,curr):
            if no == nc == n:
                stack.append(''.join(curr.copy()))
                return
            if no < n:
                curr.append('(')
                backtrack(no+1,nc,curr)
                curr.pop()
            if  nc < no:
                curr.append(')')
                backtrack(no,nc+1,curr)
                curr.pop()
        backtrack(0,0,[])
        return stack
                