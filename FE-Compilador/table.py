#!/usr/bin/python3

print("  ",end=";")
for j in range(39,46):
	print(chr(j),"",end=";")
for j in range(48,58):
	print(chr(j),"",end=";")
for j in range(59,63):
	print(chr(j),"",end=";")
for j in range(91,94):
	print(chr(j),"",end=";")
for j in range(97,123):
	print(chr(j),"",end=";")
print()

for i in range(67):
	print(i,end=";")
	for j in range(39,46):
		if   (i == 0) and (j == 39):
			print(20,end=";")			
		if   ((i == 20) or (i == 35)) and (j == 39):
			print(36,end=";")
		else :
			print(-1,end=";")
	for j in range(48,58):
		if   ((i == 0) or (i == 8) or (i == 11) or (i == 14)) and (j <= 57) and (j >= 48):
			print(11,end=";")
		elif i == 0 and (j == 43):
			print(8,end=";")
		elif i == 0 and (j == 45):
			print(14,end=";")
		elif ((i == 20) or (i == 35)) and (j <= 57) and (j >= 48):
			print(35,end=";")
		else:
			print(-1,end=";")
	for j in range(59,63):
		print(-1,end=";")
	for j in range(91,94):
		print(-1,end=";")
	for j in range(97,123):
		print(" 4",end=";")
	print()

