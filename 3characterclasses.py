#character classes
'''character classes provide a way to match only onw of a specific
 set of character. It is created by putting the chara inside []
[a-z] all lowercase alphabets
[A-Z] all uppercase alphabets
[0-9] matches any digit
[A-Za-z] matches a letter of any case
[i-u] all lowercase alphabets from i to u
 '''
import re
pattern=r"[aeiou]"

match = re.search(pattern,"prath")
if match:
	print("match fouhnd, "match.group())
	
#match fouhnd, a

match2=re.search(pattern,"rhythm")
if match2:
	print(match2.group())
else:
	print("no match")
	
#no match
'''
adding ^ at the start of a character class inverts it
[^A-Z] will accept only lowercase character
'''
pattern =r"[^a-z]"
if re.match(pattern,"prathmesh"):
	print("match")
else:
	print("accepts only UPPERcase")

#accepts only UPPERcase

