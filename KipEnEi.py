from random import randint
from random import seed

seed(1)

def generateNumber():
	stop = 4
	numberString = ''
	for i in range(stop):
		numberString = numberString + '' + randint(0,10)
	
	print(numberString)

generateNumber()