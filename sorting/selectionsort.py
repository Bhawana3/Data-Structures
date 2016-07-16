def selectionSort(List):
	for i in range(len(List)-1):
		mini = i
		j = i + 1
		while j < len(List):
			if List[j] < List[mini]:
				mini = j
			j += 1
		temp = List[i]
		List[i] = List[mini]
		List[mini] = temp
	return List

print selectionSort([1,56,29,10,5,3,4])


def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

