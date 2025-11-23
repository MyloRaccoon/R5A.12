import csv
import math
from scipy.special import gammaincc
from csv_num_reader import get_numbers

# n = 16 | m = 8
def test2(number: list[int], N, M) -> bool:

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
			if n == 1:
				pr += 1
		prs.append(pr/M)



	weird_sum = 0
	for pr in prs:
		weird_sum += (pr - 1/2)**2

	val = 4 * M * weird_sum

	igamcc = gammaincc(N/2, val/2)

	return igamcc

def main():
	res = input('please select a generator file (1 or 2): ')
	while res != '1' and res != '2':
		res = input('please select a generator file (1 or 2: ')

	file_path = f"generator{res}.csv"
	numbers = get_numbers(file_path)
	
	i = 0
	n_error = 0
	for number in numbers:
		if not test2(number, 16, 8) > 0.01:
			print(f'test not passed for number at index {i}')
			n_error += 1
		i += 1

def test():
	n_str = '1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000'
	n = list(map(int, list(n_str)))
	res = test2(n, 10, 10)

	assert res == 0.7064384496412808

if __name__ == '__main__':
	main()