import csv

def recup_all_in_one(list:list[str]):
    result=""
    for i in list:
        result += i
    return result


def get_numbers(file_path:str) -> list[str]:
    numbers:list[str] = []
    with open(file_path, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0].isnumeric():
                numbers.append(row[1])
    return numbers

def open_csv():
    with open('generator1.csv', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            print(', '.join(row))