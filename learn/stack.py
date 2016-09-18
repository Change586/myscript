#-*-encoding:utf-8-*-

from collections import deque

queue = deque(['a','b','c'])
queue.append('d')
queue.append('e')
queue.appendleft(5)
print queue
print queue.pop()
print queue
print queue.popleft()
print queue
stack = [1,2,3]
stack.append('a')
stack.append('efglist')
# t = stack.pop()
print stack
# print t

