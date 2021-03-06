# leetcode-top100-liked-questions
Python3 Solutions to [LeetCode's "Top 100 Liked Questions"](https://leetcode.com/problem-list/79h8rn6/)

The type of code that might be useful in a coding interview. Or if John Travolta with a goatee needs you to hack the DoD in less than 60 seconds at a nightclub, that kind of stuff.

Uploaded as I answer them. Run as:
```bash
$ git clone git@github.com:JacopoPan/leetcode-top100-liked-questions.git
$ cd leetcode-top100-liked-questions
$ python3 solutions/123.\ Problem\ Name.py
```

# Essentials

## Template

```python
# import pdb; pdb.set_trace() # [s]tep into function; [l]ist 11 lines; [w]here in stack; # [p]rint (exp/var);
                            # [b]reak at line no; [c]ontinue to break; [q]uit; [h]elp
from functools import lru_cache # cache since Python 3.9
from typing import List, Optional

class Problem:
    def __init__(self):
        pass

    @lru_cache
    def methodZero(self, n: int=0) -> str:
        return ''

    def methodOne(self, argName: List[int]) -> Optional[int]:
        return -1

def main():
    sol = Problem()
    ans = sol.methodOne([0,0,0])
    assert ans == -1
    print(ans)

if __name__ == "__main__":
    print('Template')
    main()
``` 

## List and Tree Node Classes

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
``` 

## Traverse a Linked List

```python
list_root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

def traverse_list(list_root):
    while list_root:
        print(list_root.val)
        list_root = list_root.next

if __name__ == "__main__":
    print('Traverse List')
    traverse_list(list_root)
``` 

## Traverse a Linked List with a Runner

```python
list_root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

def traverse_list_runner(list_root):
    if list_root:
        runner = list_root.next
    while list_root:
        print(list_root.val)
        if runner:
            print(runner.val)
        if runner:
            list_root = runner.next
            runner = list_root.next
        else:
            list_root = None

if __name__ == "__main__":
    print('Traverse List with Runner')
    traverse_list_runner(list_root)
``` 

## Reverse a Linked List

```python
list_root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

def reverse_list(list_root):
    prev = None
    nxt = list_root
    while nxt:
        temp = nxt
        nxt = nxt.next
        temp.next = prev
        prev = temp
    return prev

if __name__ == "__main__":
    print('Reverse List')    
    reverse = reverse_list(list_root)
    while reverse:
        print(reverse.val)
        reverse = reverse.next
```

## Tree Depth-First

```python
tree_root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5, TreeNode(8), TreeNode(9))), None), TreeNode(6, None, TreeNode(7)))

def tree_dfs(root):
    if root: # preorder: this, l, r / inorder l, this, r / postorder l, r, this
        print(root.val)
        tree_dfs(root.left)
        tree_dfs(root.right)

if __name__ == "__main__":
    print('Tree DFS')
    tree_dfs(tree_root)
``` 

## Tree Breadth-First

```python
from collections import deque

tree_root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5, TreeNode(8), TreeNode(9))), None), TreeNode(6, None, TreeNode(7)))

def tree_bfs(root):
    if root:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                print(node.val)
                queue.append(node.left)
                queue.append(node.right)

if __name__ == "__main__":
    print('Tree BFS')
    tree_bfs(tree_root)
``` 

## Graph Depth-First

```python
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()

def graph_dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            graph_dfs(graph, neighbour, visited)

if __name__ == "__main__":
    print('Graph DFS')
    graph_dfs(graph, 'A', visited)
``` 

## Graph Breadth-First

```python
from collections import deque

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()
queue = deque([])

def graph_bfs(graph, node, visited):
    visited.add(node)
    queue.append(node)
    while queue:
        node = queue.popleft() 
        print(node) 
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == "__main__":
    print('Graph BFS')
    graph_bfs(graph, 'A', visited)
``` 

## Graph Topological Sort

```python
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'], # ['F', 'A'] # cycle
    'F' : []
}

def topological_sort(graph):
    indegrees = {node : 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegrees[neighbor] += 1
    nodes_with_no_incoming_edges = []
    for node in graph:
        if indegrees[node] == 0:
            nodes_with_no_incoming_edges.append(node)
    topological_ordering = [] 
    while nodes_with_no_incoming_edges:
        node = nodes_with_no_incoming_edges.pop()
        topological_ordering.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                nodes_with_no_incoming_edges.append(neighbor)
    if len(topological_ordering) == len(graph):
        print(topological_ordering)
    else:
        print("Graph has a cycle: no topological ordering exists.")

if __name__ == "__main__":
    print('Topological Sort')
    topological_sort(graph)
```

## Matrix Depth-First

```python
grid = [[0,1,1],[0,0,1],[0,0,2]]

visited = set()
ans = 9999.

def matrix_dfs(grid, i, j, visited, steps):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
        return
    if (i,j) in visited or grid[i][j] == 1:
        return
    if grid[i][j] == 2:
        global ans
        ans = min(ans, steps)
    visited.add((i, j))
    matrix_dfs(grid, i+1, j, visited, steps+1)
    matrix_dfs(grid, i-1, j, visited, steps+1)
    matrix_dfs(grid, i, j+1, visited, steps+1)
    matrix_dfs(grid, i, j-1, visited, steps+1)

if __name__ == "__main__":
    print('Matrix DFS')
    matrix_dfs(grid, 0, 0, visited, -1)
    print('Shortest path: ', ans)
``` 

## Matrix Breadth-First

```python
from collections import deque

grid = [[0,1,1],[0,1,1],[0,0,2]]

visited = set()
queue = deque([])

def matrix_bfs(grid, visited):
    while queue:
        x, y, dist = queue.popleft()
        if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
            continue
        if (x,y) in visited or grid[x][y] == 1:
            continue
        if grid[x][y] == 2:
            return dist
        visited.add((x, y))
        queue.append((x+1, y, dist+1))
        queue.append((x-1, y, dist+1))
        queue.append((x, y+1, dist+1))
        queue.append((x, y-1, dist+1))
    return None

if __name__ == "__main__":
    print('Matrix BFS')
    queue.append((0,0,0))
    print('Shortest path: ', matrix_bfs(grid, visited))
```

## Merge Sort

```python
unsorted_list = [3, 7, 1, 3, 6, 3, 1, 9]

def merge_sorted(list_one, list_two):
    list_one_index = 0
    list_two_index = 0
    merged_list = []
    while list_one_index < len(list_one) and list_two_index < len(list_two):
        if list_one[list_one_index] <= list_two[list_two_index]:
            merged_list.append(list_one[list_one_index])
            list_one_index += 1
        else:
            merged_list.append(list_two[list_two_index])
            list_two_index += 1
    while list_one_index < len(list_one):
        merged_list.append(list_one[list_one_index])
        list_one_index += 1
    while list_two_index < len(list_two):
        merged_list.append(list_two[list_two_index])
        list_two_index += 1
    return merged_list

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    left  = unsorted_list[:len(unsorted_list) // 2]
    right = unsorted_list[len(unsorted_list) // 2:]
    left_sorted  = merge_sort(left)
    right_sorted = merge_sort(right)
    ans = merge_sorted(left_sorted, right_sorted)
    return ans

if __name__ == "__main__":
    print('Merge Sort')
    ans = merge_sort(unsorted_list)
    print(ans)
``` 

## Quick Sort

```python
unsorted_list = [3, 7, 1, 3, 6, 3, 1, 9]

def partition(unsorted_list, start_index, end_index):
    pivot = unsorted_list[end_index]
    left_index  = start_index
    right_index = end_index - 1
    while left_index <= right_index:
        while left_index <= end_index and unsorted_list[left_index] < pivot:
            left_index += 1
        while right_index >= start_index and unsorted_list[right_index] >= pivot:
            right_index -= 1
        if left_index < right_index:
            temp = unsorted_list[right_index]
            unsorted_list[right_index] = unsorted_list[left_index]
            unsorted_list[left_index] = temp
        else:
            temp = unsorted_list[end_index]
            unsorted_list[end_index] = unsorted_list[left_index]
            unsorted_list[left_index] = temp
    return left_index

def quick_sort(unsorted_list, start_index=0, end_index=None):
    if end_index == None:
        end_index = len(unsorted_list)-1
    if (start_index >= end_index):
        return
    pivot_index = partition(unsorted_list, start_index, end_index)
    quick_sort(unsorted_list, start_index, pivot_index - 1)
    quick_sort(unsorted_list, pivot_index + 1, end_index)

if __name__ == "__main__":
    print('Quick Sort')
    quick_sort(unsorted_list)
    print(unsorted_list)
``` 

## Heapq

```python
from heapq import heappush, heappop, heapify

unsorted_list = [3, 7, 1, 3, 6, 3, 1, 9]

def heap():
    heapify(unsorted_list)
    print(unsorted_list)
    heappush(unsorted_list, 2)
    print(unsorted_list)
    val = heappop(unsorted_list)
    print(val, unsorted_list)
    # other methods: heapq.heappushpop(heap, item); heapq.heapreplace(heap, item);
    # heapq.merge(); heapq.nlargest(n); heapq.nsmallest(n)

if __name__ == "__main__":
    print('Heap')
    heap()
```

## Minimum Spanning Tree

```python
from heapq import heappush, heappop, heapify

points = [[2,-3],[-17,-8],[13,8],[-17,-15]]

def msp(points):
    manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    edges = []
    n = len(points)
    for i in range(n):
        for j in range(i+1,n):
            edges.append((manhattan(points[i],points[j]),i,j))
    heapify(edges)
    visited = set()
    ans = 0
    while edges and len(visited) < n:
        added = False
        temp = []
        while not added:
            e = heappop(edges)
            added = True
            if not visited:
                ans += e[0]
                visited.add(e[1])
                visited.add(e[2])
            elif e[1] not in visited and e[2] in visited:
                ans += e[0]
                visited.add(e[1])
            elif e[2] not in visited and e[1] in visited:
                ans += e[0]
                visited.add(e[2])
            else:
                temp.append(e)
                added = False 
        for e in temp:
            heappush(edges, e)
    return ans

if __name__ == "__main__":
    print('Minumum Spanning Tree')
    print('Cost: ', msp(points))
```

## Dijkstra

```python
from heapq import heapify, heappop, heappush
from collections import defaultdict

costs = [[2,1,1],[2,3,1],[3,4,1]]

def dijkstra(costs, num_nodes, source):
    graph = defaultdict(list)
    for (node, neigh, cost) in costs:
        graph[node].append((neigh, cost))
    priority_queue = [(0, source)]
    heapify(priority_queue)
    shortest_path = {}
    while priority_queue:
        cost, node = heappop(priority_queue)
        if node not in shortest_path:
            shortest_path[node] = cost
            for neigh, neigh_cost in graph[node]:
                heappush(priority_queue, (cost + neigh_cost, neigh))
    if len(shortest_path) == num_nodes:
        return max(shortest_path.values())
    else:
        return -1

if __name__ == "__main__":
    print('Dijkstra')
    print('Delay: ', dijkstra(costs, 4, 2))
```

## (Dict) Trie

```python
word_list = ['app', 'apple', 'oath', 'pea', 'peanut']

def trie(words):
    trie={}
    for word in words:
        temp=trie
        for character in word:
            if character not in temp:
                temp[character]={}
            temp=temp[character]
        temp['#']='%'
    return trie

if __name__ == "__main__":
    print('Trie')
    trie = trie(word_list)
    print(trie)
```

## Binary Search

```python
sorted_arr = [2, 3, 4, 10, 40]
target = 10

def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    while low < high:
        mid = (high + low)//2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] >= x:
            high = mid 
    return low

if __name__ == "__main__":
    print('Binary Search')
    print('Index: ', binary_search(sorted_arr, target))
```

## Two Pointers

```python
barriers = [1, 8, 9, 4, 11, 15, 3, 5]

def two_pointers(barriers):
    i = 0
    j = len(barriers)-1
    max_water = (j-i)*min(barriers[i],barriers[j])
    while i < j:
        if barriers[i] < barriers[j]:
            i += 1
        else:
            j -= 1
        max_water = max(max_water, (j-i)*min(barriers[i],barriers[j]))
    return max_water

if __name__ == "__main__":
    print('Two Pointers')
    print('Max water: ', two_pointers(barriers))
```

## Dynamic Programming

```python
cache = {}

def fibonacci(n):
    if n <= 1:
        return n
    else:
        if n in cache.keys():
            return cache[n]
        else:
            ans = fibonacci(n-1) + fibonacci(n-2)
            cache[n] = ans
            return ans

if __name__ == "__main__":
    print('Dynamic Programming: Top Down Fibonacci with Memoization')
    ans = fibonacci(60)
    print(ans)
```

## Pemutations and Combinations

```python
def perms(candidates):
    if len(candidates) <=1:
        return [candidates]
    else:
        ans = []
        prev = perms(candidates[1:])
        for p in prev:
            for i in range(len(candidates)):
                ans.append(p[:i] + candidates[0:1] + p[i:])
        return ans

def combs(candidates):
    if not candidates:
        return [[]]
    else:
        ans = []
        for c in combs(candidates[1:]):
            ans.append(c)
            ans.append(c+[candidates[0]])
        return ans

if __name__ == "__main__":
    print('Permutations and Combinations')
    ans = perms([0,1,2])
    print(ans)
    ans = combs([0,1,2])
    print(ans)
```

## Lists

```python
from collections import deque

def lists():
    working_list = []
    print(working_list)
    working_list.append(1)
    print(working_list)
    working_list.extend([2, 4])
    print(working_list)
    working_list.insert(2, 3)
    print(working_list)
    working_list.remove(3)
    print(working_list)
    working_list.pop()
    print(working_list)
    working_list.pop(0)
    print(working_list)
    del working_list[0]
    print(working_list)
    working_list = [1, 2, 3, 4]
    idx = working_list.index(3)
    print(idx, working_list)
    count = working_list.count(3)
    print(count, working_list)
    working_list.sort(reverse=True)
    print(working_list)
    working_list.reverse()
    print(working_list)
    queue = deque([1, 2, 3, 4])
    print(queue)
    queue.popleft()
    print(queue)

if __name__ == "__main__":
    print('Lists')
    lists()
```

## Slicing Lists

```python
a = [1, 2, 3, 4, 5, 6, 7, 8]
start = 2
stop = 5
step = 1

def slicing():
    print(a)
    # Basic
    print(a[start:stop])        # items start through stop-1
    print(a[start:])            # items start through the rest of the array
    print(a[:stop])             # items from the beginning through stop-1
    print(a[:])                 # a copy of the whole array
    print(a[start:stop:step])   # start through not past stop, by step
    # Negative index
    print(a[-1])                # last item in the array
    print(a[-2:])               # last two items in the array
    print(a[:-2])               # everything except the last two items
    # Negative step
    print(a[::-1])              # all items in the array, reversed
    print(a[1::-1])             # the first two items, reversed
    print(a[:-3:-1])            # the last two items, reversed
    print(a[-3::-1])            # everything except the last two items, reversed

if __name__ == "__main__":
    print('Slicing')
    slicing()
```

## More Syntax Tips

```python
from functools import reduce
from collections import defaultdict
from collections import deque

def syntax():
    # Map
    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, items))
    print(items, 'maps to', squared)
    # Filter
    items = list(range(-5, 5))
    less_than_zero = list(filter(lambda x: x < 0, items))
    print(items, 'filtered to', less_than_zero)
    # Reduce
    items = [1, 2, 3, 4]
    product = reduce((lambda x, y: x * y), items)
    print(items, 'reduced to', product)
    # Ternary 
    value_if_true, condition, value_if_false = 1, True, -1
    assigned = value_if_true if condition else value_if_false
    print('assigned is', assigned, 'because', condition)
    # Set
    items = [1, 1, 3, 3]
    set_of_items = set(items)
    print(set_of_items, 'is set of', items)
    # Defaultdict
    # Defaultdict
    def_dict = defaultdict(list)
    def_dict['key'].append(1)
    print(def_dict)
    def_dict = defaultdict(dict)
    def_dict['new_key']['second_key'] = 0
    print(def_dict)
    # Queue
    queue = deque(list(range(5)))
    val = queue.popleft()
    print(val, 'popped on the left and rest of the queue', queue)
    # Decorator
    def decor(func):
        def wrapping():
            print("Work before func()")
            func()
            print("Work after func()")
        return wrapping
    @decor
    def function_to_decor():
        print("Decorated work")
    function_to_decor()
    # Enumerate
    items = ['apple', 'banana', 'grapes', 'pear']
    for idx, elem in enumerate(items):
        print(idx, elem)
    # Zip
    first_name = ['Joe','Earnst','Thomas','Martin','Charles']
    last_name = ['Schmoe','Ehlmann','Fischer','Walter','Rogan','Green']
    age = [23, 65, 11, 36, 83]
    zipped = list(zip(first_name,last_name, age))
    first_name, last_name, age = list(zip(*zipped))
    print(zipped, first_name, last_name, age)
    # Comprehension
    input_list = [1,2,3,4,5,6,7,8,9,10]
    new_list = [x**2 for x in input_list if x%2 == 0]
    print(input_list, 'to', new_list)
    input_dict = {'a': 4, 'b': 6, 'c': 8}
    new_dict = {k+'_new': v//2 for k, v in input_dict.items() if v > 5}
    print(input_dict, 'to', new_dict)
    # Lambda
    list_of_pairs = [(1, 2), (4, 1), (9, 10), (13, -3)]
    list_of_pairs.sort(key=lambda x: x[1])
    print(list_of_pairs)

if __name__ == "__main__":
    print('Syntax Tips')
    syntax()
``` 


