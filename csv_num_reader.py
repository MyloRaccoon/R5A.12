import csv

def get_numbers(file_path: str) -> list[list[int]]:
	numbers = []
	with open(file_path, newline='') as file:
		reader = csv.reader(file, delimiter=',')
		for row in reader:
			if row[0].isnumeric():
				numbers.append(list(map(int, list(row[1]))))
	return numbers