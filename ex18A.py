#converts measurements with nested functions

print "What temperature do you want to convert?"
temperature = raw_input(">")

def temp_F(tempF):
	print "The temperature is %r degrees Farenheit" % tempF

def convert_temp():
	tempC = (temperature - 32)/1.8
	print "The temperature is %r degrees Celsius" % tempC
	
temp_F(temperature)
convert_temp()
