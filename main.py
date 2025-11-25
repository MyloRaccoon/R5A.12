from test2 import test2
from test1 import test1
from fonctions import get_numbers, recup_all_in_one

def main():

	print("	TEST FOR GENERATOR 1")
	numbers_csv1 = recup_all_in_one(get_numbers("generator1.csv"))

	print(f'Test 1 {test1(numbers_csv1) > 0.01}')

	print(f'Test 2 {test2(numbers_csv1) > 0.01}')




	print("	TEST FOR GENERATOR 2")
	numbers_csv2 = recup_all_in_one(get_numbers("generator1.csv"))

	print(f'Test 1 {test1(numbers_csv2) > 0.01}')

	print(f'Test 2 {test2(numbers_csv2) > 0.01}')



if __name__ == '__main__':
	main()