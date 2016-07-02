# update index with multiplication of previos and next integers

def multiplication(array):
	n = len(array)
	# create myarray of same size of array
	myarray = [j for j in range(n)]		# using list comprehension myarray of fixed size has been made
	i = 0
	j = 0
	while i < len(array):
		if i == 0:
			myarray[j] = (array[i] * array[i+1])
		elif i == len(array)-1:
			myarray[j] = (array[i-1] * array[i])
		else:
			myarray[j] = (array[i-1] * array[i+1])
		i += 1
		j += 1
	return myarray 

print multiplication([1,2,3,4,5,6,7])
