def print_params (a = 1, b = 'string', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c =[1, 2, 3])


value_list = [1, 'two', False]
value_dict = {'a':2, 'b':'three', 'c':4}

print_params(*value_list)
print_params(**value_dict)

value_list_2 = [1, 'four']
print_params(*value_list_2, 42)