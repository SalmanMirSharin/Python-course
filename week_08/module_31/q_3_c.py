# #Main function:
# def make_upper(st):
#     return st.upper()

# def make_capital(st):
#     return st.capitalize()
 
# def make_lower(st):
#     return st.lower()
 
 
# #For UpperCase:
# stu = 'i love python'
# upper = make_upper(stu)
# print(upper)
 
# #For Capitalize:
# stc = 'i love python'
# capitalize = make_capital(stc)
# print(capitalize)
 
# #For LowerCase:
# stl ='I LOVE PYTHON'
# lower = make_lower(stl)
# print(lower)
 
 
# # For test:
# def test_script():
#     is_str_upper ='I LOVE PYTHON'
#     assert is_str_upper == make_upper(stu),'test fail'
#     is_str_capital ='I love python'
#     assert is_str_capital == make_capital(stc),'test fail'
#     is_str_lower = 'i love python'
#     assert is_str_lower == make_lower(stl),'test fail'
# test_script()



# Main Function:
def half_adder_sum(a,b):
       return a^b
def half_adder_carry(a,b):
        return a&b

try: 
    a = int(input('Enter 1 or 0: '))
    b = int(input('Enter 1 or 0: '))
    
    if (a==1 or a==0) and (b==1 or b==0):
        sum = half_adder_sum(a,b)
        carry = half_adder_carry(a,b)
        print('Sum: ',sum)
        print('Carry: ',carry)
    else:
        print('Please Enter 0 or 1!')
except:
    print('Give input again!')


# For Test:
def test_script():
    sm = True
    cr = False
    assert sm == half_adder_sum(a,b) ,'test fail'
    assert cr == half_adder_carry(a,b),'test fail'
test_script()