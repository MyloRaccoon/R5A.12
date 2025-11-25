import math

def test1(numbers: str, verbos = False) -> float:
	n_size = len(numbers)

	n_zero = 0
	n_one = 0
	for n in numbers:
		match n:
			case '0': n_zero += 1
			case '1': n_one +=1

	fr = n_one * 1 + n_zero * (-1)

	if verbos:
		print(f'fr = {fr}')

	val = abs(fr) / math.sqrt(n_size)

	if verbos:
		print(f'val = {val}') 

	erfc = math.erfc(val/math.sqrt(2))

	if verbos:
		print(f'erfc = {erfc}')

	return erfc

def test():
	n = '1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000'
	res = test1(n, True)

	assert res == 0.10959858339911599

if __name__ == '__main__':
	test()

