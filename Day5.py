def lines(text,num):
	for i in range(0,len(text),num):
		print(text[i-num:i])
		lastI=i
	print(text[lastI:len(text)])
lines("ABCDEFGHIJKLIMNOQRSTUVWXYZ",2)