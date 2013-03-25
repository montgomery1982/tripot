def return_if (a):
	a = int(a)
	if a > 0 and a < 10 :
		print a + 10
	elif a >10 and a<100 :
	 	print a * 0.1
	else:
		print False

a = raw_input("Input your number: ")
return_if(a)
