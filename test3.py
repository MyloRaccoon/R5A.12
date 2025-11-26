import csv
from math import sqrt
from math import erfc

def open_csv():
    with open('generator1.csv', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            print(', '.join(row))

def get_numbers(file_path:str) -> list[str]:
    numbers:list[str] = []
    with open(file_path, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0].isnumeric():
                numbers.append(row[1])
    return numbers


def calcul_test3(fr:float,val:float,length_list:int):
    stat = (abs(val - length_list * 2 * fr * (1 - fr)) / (2 * sqrt(2 * length_list) * fr * (1 - fr)))

    print("stat = ",erfc(stat))
    return erfc(stat)
def number_suits(sequence:str):
    length_seq=len(sequence)
    c_1=0
    for i in sequence:
        if i == '1':
            c_1+=1
    print(c_1)
    fr=c_1/length_seq
    val=suit(sequence,length_seq)
    return fr,val,length_seq

def suit(sequence:str,len:int):
    cpt=0
    for i in range(len):
        v=sequence[i-1]
        v2=sequence[i]
        if v!=v2:
            cpt+=1
    return cpt

def good(res_calcul:float)->bool:
    if res_calcul<0.01:
        return False
    return True


def Test3(line:str):
    fr, val, length = number_suits(line)
    print("fr : ",fr)
    print("val : ",val)
    print("length : ",length)
    res = calcul_test3(fr, val, length)
    print("Is good :",good(res))

def recup_all_in_one(list:list[str]):
    result=""
    for i in list:
        result += i
    return result


if __name__ == '__main__':
    Test3("1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000")
    list_csv=get_numbers('generator1.csv')
    all_in_one=recup_all_in_one(list_csv)
    print(all_in_one)
    Test3(all_in_one)
    list_csv=get_numbers('generator2.csv')
    all_in_one=recup_all_in_one(list_csv)
    Test3(all_in_one)
