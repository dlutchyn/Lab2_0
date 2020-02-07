def palindrom_check(num):
    '''
    (int) -> (bool)
    Returns True if number is palindrom and False otherwise.
    '''
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


def krapekar_check(num):
    '''
    (int) -> (bool)
    Returns True if number is krapekars's number and False otherwise.
    '''
    square = str(num**2)
    for i in range(1, len(square)):
        if int(square[:i]) + int(square[i:]) == num:
            return True
    else:
        return False


def var_1():
    '''
    Returns minimal number that is not a palindrom and is a product of two
    four-digit krapekar numbers.
    '''
    krap_list = [num for num in range(1000, 10000) if krapekar_check(num)]
    num_list = []
    for i in range(len(krap_list)-1):
        for j in range(i+1, len(krap_list)):
            if not palindrom_check(krap_list[i]*krap_list[j]):
                num_list.append(krap_list[i]*krap_list[j])
    return min(num_list)


def leyland(dig_num):
    '''
    (int) -> (list)
    Returns list of leyland numbers with certain number of digits (dig_num).
    '''
    leyland_list = []
    for x in range(1, 100):
        for y in range(x, 100):
            if len(str(x**y + y**x)) == dig_num:
                leyland_list.append(x**y + y**x)
    return leyland_list


def var_2():
    '''
    Returns maximal number that is not a palindrom and is a product of two
    five-digit leyland numbers.
    '''
    leyland_list = leyland(5)
    num_list = []
    for i in range(len(leyland_list)-1):
        for j in range(i+1, len(leyland_list)):
            if not palindrom_check(leyland_list[i]*leyland_list[j]):
                num_list.append(leyland_list[i]*leyland_list[j])
    return max(num_list)


def threemorph_check(num):
    '''
    (int) -> (bool)
    Returns True if number is threemorphic and False otherwise.
    '''
    qube = str(num**3)
    if qube[-len(str(num)):] == str(num):
        return True
    else:
        return False


def var_3():
    '''
    Returns maximal number that has its digits sorted and is a product of two
    five-digit threemorphic numbers.
    '''
    threemorph_list = [num for num in range(
        10000, 100000) if threemorph_check(num)]
    num_list = []
    for i in range(len(threemorph_list)-1):
        for j in range(i+1, len(threemorph_list)):
            num_list.append(threemorph_list[i]*threemorph_list[j])
    sorted_list = []
    for num in num_list:
        if list(str(num)) == sorted(list(str(num))):
            sorted_list.append(num)
    return max(sorted_list)


def automorphic_check(num):
    '''
    (int) -> (bool)
    Returns True if number is automorphic and False otherwise.
    '''
    square = str(num**2)
    if square[-len(str(num)):] == str(num):
        return True
    else:
        return False


def lishrel_check(num):
    '''
    (int) -> (bool)
    Returns True if number is lishrel's number and False otherwise.
    '''
    new_number = num + int(str(num)[::-1])
    if palindrom_check(new_number):
        return False
    else:
        return True


def var_4():
    '''
    Returns minimal lishrel's number and is a product of two
    six-digit automorphic numbers.
    '''
    automorphic_list = [num for num in range(
        100000, 1000000) if automorphic_check(num)]
    num_list = []
    for i in range(len(automorphic_list)-1):
        for j in range(i+1, len(automorphic_list)):
            if not lishrel_check(automorphic_list[i]*automorphic_list[j]):
                num_list.append(automorphic_list[i]*automorphic_list[j])
    return min(num_list)


def square_pairs(num):
    '''
    (int) -> list(tuples)
    Returns list of tuples with solutions x and y of the
    equation N = x^2 + y^2.
    '''
    x_y_list = []
    for x in range(1, int(num**(1/2))+1):
        for y in range(1, int((num - x**2)**(1/2))+1):
            if x**2 + y**2 == num:
                x_y_list.append((x, y))
    return x_y_list


def multiply_pairs(num):
    '''
    (int) -> list(tuples)
    Returns list of tuples with solutions x and y of the
    equation N = x*y.
    '''
    x_y_list = []
    for x in range(1, int(num**(1/2))):
        if (num/x) % 1 == 0:
            x_y_list.append((x, int(num/x)))
    return x_y_list


def taemp():
    print("hello")
    print("hi!")


if __name__ == "__main__":
    var = input("Введіть варіант: ")
    if var == '1':
        num = var_1()
        print('число:', num)
        print('пари x та y:', square_pairs(num))
    elif var == '2':
        num = var_2()
        print('число:', num)
        print('пари x та y:', multiply_pairs(num))
    elif var == '3':
        num = var_3()
        print('число:', num)
        print('пари x та y:', square_pairs(num))
    elif var == '4':
        num = var_4()
        print('число:', num)
        print('пари x та y:', multiply_pairs(num))
