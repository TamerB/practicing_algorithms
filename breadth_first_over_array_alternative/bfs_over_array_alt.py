import sys

def search(arr):
	arr1 = []
	arr1.extend(arr)
	count = 0
	i = j = 0
	r = len(arr1)
	c = len(arr1[0])
	for i in range (0, r):
		for j in range(0, c):
			if arr1[i][j] == 1:
				if not (i-11>0 and arr1[i-1][j] == 2) and not (j-1>0 and arr1[i][j-1] == 2) and not (i+1<r and arr1[i+1][j] == 1) and not (j+1 < c and arr1[i][j+1] == 1):
					count += 1

				arr1[i][j] = 2

	return count

def replaces(arr, i, j):
        temp = arr.replace('[', '')
        temp = temp.replace(']', '')
        return temp

if len(sys.argv) > 1 and sys.argv[1] != '[]' and sys.argv[2] != '[]':
        arr = sys.argv[1:]

        arr[0] = replaces(arr[0], 0, 0)
        arr[1] = replaces(arr[1], 0, 0)

        arr[0] = arr[0].split(',')
        arr[1] = arr[1].split(',')

        r = len(arr)
        c = len(arr[0])

        for i in range(0, r):
                for j in range(0, c):
                        arr[i][j] = int(arr[i][j])
        print(search(arr))
else:
        print(0)
