import collections as cui
G = cui.defaultdict(list)
s = cui.defaultdict(list)
G[0].append(1)
G[1].extend([2,4,5])
G[2].extend([3,6])
G[3].extend([7,2])
G[4].extend([5,0])
G[5].append(6)
G[6].extend([7,5])
G[7].append(7)
for i in range(len(G)):
    s[i].extend([0,-1,-1,-1,0,-1,-1])
    
def bfs(G,s,r):
    s[r][4] = 1
    s[r][5] = 0
    queue = cui.deque([r])
    while queue:
        u = queue.popleft()
        for v in G[u]:
            if s[v][4] == 0:
                s[v][4] = 1
                s[v][5] = s[u][5] + 1
                s[v][6] = u
                queue.append(v)
        s[u][4] = 2
def dfsV(G, s, u):
    global time
    time += 1
    s[u][1] = time
    s[u][0] = 1
    for v in G[u]:
        if s[v][0] == 0:
            s[v][3] = u
            dfsV(G,s,v)
    time += 1
    s[u][2] = time
    s[u][0] = 2
def dfs(G,s):
    for u in G:
        if s[u][0] == 0:
            dfsV(G,s,u)
time = 0
bfs(G,s,0)
dfs(G,s)
temp = sorted(s, key = lambda x:-s[x][2])
#print(temp)
GT = cui.defaultdict(list)
st = cui.defaultdict(list)
for u in G:
    for v in G[u]:
        GT[v].append(u)
for i in range(len(GT)):
    st[i].extend([0,-1,-1,-1,0,-1,-1])
def scc(GT, st, temp):
    res = []
    for u in temp:
        if st[u][0] == 0:
            dfsV(GT, st, u)
            res.append(set([x for  x in st if st[x][0] == 2]))

    return res
res1 = scc(GT, st, temp)
#print(res1)
for i in range(len(res1) -1, 0, -1):
    res1[i] = res1[i].difference(res1[i-1])
print(res1)




    