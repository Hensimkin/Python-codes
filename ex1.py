#ex1
def factorSum(num):
    group = []
    d = int(2)
    while num != 1:
        if (num % d) == 0:
            num = num / d
            group.append(d)
        else:
            d += 1
    group1 = set(group)
    return sum(group1)


"""
Counts the sum of the prime number

:param group: array of all prime numbers
:param d: the prime number
:param group1: the group of all prime numbers without returns
:return: sum of prime numbers
"""


#ex2
def f(x):
    return x+1


"""
returns number +1
"""


def op(function):
    def abst(num):
        return function(abs(num))
    return abst


"""
function gets a function as a parameter and returns a function

:param: function
inside function returns a positive number after getting any number 
"""


#ex3
def interceptpoint(cordinate1, cordinate2):
    if cordinate1[0] == cordinate2[0]:
        return None
    im = (-1) * cordinate2[0]
    im2 = (-1) * cordinate1[1]
    m_point = cordinate1[0] + im
    n_point = cordinate2[1] + im2
    x = n_point / m_point
    y = cordinate1[0] * x + cordinate1[1]
    z = (x, y)
    return z


"""
function gets a the Coefficient of the parametrs

:param: im equals to the Coefficient of the m
:param: im2 equals to the Coefficient of n
:param: x equals to the x point
:param: y equals to the y point
:param: z equals to tuple
"""


#ex4
def printnumber(start, end, notprint):
    if start == end:
        return
    if start <= end:
        if start == notprint:
            start += 1
            if start == end and start != notprint:
                print(start)
            return printnumber(start, end, notprint)
        else:
            print(start)
            start += 1
            if start == end and start != notprint:
                print(start)
            return printnumber(start, end, notprint)
    else:
        if start == notprint:
            start -= 1
            if start == end and start != notprint:
                print(start)
            return printnumber(start, end, notprint)
        else:
            print(start)
            start -= 1
            if start == end and start != notprint:
                print(start)
            return printnumber(start, end, notprint)


"""
The function works as recursion every time it adds or decreses the start number until the end and returns the function with the new start
:param: start is the first number
:param: end is the end number 
:param: notprint is the the number which we dont print
"""


#ex5
def arrproduct(arr1, arr2):
    newarr = []
    n = 0
    for i in range(len(arr1)):
        for j in range(arr2[n]):
            newarr.append(arr1[n])
        n += 1
    return newarr


""""
The function chains to the array the numbers in the first array by the times of the second array

:param: n saves the position of the number of the second array
"""


#ex6
def analyze(string):
    weather = list(string.split(","))
    count = 0
    for i in range(len(weather)):
        if float(weather[i]) >= 75:
            count += 1
    return count


""""
The function changes the string into list with numbers

:param: count =counts the numbers above 75
"""