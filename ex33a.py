i = 0
numbers = []
max_it = 15
step_it = 2

def loop_it(i,numbers):	
	while i < max_it:
		print "At the top i is %d" % i
		numbers.append(i)
		i = i + step_it
		print "Numbers are now: ", numbers
		print "At the bottom i is %d" % i

loop_it(i,numbers)

print "The numbers : "

for num in numbers:
	print num

