# implementation of quick sort algorithm

""" start is the index of first element of array,
    end is the index of last element of array"""

def partition(array,start,end):
	pivot = array[end]
	print "pivot : ",pivot
	pindex = start
	
	i = start
	while i < end:
		if array[i] <= pivot:
			array[i],array[pindex] = array[pindex],array[i]		# swap array[i] with array[pindex]
			pindex += 1
		i += 1
	array[pindex],array[end] = array[end],array[pindex]			# swap array[pindex] with array[end]
	return pindex
	
def Quicksort(array,start,end):
	
	# base case for recursion to occur
	if start >= end:
		return array

	# else recursive call occur
	pindex = partition(array,start,end)	
	Quicksort(array,start,pindex-1)
	Quicksort(array,pindex+1,end)

if __name__ == "__main__":
	array = [5,9,2,1,6,7,10]
	Quicksort(array,0,6)
	print array
