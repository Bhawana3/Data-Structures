def insertionSort(array):
	for index in range(len(array)):
		currentvalue = array[index]
		position = index
		while position > 0 and array[position-1] > currentvalue:
			array[position] = array[position-1]
			position = position - 1
		array[position] = currentvalue  
	return array	

print insertionSort([2,5,3,1,9])
