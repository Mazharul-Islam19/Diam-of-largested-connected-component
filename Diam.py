file = 'PGPgiantcompo.graph'
adj_list = {}
data = []
with open(file) as f:
    for line in f:
        line = line.strip("\n")
        data.append(line)
    num_of_vertices = int(data[0].split()[0])
    num_of_edges = int(data[0].split()[1])
    if data[0].split()[2] == '0':
        Weighted = False
    data.pop(0)
    data = data[:num_of_vertices]
    for i in range(1,len(data)+1):
        adj_list[i] = data[i-1].split()

Visited = {}
for i in adj_list:
    Visited[i] = False

Comp = {}

def DFS(v):
    Visited[int(v)] = True
    Comp[i].append(v)
    for w in adj_list[int(v)]:
        if Visited[int(w)] == False:
            DFS(w)
    return Comp

i = 0
for v in adj_list:
    if Visited[int(v)] == False:
        i += 1
        Comp[i] = []
        DFS(v)

def BFS(G,s):
    Q = [s]
    dist = {}
    for i in G:
        dist[int(i)] = float('inf')
    dist[int(s)] = 0
    max_sp = 0
    while len(Q) != 0:
        v = Q[0]
        for w in adj_list[int(v)]:
            if dist[int(w)] == float('inf'):
                dist[int(w)] = dist[int(v)] + 1
                Q.append(w)
                if dist[int(w)] > max_sp:
                    max_sp = dist[int(w)]
        Q.pop(0)
    return max_sp

Max_Comp = (0,0)
for i,j in Comp.items():
    if len(j) > Max_Comp[1]:
        Max_Comp = (i,len(j))
   
Diam = 0
Max_CompSP = {}  
for k in Comp[Max_Comp[0]]:
    Max_CompSP[k] = BFS(Comp[Max_Comp[0]],k)
    if Max_CompSP[k] > Diam:
        Diam = Max_CompSP[k]

Output = {'Vertices':Max_Comp[1], 'Diameter':Diam}
print('Number of vertices in the largest component : {}\nDiameter of that component : {}'.format(Output['Vertices'],Output['Diameter']))

