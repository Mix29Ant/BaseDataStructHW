# 1st program (Arithmetic)
result1=(pow(9,0.5))*5
print(result1)
input('1st ended')
# 2nd program (Easy logic)
check_var=bool((9.99>9.98)and(1000!=1000.1))

#      1st variant of solution
if check_var:
    print('True')
else:
    print("False")

#      2nd variant of solution
print((9.99>9.98)and(1000!=1000.1))

input('2nd ended')
# 3rd program (School's brainteaser)
math_result_no_priority=2*2+2
math_result_with_addition_priority=2*(2+2)
print(math_result_no_priority)
print(math_result_with_addition_priority)

input('3rd ended')
# 4th program (The first after Dot)

#      Easy decision
dot_str='1234.56'
def find_dot(chk_str):
    len_str= int(len(chk_str))
    ret_i=0
    i=0
    print('test string lenght is:', len_str)
    while len_str>i :
        print('Scan pos :', i)
        if chk_str[i]=='.' :
            i = i + 1
            ret_i = i
            print('Dot found at position: ',ret_i)
            break
        else :
            i = i + 1
    return ret_i


if type(dot_str) != str:
    print('Wrong type')
    pass
else:
    n=find_dot(dot_str)
    if n>0:
        print('VASHA CYFRA :',dot_str[n])
    else:
        print("Dot didn't found")
# 2nd decision
dot_float=float(dot_str)
dot_float=dot_float*10
print('intermediade result is: ',dot_float)
dot_float_shl=int(dot_float//1)
print('integer result is: ',dot_float)
your_digit=dot_float_shl-(dot_float_shl//10)*10
print('VASHA CYFRA :',your_digit)
input('4th ended')

#https://replit.com/join/kbhbjafnxp-ant29011982