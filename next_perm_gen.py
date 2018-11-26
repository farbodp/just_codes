from math import factorial

def perm_gen(lst):
	if len(lst)==0:
		yield []
	if len(lst)==1:
		yield lst
	for n in range(factorial(len(lst))):
		i = len(lst)-1
		while lst[i-1]>=lst[i]:
			i -= 1
		j = len(lst)-1
		while lst[j]<=lst[i-1]:
			j -= 1
		lst[i-1], lst[j] = lst[j], lst[i-1]
		lst[i:] = lst[len(lst)-1:i-1:-1]
		yield lst


if __name__ == '__main__':
	a = perm_gen([1, 3, 2, 7, 6, 4])
	print(next(a))
	print(next(a))
	print(next(a))
	