res = 0

def solve (n, repeats):
	global res
	number = int(f'{n}' * repeats)
	res += number
	if repeats == 1: return print(res)
	return res,solve(n, repeats - 1)
