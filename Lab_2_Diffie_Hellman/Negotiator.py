import random


def miller_rabin(number):
    if number % 2 == 0:
        return False
    source_number = number
    number -= 1
    s = 0
    while number % 2 == 0:
        number //= 2
        s += 1
    d = number
    # print(f'd is {d}, s is {s}')
    for i in range(5):
        flag = False
        a = random.randint(1, source_number - 1)
        # print(f'a is {a}')
        x = a ** d % source_number
        if x == 1 or x == source_number - 1:
            continue
        for j in range(s):
            x = x ** 2 % source_number
            if x == 1:
                return False
            if x == source_number - 1:
                flag = True
                break
        if not flag:
            return False
    return True


def generate_prime_number(left_border, right_border):
    while True:
        number = random.randint(left_border, right_border)
        if miller_rabin(number):
            return number


class Negotiator:

    def __init__(self, g, p, name):
        self.g = g
        self.p = p
        self.uniq = generate_prime_number(1, 1000)
        self.uniq1 = (self.g ** self.uniq) % self.p
        self.k = 0
        self.name = name
        self.log(1)

    def set_alien_mod(self, num):
        self.k = (num ** self.uniq) % self.p
        self.log(2)

    def log(self, step):
        match step:
            case 1:
                print(f"{self.name}: p = {self.p}, g = {self.g}, uniq = {self.uniq}, uniq1 = {self.uniq1}")
            case 2:
                print(f"K = {self.k}")
