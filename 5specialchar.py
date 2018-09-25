#special characters
'''
\d match any decimal digit, same as [0-9]
\D inverse of \d, do not match any numeric digit
\w match any alphanumeric character, same as [A-Za-z0-9]
\W inverse of \w
\s match any whitespace char,same as [ \n\t\r\v\f] eg. of\sthe
\S inverse of \s
\b match any word boundary eg. \bThe\b
\B inverse of \b
\c match any special char without its special meaning eg. \.,\\
\A match start of string
\Z match end of string
'''
import re
pattern=r"\w+-\d+"
if re.match(pattern,"a12-34"):
	print("matched")

#matched

if re.match(pattern,"12-asd"):
	print("matched")
else:
	print("not matched")

#not matched
	
pattern = r"\+91\s\d{10}"
if re.match(pattern,"+91 234567890"):
	print("matched")
else:
	print("not matched")

#not matched	
if re.match(pattern,"+91 1234567890"):
	print("matched")
	
#matched
 
pattern=r"\w+@\w+\.com"
if re.match(pattern,"abc1@gmail.com"):
	print("matched")
	
#matched

