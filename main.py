from test2 import test2
from test1 import test1
from csv_num_reader import get_numbers

def main():

	print("	TEST FOR GENERATOR 1")
	numbers_csv1 = get_numbers("generator1.csv")

	print('		Test 1')
	i = 0
	n_error = 0
	for number in numbers_csv1:
		if not test1(number) > 0.01:
			print(f'test not passed for number at index {i}')
			n_error += 1
		i += 1

	print('		Test 2')
	i = 0
	n_error = 0
	for number in numbers_csv1:
		if not test2(number) > 0.01:
			print(f'test not passed for number at index {i}')
			n_error += 1
		i += 1

	print('		Test 3')
	print('TODO')

	print('		Test 4')
	print('TODO')




	print("	TEST FOR GENERATOR 2")
	numbers_csv2 = get_numbers("generator2.csv")

	print('		Test 1')
	i = 0
	n_error = 0
	for number in numbers_csv2:
		if not test1(number) > 0.01:
			print(f'test not passed for number at index {i}')
			n_error += 1
		i += 1

	print('		Test 2')
	i = 0
	n_error = 0
	for number in numbers_csv2:
		if not test2(number) > 0.01:
			print(f'test not passed for number at index {i}')
			n_error += 1
		i += 1

	print('		Test 3')
	print('TODO')

	print('		Test 4')
	print('TODO')

if __name__ == '__main__':
	main()