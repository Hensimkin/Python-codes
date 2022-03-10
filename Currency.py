ds = float(input("enter dollar shekel currency"))
es = float(input("enter euro shekel currency"))
sd = float(input("enter shekel dollar currency"))
se = float(input("enter euro shekel currency"))
ed = float(input("enter euro dollar currency"))
de = float(input("enter dollar euro currency"))

curr_dic = {('Dollar', 'Shekel'): ds, ('Euro', 'Shekel'): es, ('Shekel', 'Dollar'): sd, ('Shekel', 'Euro'): se
            ,('Euro', 'Dollar'): ed, ('Dollar', 'Euro'): de}


class Shekel:
    def __init__(self, amount1):
        self.__amount = amount1

    def get_amount(self):
        return self.__amount

    def __add__(self, money):
        if isinstance(money, Dollar):
            return self.get_amount()+money.get_amount()

        if isinstance(money, Euro):
            return self.get_amount()+money.get_amount()

        if isinstance(money, Shekel):
            return self.get_amount()+money.get_amount()

    def __sub__(self, money):
        if isinstance(money, Dollar):
            return self.get_amount()-money.get_amount()

        if isinstance(money, Euro):
            return self.get_amount()-money.get_amount()

        if isinstance(money, Shekel):
            return self.get_amount()-money.get_amount()

    def __repr__(self):
        return repr(f'{self.__amount}' + f'₪\n')

    def __str__(self):
        return f'{self.__amount}₪\n'


class Dollar:
    def __init__(self, amount1):
        self.__amount = amount1

    def get_amount(self):
        return self.__amount*curr_dic.get(('Dollar', 'Shekel'))

    def __add__(self, money):
        if isinstance(money, Dollar):
            return self.get_amount() + money.get_amount()

        if isinstance(money, Euro):
            return self.get_amount() + money.get_amount()

        if isinstance(money, Shekel):
            return self.get_amount() + money.get_amount()

    def __sub__(self, money):
        if isinstance(money, Dollar):
            return self.get_amount()-money.get_amount()

        if isinstance(money, Euro):
            return self.get_amount()-money.get_amount()

        if isinstance(money, Shekel):
            return self.get_amount()-money.get_amount()

    def __repr__(self):
        return repr(f'{self.__amount}' + f'$\n')

    def __str__(self):
        return f'{self.__amount}$\n'


class Euro:
    def __init__(self, amount1):
        self.__amount = amount1

    def get_amount(self):
        return self.__amount*curr_dic.get(('Euro', 'Shekel'))

    def __add__(self, money):
        if isinstance(money, Dollar):
            return self.get_amount() + money.get_amount()

        if isinstance(money, Euro):
            return self.get_amount() + money.get_amount()

        if isinstance(money, Shekel):
            return self.get_amount() + money.get_amount()

    def __sub__(self, money):
        if isinstance(money, Dollar):
            return self.get_amount()-money.get_amount()

        if isinstance(money, Euro):
            return self.get_amount()-money.get_amount()

        if isinstance(money, Shekel):
            return self.get_amount()-money.get_amount()

    def __repr__(self):
        return repr(f'{self.__amount}' + f'€\n')

    def __str__(self):
        return f'{self.__amount}€\n'


tags = {Shekel: 'Shekel', Dollar: 'Dollar', Euro: 'Euro'}


def tag_type(x):
    return tags[type(x)]


def add_das(a, b):
    if type(a) == Shekel:
        return a + b
    if type(a) == Dollar:
        return (a + b) * curr_dic.get(('Shekel', 'Dollar'))
    if type(a) == Euro:
        return (a + b) * curr_dic.get(('Shekel', 'Euro'))


def sub_das(a, b):
    if type(a) == Shekel:
        return a - b
    if type(a) == Dollar:
        return (a - b) * curr_dic.get(('Shekel', 'Dollar'))
    if type(a) == Euro:
        return (a - b) * curr_dic.get(('Shekel', 'Euro'))


def exchange(x):
    if type(x) == Dollar:
        return x.get_amount()
    if type(x) == Euro:
        return x.get_amount()
    if type(x) == Shekel:
        return x.get_amount()


def add1(a, b):
    return a+b


implementations = {'add': {('Dollar', 'Shekel'): add_das, ('Euro', 'Shekel'): add_das, ('Shekel', 'Dollar'): add_das,
                           ('Shekel', 'Euro'): add_das, ('Euro', 'Dollar'): add_das, ('Dollar', 'Euro'): add_das,
                           ('Dollar', 'Dollar'): add_das,('Shekel', 'Shekel'): add_das, ('Euro', 'Euro'): add_das},
                   'sub': {('Dollar', 'Shekel'): sub_das, ('Euro', 'Shekel'): sub_das, ('Shekel', 'Dollar'): sub_das,
                           ('Shekel', 'Euro'): sub_das, ('Euro', 'Dollar'): sub_das, ('Dollar', 'Euro'): sub_das,
                           ('Dollar', 'Dollar'): sub_das, ('Shekel', 'Shekel'): sub_das, ('Euro', 'Euro'): sub_das}}

ceorcions = {('Dollar', 'Shekel'): exchange, ('Euro', 'Shekel'): exchange, ('Shekel', 'Dollar'): exchange,
             ('Shekel', 'Euro'): exchange, ('Euro', 'Dollar'): exchange, ('Dollar', 'Euro'): exchange,
             ('Dollar', 'Dollar'):exchange,('Euro', 'Euro'):exchange}


def apply(operator_name, c, e):
    tags1 = (tag_type(c), tag_type(e))
    return implementations.get(operator_name)[tags1](c, e)


def coerce_apply(operator_name, c, e):
    tags1 = (tag_type(c), tag_type(e))
    if tags1 in ceorcions:
        return apply(operator_name, Shekel(ceorcions[tags1](c)), Shekel(ceorcions[tags1](e)))
    else:
        return apply(operator_name, c, e)


s = Shekel(50)
d = Dollar(50)
e = Euro(50)
print(d.get_amount())
print(e.get_amount())
print(d+s)
print(add1(e, d))
z = eval(repr(d))
print(z)
print(s)
print(e)
print(apply('add',Shekel(50),Dollar(20)))
print(curr_dic[('Euro', 'Dollar')])
print(apply('add',Dollar(50),Euro(20)))
print(apply('sub',Dollar(50),Euro(20)))
print(ceorcions[('Dollar', 'Shekel')](Dollar(50)))
print(coerce_apply('add',Dollar(50),Euro(20)))
print(coerce_apply('sub',Dollar(50),Euro(20)))



