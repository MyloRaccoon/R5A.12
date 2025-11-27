import csv
import math
from scipy.special import gammaincc
from fonctions import get_numbers, recup_all_in_one

# 6400/4 : pass pass
# 3200/8 : pass pass
# 1600/16: pass pass
# 800/32 : fail fail
# 400/64 : fail fail
# 200/128: fail pass

DEFAULT_N = 200
DEFAULT_M = 128


def test2(number: str, N = DEFAULT_N, M = DEFAULT_M, verbos = True) -> bool:

	if verbos:
		print(f'N = {N} | M = {M}')

	splited_number = []
	i = 0
	temp = []
	for n in number:

		temp.append(n)
		i += 1

		if i == M:
			i = 0
			splited_number.append(temp.copy())
			temp = []

	prs = []

	for part in splited_number:
		pr = 0
		for n in part:
			if n == '1':
				pr += 1
		prs.append(pr/M)


	# if verbos:
	# 	line = ''
	# 	for pr in prs:
	# 		line += (f'{pr} |')
	# 	print(f'prs: {line}')


	weird_sum = 0
	for pr in prs:
		weird_sum += (pr - 1/2)**2

	val = 4 * M * weird_sum

	if verbos:
		print(f'val = {val}')

	igamcc = gammaincc(N/2, val/2)

	if verbos:
		print(f'igamcc = {igamcc}')

	return igamcc > 0.01

def main():
	n = '1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000'
	assert test2(n, 10, 10, False)
	print('')

	print("Generator 1")
	numbers = recup_all_in_one(get_numbers("generator1.csv"))
	print(test2(numbers))

	print('')

	print("Generator 2")
	numbers = recup_all_in_one(get_numbers("generator2.csv"))
	print(test2(numbers))

if __name__ == '__main__':
	main()
