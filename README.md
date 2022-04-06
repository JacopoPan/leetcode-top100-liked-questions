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
# import pdb; pdb.set_trace()
from typing import List

class Problem:
    def __init__(self):
        pass

    def methodOne(self, argName: List[int]) -> int:
        return -1

def main():
    sol = Problem()
    ans = sol.methodOne([0,0,0])
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

## Syntax Tips

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
