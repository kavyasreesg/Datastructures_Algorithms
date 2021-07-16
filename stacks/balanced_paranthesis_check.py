from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        if not self.is_empty():
            return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def match_dict(ch1, ch2):
    match = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    return match[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ele in s:
        if ele in ['[', '(', '{']:
            stack.push(ele)
        if ele in [')', '}', ']']:
            if stack.size() == 0:
                return False
            if not match_dict(stack.pop(), ele):
                return False
    return True


print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
