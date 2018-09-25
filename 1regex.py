#regular expression
'''standard library re.
commonly used task is to verify that string match a pattern
and performing a substitution in a string.
raw strings expressed as r"expression".
'''
import re
pattern=r"prath"

if re.match(pattern,"prathmeshprath"):
	print("match")
else:
	print("no match")
#match
'''re.match function can be used to determine whether it matches
at the beginnnig of a string.

other functions to match patterns are re.search and re.findall
'''
if re.search(pattern,"pureprathmesh"): #finds a pattern anywhere in a string
	print("match")
else:
	print("no match")
#match
print(re.findall(pattern,"prathmeshpureprahprath")) #returns all substrings that match
#['prath', 'prath']
'''
#methods
group returns the string matched.
start and end return the start and end position of first match.
span rerturns the start and end position as a tuple'''
match=re.search(pattern,"paaatprathm")
if match:
	print(match.group())
	print(match.start())
	print(match.end())
	print(match.span())
'''
prath
5
10
(5, 10)
''' 
#search and replace
'''
syntax: re.sub(pattern,repl,string,max=0)
this method replaces all occurances of the pattern in string
with repl,substituting all occurances,unless max provided.
'''
pattern2="prathmesh"
stirng="you can call me prathmesh."
newstr=re.sub(pattern2,"prath",str)
print(newstr)
#you can call me prath
