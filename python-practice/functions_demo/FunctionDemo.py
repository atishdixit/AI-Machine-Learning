def mul_div(value1, value2):
    return (value1 * value2), (value1 / value2)


mul, div = mul_div(10, 5)
print(mul)
print(div)


def sum(num1, num2):
    return num1 + num2


sum_of_numbers = sum

print(sum_of_numbers(10, 12))


def test(func, num1, num2):
    return func(num1, num2)


print(test(sum_of_numbers, 10, 12))


def fuc_return_func_mul_by_value(num):
    def mult(value):
        return num * value

    return mult


generated_fun = fuc_return_func_mul_by_value(10)

print(generated_fun(20))

list_of_functions = [generated_fun, sum_of_numbers, sum, mul_div]

x, y = list_of_functions[3](12, 4)
print(x)
print(y)

ss = list_of_functions[2](12, 4)
print(ss)


def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def change_list(list, func):
    odd_list = []
    for i in list:
        if func(i):
            odd_list.append(i)
    return odd_list

a_list = range(1,20)

print(change_list(a_list, is_it_odd))

