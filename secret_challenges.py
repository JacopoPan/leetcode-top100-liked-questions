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