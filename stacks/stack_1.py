from collections import deque

stack = deque()
stack.append('www.youtube.com')
stack.append('www.google.com')
stack.append('www.kool.com')
print(stack)
stack.pop()
print(stack)
