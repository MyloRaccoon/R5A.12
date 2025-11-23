import fonctions
from scipy.special import gammaincc

def choice_of_m_and_k_and_n(string:str)->list[int]:
    length=len(string)
    if length>=750000:
        return [10000,6,75]
    elif length>=6272:
        return [128,5,49]
    elif length>=128:
        return [8,3,16]
    return [00,0,]


def list_pi(k:int,m:int)->list[float]:
    if k==3:
        return [0.2148,0.3672,0.2305,0.1875]
    elif k==5 and m==128:
        return [0.1174,0.2430,0.2493,0.1752,0.1027,0.1124]
    elif k==5 and m==512:
        return [0.1170,0.2460,0.2523,0.1755,0.1027,0.1124]
    elif k==5 and m==1000:
        return [0.1307,0.2437,0.2452,0.1714,0.1002,0.1088]
    elif k==6 and m==10000:
        return [0.0882,0.2092,0.2483,0.1933,0.1208,0.0675,0.0727]
    return [0.0]

def calcul_max_run(value:str,m:int,k:int)->list[int]:
    cpt_max=0
    cpt=0
    cpt_iter=0
    result:list[int]=[]
    for _j in range(k+1):
        result.append(0)
    for i in value:
        cpt_iter+=1
        if i =="1":
            cpt+=1
            if cpt>cpt_max:
                cpt_max=cpt
        else:
            cpt=0
        if cpt_iter==m:
            if cpt_max>0:
                result[cpt_max-1]=result[cpt_max-1]+1
            cpt_iter=0
            cpt=0
            cpt_max=0
    return result
        
def calcul_stat(list_result:list[int],v:list[float],n:int)->float:
    res:float=0
    for i in range(len(list_result)):
        list_value=list_result[i]
        print("list_value",list_value)
        print("list_p : ",v[i])
        res=res+((list_value-(n*v[i]))**2/(n*v[i]))
    return res
        
def P_value(k:int,stat:float)->float:
    print("k: ",k," stat : ",stat)
    return gammaincc(k/2,stat/2)

def test_passed(value:float):
    if value > 0.01:
        return True
    return False
    
if __name__ == '__main__':
    print("Test 4")
    list_csv=fonctions.get_numbers('generator1.csv')
    all_in_one=fonctions.recup_all_in_one(list_csv)
    print(len(all_in_one))
    test_value="11001100000101010110110001001100111000000000001001001101010100010001001111010110100000001101011111001100111001101101100010110010"
    test_list_m_k_n=choice_of_m_and_k_and_n(test_value)
    test_m:int=test_list_m_k_n[0]
    test_k:int=test_list_m_k_n[1]
    test_n:int=test_list_m_k_n[2]
    list_pi_v:list[float]=list_pi(test_k,test_m)

    print(test_m)
    print(test_k)
    print(test_n)
    
    list_result=calcul_max_run(test_value,test_m,test_k)
    print(list_result)
    stat=calcul_stat(list_result,list_pi_v,test_n)
    print(stat)
    value_final=P_value(test_k,stat)
    print(value_final)

