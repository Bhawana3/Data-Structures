# merge two arrays

def merge(left,right,array):

	length_of_left = len(left)
	length_of_right = len(right)

	index_of_left = 0
	index_of_right = 0
	index_of_array = 0
	
	while index_of_left < length_of_left and index_of_right < length_of_right:
		if left[index_of_left] > right[index_of_right]:
			array[index_of_array] = right[index_of_right]
			index_of_right += 1
			index_of_array += 1
		else:
			array[index_of_array] = left[index_of_left]
			index_of_left += 1
			index_of_array += 1

	# one of the left or right array will exhaust first, therefore if it is right array then
	while index_of_left < length_of_left:
		array[index_of_array] = left[index_of_left]
		index_of_left += 1
		index_of_array += 1
	
	while index_of_right < length_of_right:
		array[index_of_array] = right[index_of_right]
		index_of_right += 1
		index_of_array += 1
	
	return array
	
def mergeSort(array):
	length_of_array = len(array)
	# base case
	if length_of_array < 2:
		return array
	# else
	mid = length_of_array/2
	# left array will be
	left = array[0:mid]
	print "left :",left
	right = array[mid:length_of_array]
	print "right :",right
	for i in range(len(left)):
		left[i] = array[i]
	
	j = mid
	while j < len(right):
		right[j-mid] = array[j]
		j += 1

	mergeSort(left)
	mergeSort(right)
	return merge(left,right,array)


if __name__ == "__main__":
	print mergeSort([65,56,1,87,10,0,15,3,4,2])
