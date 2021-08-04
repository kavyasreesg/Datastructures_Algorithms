"""
An anagram of a string is another string that contains the same 
characters, only the order of characters can be different

Time Complexity of sorted function is O(nlogn)
"""
def check_anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        print("Anagrams")
    else:
        print("Not anagram")
        
s1 = "listen"
s2 = "stenli"
check_anagram(s1,s2)

"""
Method 2 : Count frequency of each character in both S1 and S2 and store it in
count array.
If both are same then they are anagrams
There can be 256 possible characters
Space complexity is O(N) and Time Complexity is O(N) where N is number of
    characters possible (i.e., 256)
"""
def anagram(S1, S2):
    count1 = [0] * 256
    count2 = [0] * 256
    for i in S1:
        count1[ord(i)] += 1
    for i in S2:
        count2[ord(i)] += 1
    if len(S1) != len(S2):
        return False
    for i in range(256):
        if count1[i] != count2[i]:
            return False
    return True

str1 = "GeeksforGeeks"
str2 = "forgeeksGeeks"
print(anagram(str1, str2))

"""
Method 3: Also, we can use single count array to check if two strings are anagrams
Time Complexity : O(N) and Space Complexity is O(N)
"""
def anagram_meth_3(S1, S2):
    count1 = [0] * 256
    
    if len(S1) != len(S2):
        return False
    
    for i in range(len(S1)):
        count1[ord(S1[i])] += 1
        count1[ord(S2[i])] -= 1
    
    for i in range(256):
        if count1[i] != 0:
            return False
    return True

str1 = "GeeksforGeeks"
str2 = "forGeeksGeeks"
print(anagram(str1, str2))