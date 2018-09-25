#metacharacters
'''
.(dot) -any character other than a new line
^	- start of a string
$	- end of a string
'''
import re
pattern = r"se." #start with se and end with any char except new line
if re.match(pattern,"see"):
	print("match 1")

#>>>match 1

if re.match(pattern,"sea"):
	print("match 2")

#>>>match 2

if re.match(pattern,"sae"):
	print("match" 3)
else:
	print("no match 3")
	
#>>>no match 3

pattern=r"^pr..h$"	#string should start with pr then follow with any 2 char and end with h
if re.match(pattern,"prath"):
	print("match 1")

#match 1

if re.match(pattern,"print"):
	print("match 2")
else:
	print("no match 2")

#no match 2

if re.match(pattern,"prh"):
	print("match 3")
else:
	print("no match 3")
#no match 3
'''
*	-zero or more repetitions		# h*
+	-one or more repetitions		# (prath)+
?	-zero or one repetitions		#(mesh*)?
{x,y}	-number of repetitions between x and y(numbers)
''' 
pattern=r"((prath)+(mesh*)?)"
if re.match(pattern,"prathmeshhhh"):
	print("matched")
	
#matched
if re.match(pattern,"prath"):
	print("look,it is also matched")
	
#look,it is also matched
if re.match(pattern,"prathmesh"):
	print("and this one also")
	
#and this one also
if re.match(pattern,"prank"):
	print("never gonna print this")
else:
	print("no chances to match")

#no chances to match
if re.match(pattern,"prathprathmeshhh"):
	print("yeahh,matched")

#yeahh,matched


passwd=r"[A-Za-z0-9]{6,}"
if re.match(passwd,"99999"):
	print("ok")
else:
	print("password should be more than 6 digits")
	
#password should be more than 6 digits
if re.match(passwd,"ASdcscasd12"):
	print("ok")
else:
	print("password should be more than 6 digits")
	
#ok
