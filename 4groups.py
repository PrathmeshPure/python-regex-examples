#groups   ()
import re
pattern=r"((prath)+(mesh*)?)"
match= re.match(pattern,"prathmeshh")
if match:
	print(".group()-",match.group())	#group() returns whole match
	print(".group(0)-",match.group(0)) 	#group(0) same as group()
	print(".group(1)-",match.group(1))	#group(1) 1st group from left
	print(".group(2)-",match.group(2))
	print(".groups()-",match.groups())	#groups() returns all groups from 1

'''	
>>>
.group()- prathmeshh
.group(0)- prathmeshh
.group(1)- prathmeshh
.group(2)- prath
.groups()- ('prathmeshh', 'prath', 'meshh')

''' 
