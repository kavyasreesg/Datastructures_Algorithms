"""
Remove duplicate characters and just
keep one occurance of the duplicate character
"""
class Solution:
	def removeDups(self, S):
		t = ''
		for i in S:
		    if i in t:
		        pass
		    else:
		        t = t+i
		return t