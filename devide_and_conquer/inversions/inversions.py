import sys

class Sorter():
	def __init__(self):
		self.n = 0
	
	def get_n(self):
		return self.n

	def startsort(self, arr):
		self.n = 0
		return self.mergesort(arr)

	def merge(self, x, y):
		z = []
		while len(x) > 0 and len(y) > 0:
			if x[0] <= y[0]:
				z.append(x[0])
				x.remove(x[0])
			else:
				for item in x:
					if item > y[0]:
						self.n += 1
				z.append(y[0])
				y.remove(y[0])
		while len(x) > 0:
			z.append(x[0])
			x.remove(x[0])

		z.extend(y)
		return z

	def mergesort(self, arr):
		if len(arr) <=1:
			return arr

		middle = int(len(arr) / 2)
		return self.merge(self.mergesort(arr[:middle]), self.mergesort(arr[middle:]))

x = Sorter()

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

        print(x.startsort(arr1))
        print(x.get_n())
else:
        print([])
        print(0)
