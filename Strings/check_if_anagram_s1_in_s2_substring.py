"""
Check if a string contains an anagram of another string 
as its substring
"""
def check(S1, S2):
    s1hash = [0] * 26
    s2hash = [0] * 26
    s1len = len(S1)
    s2len = len(S2)
    
    if s1len > s2len:
        return False
    
    left = 0
    right = 0
    
    while right < s1len:
        
        s1hash[ord(S1[right])-97] += 1
        s2hash[ord(S2[right])-97] += 1
        right += 1
    
    right -= 1
    
    while right < s2len:
        
        if s1hash == s2hash:
            return True

        right += 1
        
        if right != s2len:
            
            s2hash[ord(S2[right])-97] += 1
        
        s2hash[ord(S2[left])-97] -= 1
        left += 1
        
    return False

if __name__ == '__main__':
    
    s1 = "abc"
    s2 = "abbcdba"
    
    if check(s1, s2):
        print("YES, String 1's permutation is a substring of String 2")
    else:
        print("NO, String 1's permutation is not a substring of String 2")