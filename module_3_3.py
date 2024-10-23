def print_params (a = 1, b = 'Rustam', c = True):
    print(a, b, c)
print_params()
print_params(66)
print_params(b=25)
print_params(c=[1, 2, 3])
# 2
values_list = (25,'String', True)
values_dict = {'a': 2, 'b': 'String','c': True}
print_params(*values_list)
print_params(**values_dict)
# 3
values_list_2 = (5.5, 'String')
print_params(*values_list_2, 42)