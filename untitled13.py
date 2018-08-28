def dfs(nums, visited,  path, res):
    if len(path) == len(nums):
        res.append(''.join(path))
    for i in range(len(nums)):
        if i not in visited:
            visited.add(i)
            path.append(nums[i])
            dfs(nums,  visited, path, res)
            path.pop()
            visited.discard(i)
n = 3
nums = ['a'] * n + ['z'] * n 
visited = set()
res = []
dfs(nums, visited, [], res)
ans = list(set(res))
ans.sort()