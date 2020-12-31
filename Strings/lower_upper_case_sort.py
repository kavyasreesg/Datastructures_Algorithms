"""Given a string S consisting of uppercase and lowercase characters. The task is to sort uppercase and lowercase letters 
separately such that if the ith place in the original string had an Uppercase character then it should not have a lowercase 
character after being sorted and vice versa."""

"""
steps to solve this challenge is
1) Store lower and upper case letters in two different arrays.
2) Sort both the arrays
3) Then check for each letter in the string and if it is lower case sort with corresponding letter in array
"""


def caseSort(s, n):
    s = list(s)
    v1 = []
    v2 = []
    for i in range(n):
        if s[i] >= 'a':
            if s[i] <= 'z':
                v1.append(s[i])
        if s[i] >= 'A':
            if s[i] <= 'Z':
                v2.append(s[i])
    v1 = sorted(v1)
    v2 = sorted(v2)
    i = 0
    j = 0
    for k in range(n):
        if s[k] >= 'a':
            if s[k] <= 'z':
                s[k] = v1[i]
                i = i + 1
        if s[k] >= 'A':
            if s[k] <= 'Z':
                s[k] = v2[j]
                j = j + 1
    return "".join(s)


if __name__ == '__main__':
    print(caseSort('defRTSersUXI', 12))
