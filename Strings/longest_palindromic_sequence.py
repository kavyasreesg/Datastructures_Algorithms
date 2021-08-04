"""
    Return longest Palindrome in the String.
    This can be achieved by using two pointers and comparing whether they are
    equal until length of String.
    Time Complexity is O(N*N)
    Space is O(N)
"""


def longest_palindromic_sequence(S):
    def helper(l, r):
        while l >= 0 and r < len(S) and S[l] == S[r]:
            l -= 1
            r += 1
        return S[l + 1:r]

    res = ''
    for i in range(len(S)):
        test_pal = helper(i, i)
        if len(test_pal) > len(res):
            res = test_pal
        test_pal = helper(i, i + 1)  # For even numbers of chars in String input
        if len(test_pal) > len(res):
            res = test_pal
    return res


result = longest_palindromic_sequence("BABAD")
print(result)
