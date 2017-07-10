import sys

def quicksort(arr):
	arr = helpersort(arr, 0, len(arr) - 1)
	return arr

def helpersort(arr, low, pivote):
	if pivote - low <= 1:
		return arr

	count = low
	for i in range(low,pivote):
		if arr[i] < arr[pivote]:
			arr[i], arr[count] = arr[count], arr[i]
			count += 1

	arr[pivote], arr[count] = arr[count], arr[pivote]
	
	arr = helpersort(arr, low, count - 1)
	arr = helpersort(arr, count + 1, pivote)

	return arr

def replaces(arr, i, j):
	arr[i] = arr[i].replace('[', '')
	arr[j] = arr[j].replace(']', '')
	return arr

if len(sys.argv) > 1:
	arr = sys.argv[1:]

	if len(arr) == 1:
		arr = replaces(arr, 0, 0)
		arr = arr[0].split(',')

	n = len(arr)
	arr = replaces(arr, 0, n-1)
	
	arr1 = []
	for i in range(0, n):
		if arr[i] != '' and arr[i] != '':
			arr[i] = arr[i].replace(',', '')
			arr1.append(int(arr[i]))

	print(quicksort(arr1))
else:
	print([])
