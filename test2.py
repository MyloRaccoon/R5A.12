import csv
import math
from scipy.special import gammaincc
from csv_num_reader import get_numbers

# n = 16 | m = 8
def test2(number: str, N = 200, M = 128, verbos = False) -> float:

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


	if verbos:
		print(f'prs = {prs}')


	weird_sum = 0
	for pr in prs:
		weird_sum += (pr - 1/2)**2

	val = 4 * M * weird_sum

	if verbos:
		print(f'val = {val}')

	igamcc = gammaincc(N/2, val/2)

	if verbos:
		print(f'igamcc = {igamcc}')

	return igamcc

def test():
	n = '1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000'
	res = test2(n, 10, 10, True)

	assert res == 0.7064384496412808

if __name__ == '__main__':
	test()