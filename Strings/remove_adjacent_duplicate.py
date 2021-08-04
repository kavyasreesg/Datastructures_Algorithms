"""
The problem is to remove adjacent duplicate characters in a string.
Eg : geeksforgeeks should return gksforgks
The idea is to use stack.
Loop through length of string
    whenever current char and ith character are equal and i > 0
        decrement i by -1
    else
        add current char to stack
        Increment i
"""


def remove(S):
    i = 0
    stack = []
    for j in range(len(S)):
        curr = S[j]
        if i > 0 and stack[i - 1] == curr:
            i -= 1
        else:
            stack.insert(i, curr)
            i += 1
    return ''.join(stack[:i])


def remove1(S):
    res = []
    i = 0
    while i < len(S):
        if i + 1 < len(S) and S[i] != S[i + 1]:
            res.append(S[i])
        if i + 1 < len(S) and S[i] == S[i + 1]:
            while S[i] == S[i + 1]:
                i += 1
            i += 1
        i += 1
    if i == len(S):
        res.append(S[i-1])
    return ''.join(res)


out = remove1("abaacca")
print(out)
