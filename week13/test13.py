def addition_num(num1, num2):
    add_num = num1 + num2
    return add_num

def multiply_num(num1, num2):
    mul_num = num1 * num2
    return mul_num

def combine_num(addition_num, multiply_num):
    com_num = addition_num() + multiply_num()
    print(com_num)


add_num1 = addition_num(4, 5)
multiply_num1 = (4, 5)
combine_num(add_num1, multiply_num1)
    
    