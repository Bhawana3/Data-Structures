# search element in the list using binary search

def binary_search(List,value):
	low = 0
	high = len(List) - 1
	while low <= high :			
		mid = (high + low)/2
		if List[mid] == value:
			return mid
		elif List[mid] < value:
			low = mid + 1
		else:
			high = mid - 1
	return -1

print binary_search([2,3,4,5,6,7,8],6)	
