def solution(s):
    # Your code here
    ans = -1
    div = 1
    while div <= len(s):
        if len(s)%div == 0:
            # print(s[:len(s)//div])
            if s[:len(s)//div]*div == s:
                ans = div
        div += 1
    return ans

###

def solution(l, t):
    # Your code here
    beg = 0
    end = 0
    test = l[0]
    while end <= len(l)-1 and beg <= end:
        # test = sum(l[beg:end+1])
        print(beg, end, '-', test)
        if test < t:
            end += 1
            if end == len(l):
                return [-1, -1]
            test += l[end]
        elif test > t:
            beg += 1
            test -= l[beg-1]
        else:
            return [beg, end]
    return [-1, -1]

###

def solution(src, dest):
    # Your code here
    def pos2Idx(p):
        return p//8, p%8
    def idx2Pos(i):
        return i[0]*8+i[1]
    src_x, src_y = pos2Idx(src)
    queue = deque([(src_x, src_y, 0)])
    visited = set()
    while queue:
        x, y, mv = queue.popleft()
        if x<0 or y<0 or x>=8 or y>=8:
            continue
        if (x,y) in visited:
            continue
        if idx2Pos((x,y)) == dest:
            return mv
        visited.add((x, y))
        queue.append((x+2, y+1, mv+1))
        queue.append((x+2, y-1, mv+1))
        queue.append((x-2, y+1, mv+1))
        queue.append((x-2, y-1, mv+1))
        #
        queue.append((x+1, y+2, mv+1))
        queue.append((x-1, y+2, mv+1))
        queue.append((x+1, y-2, mv+1))
        queue.append((x-1, y-2, mv+1))
    return -1

###

def solution(n):
    # Your code here
    n = int(n)
    queue = deque([(n, 0)])
    visited = set()
    while queue:
        val, op = queue.popleft()
        if val in visited:
            continue
        if val == 1:
            return op
        visited.add(val)
        queue.append((val+1, op+1))
        queue.append((val-1, op+1))
        if val%2 == 0:
            queue.append((val//2, op+1))
    return -1

###

def solution(x, y):
    # Your code here
    x = int(x)
    y = int(y)
    if x == 1 and y == 1:
        return str(0)
    queue = deque([(x, y, 0)])
    visited = set()
    while queue:
        m, f, gen = queue.popleft()
        if m == 1 and f == 1:
            return str(gen)
        if m == 1:
            return str(gen+f-1)
        if f == 1:
            return str(gen+m-1)
        if (m, f) in visited \
                or m < 1 or f < 1 \
                or m == f:
            continue
        visited.add((m,f))
        if f > m:
            queue.append((m, f%m, gen+f//m))
        if m > f:
            queue.append((m%f, f, gen+m//f))
    return "impossible"

###

def solution(map):
    # Your code here
    queue = deque([(0,0,False,1)])
    visited = set()
    while queue:
        # print(queue)
        x, y, rem, dist = queue.popleft()
        # print(x,y,rem,dist)
        if x == len(map)-1 and y == len(map[0])-1:
            return dist
        if x<0 or y<0 or x>=len(map) or y>=len(map[0]):
            continue
        if map[x][y] == 1 and rem == True:
            continue
        if (x,y,rem) in visited:
            continue
        visited.add((x,y,rem))
        if map[x][y] == 1:
            queue.append((x+1, y, True, dist+1))
            queue.append((x-1, y, True, dist+1))
            queue.append((x, y+1, True, dist+1))
            queue.append((x, y-1, True, dist+1))
        else:
            queue.append((x+1, y, rem, dist+1))
            queue.append((x-1, y, rem, dist+1))
            queue.append((x, y+1, rem, dist+1))
            queue.append((x, y-1, rem, dist+1))
    return -1

###

import itertools

def solution(num_buns, num_required):
    # Your code here
    ans = [ [] for _ in range(num_buns) ]
    num_uses = 1 + (num_buns - num_required)
    key = 0
    for team in itertools.combinations(list(range(num_buns)), num_uses):
        # print(team, key)
        for bunny in team:
            ans[bunny].append(key)
        key += 1
    return ans

###

def EdmondsKarp(E, C, s, t):
    n = len(C)
    flow = 0
    F = [[0 for y in range(n)] for x in range(n)]
    while True:
        P = [-1 for x in range(n)]
        P[s] = -2
        M = [0 for x in range(n)]
        M[s] = 2000001
        BFSq = []
        BFSq.append(s)
        pathFlow, P = BFSEK(E, C, s, t, F, P, M, BFSq)
        if pathFlow == 0:
            break
        flow = flow + pathFlow
        v = t
        while v != s:
            u = P[v]
            F[u][v] = F[u][v] + pathFlow
            F[v][u] = F[v][u] - pathFlow
            v = u
    return flow

def BFSEK(E, C, s, t, F, P, M, BFSq):
    while (len(BFSq) > 0):
        u = BFSq.pop(0)
        for v in E[u]:
            if C[u][v] - F[u][v] > 0 and P[v] == -1:
                P[v] = u
                M[v] = min(M[u], C[u][v] - F[u][v])
                if v != t:
                    BFSq.append(v)
                else:
                    return M[t], P
    return 0, P

def solution(entrances, exits, path):
    # Your code here
    src = -1
    sink = len(path)
    graph = {src: [(entry, 2000001) for entry in entrances]}
    for n, links in enumerate(path):
        graph[n] = []
        for neigh, cap in enumerate(links):
            if cap != 0:
                graph[n].append((neigh, cap))
        if n in exits:
            graph[n].append((sink, 2000001))
    graph[sink] = []
    # print(graph)
    capacity_matrix = [ [0]*(len(path)+2) for _ in range(len(path)+2) ]
    for k, v in graph.items():
        for n in v:
            capacity_matrix[k+1][n[0]+1] = n[1]
    # print(capacity_matrix)
    next_graph = []
    for n in range(-2,len(path)):
        temp = []
        for nxt in graph[n+1]:
            temp.append(nxt[0]+1)
        next_graph.append(temp)
    # print(next_graph)
    max_flow = EdmondsKarp(next_graph, capacity_matrix, 0, len(next_graph)-1)
    return max_flow

###

import math
import decimal
from decimal import Decimal
context = decimal.getcontext()
context.prec = 1010

def help(n):
    # print(n)
    if n == Decimal(0):
        return Decimal(0)
    if n == Decimal(1):
        return Decimal(1)
    n_i = Decimal((Decimal(2).sqrt()-1)*n).quantize(Decimal('1.'), rounding='ROUND_FLOOR')
    val = n*n_i + n*(n+1)/2 - n_i*(n_i+1)/2 - help(n_i)
    # print(val)
    return Decimal(val)

def solution(s):
    # Your code here
    ans = help(Decimal(s))
    return '{0}'.format(ans)

###

b"{'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}"