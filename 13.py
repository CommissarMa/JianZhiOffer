#%%
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        self.visited = [[0 for c in range(cols)] for r in range(rows)]
        self.threshold = threshold
        self.rows = rows
        self.cols = cols
        self.result = 0
        
        self.dfs(0, 0)
        return self.result
        
    def dfs(self, r, c):
        if r < 0 or c < 0 or r >= self.rows or c >= self.cols or self.visited[r][c] == 1: # 超出矩阵范围 或者 已经被访问过
            return
        
        self.visited[r][c] = 1
        if self.check(r, c) == True:
            print(r,c)
            self.result += 1
        self.dfs(r-1, c)
        self.dfs(r, c-1)
        self.dfs(r+1, c)
        self.dfs(r, c+1)
        
    def check(self, r, c):
        r_int = [int(ch) for ch in str(r)]
        c_int = [int(ch) for ch in str(c)]
        if sum(r_int) + sum(c_int) > self.threshold:
            return False
        else:
            return True

if __name__ == "__main__":
    s = Solution()
    r = s.movingCount(10, 1, 100)
    print(r)
