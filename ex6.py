#exercise 6
#setting the value of text variables. this one uses a formatter
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those %s." % (binary, do_not)

# printing variables
print x
print y

#combining a new string with previously defined text variable and printing it. 
#Using %r will output a direct quote

print "I said: %r." % x

#combination again, but using %s you have to place the quotes around what you want
#quoted
print "I also said: '%s'." % y

#setting a boolean variable
hilarious = False

#combining a boolean variable with a text output
joke_evaluation = "Isn't that joke so funny ?! %r"

#prints the evaluation with the formatter variable hilarious
print joke_evaluation % hilarious


#assigning text string variable values
w = "This is the left side of..."
e = "a string with a right side."

#adding variables and printing output. it appears this is another way to 
#concatenate text
print w + e
