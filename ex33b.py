i = 0
numbers = []
max_it = 77
step_it = 3

for num in range(0,max_it,step_it):
	print "At the top i is %d" % num
	numbers.append(num)
	#i = i + step_it
	print "Numbers are now: ", numbers
	print "At the bottom i is %d" % num


print "The numbers : "

for num in numbers:
	print num

