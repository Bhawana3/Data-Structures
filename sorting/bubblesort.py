def bubble_sort(array):
	i = len(array)
	while i >= 0:
		j = 0
		while j < i-1:
			if array[j] > array[j+1]:
				array[j],array[j+1] = array[j+1],array[j]
			j += 1
		i -= 1
	return array
array = [4,20,45,63,34,9]
print bubble_sort(array)

def bubbleSort(alist):
    sort = True
    passnum = len(alist)-1
    while passnum > 0 and sort:
	sort = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
		sort = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
	passnum -= 1
    return alist

alist = [54,26,93,17,77,31,44,55,20]
print bubbleSort(alist)

