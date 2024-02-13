import math

def calc_discr(x1, x2, x3):
    print('a = ' + str(x1) + ' b = ' + str(x2) + ' c = ' + str(x3))
    return math.pow(x2, 2) - 4 * x1 * x3

def print_result(discr, b, a):
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print('x1 = ' + str(x1) + '; x2 = ' + str(x2))
    elif discr == 0:
        x1 = (-b) / (2 * a)
        x1_other_variant = (-b + math.sqrt(discr)) / (2 * a)
        print('x1 = ' + str(x1) + ' (other varian value = ' + str(x1_other_variant) + ')')
    else:
        print('Discr < 0, no solutions')

print('ax^2 + bx + c = 0')

a = 2
b = 5
c = 10

#discr1 = b*b - 4 * a * c
#discr = math.pow(b, 2) - 4 * a * c
discr = calc_discr(a, b, c)

#print(discr1)
print(discr)

print_result(discr=discr, a=a, b=b)



    