import sys

def prepare(in1, in2):
	in1 = str(in1)
	in2 = str(in2)
	if len(in1) == len(in2):
		return multiply(in1, in2)
	else:
		return 'values with different digits number are not supported'

def multiply(x, y):
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)

    a = int(x[:int(len(x)/2)])
    b = int(x[int(len(x)/2):])
    c = int(y[:int(len(x)/2)])
    d = int(y[int(len(x)/2):])
    if len(x) <= 4:
        step1 = a * c
        step2 = b * d
        step3 = a * d + b * c
    else:
        step1 = multiply(str(a), str(c))
        step2 = multiply(str(b), str(d))
        step3 = multiply(str(a), str(d)) + multiply(str(b), str(c))
    n = int(len(x))
    return (10**n) * step1 + step2 + (10**(n/2)) * step3

if len(sys.argv) == 3:
	print(prepare(int(sys.argv[1]), int(sys.argv[2])))
else:
	print('You must enter two numbers with the same digits number')
