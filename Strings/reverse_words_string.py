class Solution:
    
    def reverse(self, S):
        list_words = S.split('.')
        return '.'.join(list_words[::-1])
    
if __name__ == '__main__':
    
    obj = Solution()
    output = obj.reverse("i.like.this.program.very.much")
    print(output)