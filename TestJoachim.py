import csv

def get_numbers(file_path) -> list[int]:
	numbers = []
	with open(file_path, newline='') as file:
		reader = csv.reader(file, delimiter=',')
		for row in reader:
			if row[0].isnumeric():
				numbers.append(row[1])
	return numbers

def main():
	res = input('please select a generator file (1 or 2): ')
	while res != '1' and res != '2':
		res = input('please select a generator file (1 or 2: ')

	file_path = f"generator{res}.csv"
	numbers = get_numbers(file_path)

if __name__ == '__main__':
	main()
