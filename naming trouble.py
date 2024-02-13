# числа

# int - целое число
# double - вещественное число
# float - вещественное число (разрядность меньше по сравнению с double)

first_number = 10
second_number = 5

sum = first_number + second_number

sub = second_number - first_number
mul = first_number * second_number
div = second_number/second_number

#print('sum = ' + str(sum))
#print('sub = ' + str(sub))
#print('mul = ' + str(mul))
#print('div = ' + str(div))


# булевые переменные (boolean)

first_boolean = True
second_boolean = False

var1 = 10.0
var2 = 10

#print('5'. > 5)
#print(var1 == var2)
#print('10' < 77)

first_number = 6
second_number = 6

# if (first_number > second_number):
#     print('first_number > second_number')
# elif (first_number == second_number):
#     print('first_number == second_number')
# else:
#     print('first_number < second_number')

# list (список), set (множество), tuple (кортеж), dictionary (словарь)
    
some_list = [123, 666, True, 'some_str']

some_list.append(False)
print(type(some_list))

# some_list.append(7)
# some_list.clear()

# print(some_list)

some_set = { 1, 2, 4, True }

some_set.add(False)
some_set.add('False')

print(some_set)
print(type(some_set))

some_tuple = (1,2,3,True,False)


print(some_tuple[0])

some_dict = {'Иванов Иван Иванович': 'инженер', 'Петров Петр Петрович': 'зав. гл. инженера'}

var1 = some_dict.get('Иванов Иван Иванович')

print(var1)

some_dict[7] = 'директор'
some_dict[True] = 'директор'

print(some_dict)
