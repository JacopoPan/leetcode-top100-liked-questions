def solution(s):
    ans = -1
    div = 1
    while div <= len(s):
        if len(s)%div == 0:
            #print(s[:len(s)//div])
            if s[:len(s)//div]*div == s:
                ans = div
        div += 1
    return ans

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

def solution(src, dest):
    #Your code here
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

def solution(map):
    # Your code here
    queue = deque([(0,0,False,1)])
    visited = set()
    while queue:
        #print(queue)
        x, y, rem, dist = queue.popleft()
        #print(x,y,rem,dist)
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
