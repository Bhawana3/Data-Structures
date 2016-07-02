# reverse elements of array

def reverse_array(array):
	start = 0
	end = len(array) - 1
	while start < end :
		array[start],array[end] = array[end],array[start]
		start += 1
		end -= 1
	return array

if __name__ == "__main__":
	print "Menu : "
	print "reversed elements of array"
	print reverse_array([12,3,4,5,6,7,1])
