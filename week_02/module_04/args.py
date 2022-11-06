from unittest import result


def add(num1,num2):
    result = num1+num2
    print(f"num1 = {num1} and num2 = {num2}")
    return result

#total = add(12,14)
# total = add(num2=14,num1=12)

def multiply(sum1,sum4,sum2=2,sum3=1):
    multi = sum1*sum2
    return multi

result_of_multi = multiply(45,3)
# print(result_of_multi)

def multiply2(*number):
    result = 1
    for num in number:
        result*=num
    return result
    
final_result = multiply2(12,2,3)
print(final_result)
