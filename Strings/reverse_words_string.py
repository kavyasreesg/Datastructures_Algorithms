"""
[::-1] has time complexity of O(N) and space complexity of O(1)
Rather than using loop and using temp variables for swap; using [::-1] is faster
"""


class Solution:

    def reverse(self, S):
        list_words = S.split('.')
        return '.'.join(list_words[::-1])


if __name__ == '__main__':
    obj = Solution()
    output = obj.reverse("i.like.this.program.very.much")
    print(output)
