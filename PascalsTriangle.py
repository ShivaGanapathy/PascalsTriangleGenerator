'''
create a program that will result in an output of n rows of Pascal's Triangle
ex. if n is 3 the out put should look like this:
  1
 1 1
1 2 1
'''


def get_input():
	"""
	This Function handles the user input process, ensuring that the user enters an positive integer.
	The Function has no arguments and returns an integer that the user enters.
	"""

	#this while loops ensures the user enters an input
	inputFetched = False
	while inputFetched == False:

		#this try-except statement validates the entry of a string
		try: 
			n = int(input("How many rows of Pascal's Triangle do you need?"))

			#this if block validates the number inputted is positive
			if n <0:
				print("Please enter a positive number")
			else:
				inputFetched = True
				return n

		except: 
			print("Please enter a number")





def populateList(n):
	'''
	This function populates a list of lists, each list containing a row of Pascal's Triange
	The function expects a positive integer, n, and returns n rows of Pascal's Triangle
	'''

	allRows = []

	#if no rows are wanted, the function returns an empty list
	if n == 0 :
		return allRows


	for rowNumber in range(1,n+1):

		#rowList stores all numbers in each row of the Triangle. It is initalized with a 1

		rowList = [1,]

		#if the current row is one, the else code is Not Applicable
		if rowNumber == 1:
			pass

		else:
			#stores the previous row of the triangle in previousRow
			previousRow = allRows[rowNumber-2]

			for i in range(len(previousRow)):

				#if there are no new numbers to add, end loop
				if i == len(previousRow)-1:
					break

				#adds two numbers and appends it to new row
				else: 
					sumNumber=  previousRow[i] + previousRow[i+1]
					rowList.append(sumNumber)


			#after end of adding numbers, add an aditional 1
			rowList.append(1)




		#adds row to list of rows after the new row is formed
		allRows.append(rowList)

	return allRows







def prettyPrint(array):
	'''
	This function takes a list of lists, and prints in a nicer, more readable and triangular manner
	'''

	size = len(array)
	for i in range(len(array)):
		space = " "

		print((size-i)*space, array[i], (size-i)*space)




def main():
	n = get_input()
	data = populateList(n)
	prettyPrint(data)


main()
