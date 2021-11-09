import random
import Lab_4_SRP.Хэш_функция as Хэш


def генератор(p):
    fact = []
    фи = p - 1
    n = фи

    i = 2
    while i * i <= n:
        if n % i == 0:
            fact.append(i)
            while n % i == 0:
                n //= i
        i += 1

    if n > 1:
        fact.append(n)

    for res in range(2, p + 1):
        ok = True
        i = 0
        while i < len(fact) and ok:
            ok = ok and pow(res, фи // fact[i], p) != 1
            i += 1
        if ok:
            return res
    return -1


class Клиент:

    def __init__(self):
        self.Хэш = Хэш.hash_it
        self.N = 359  # 2 * 179 + 1 (q = 179, простое число)
        self.A = None
        self.B = None
        self.g = генератор
        self.k = 3
        self.скремблер = None

        self.пароль = "qweqwe"
        self.username = "PAPA_KARLO"
        self.сервер = None

    def зарегать(self):
        self.соль = str(random.randbytes(500))
        x = self.Хэш(self.соль + self.пароль)
        v = pow(self.g(self.N), int(x, 16), self.N)

        self.сервер.зарегать([self.username, self.соль, v])  # отправить серверу


    def залогиниться(self):
        I = self.username
        self.a = random.randint(1, 10000000000000)
        self.A = pow(self.g(self.N), self.a, self.N)

        self.сервер.проверить_А([I, self.A], self)

    def проверить_B(self, список):
        self.B = список[1]
        if self.B == 0:
            raise Exception("B = 0")

    def вычислить_скремблер(self):
        self.скремблер = self.Хэш(self.A.__str__() + self.B.__str__())
        if self.скремблер == 0:
            raise Exception("скремблер = 0")

    def вычислить_ключ_сессии(self):
        x = self.Хэш(self.соль + self.пароль)
        S = pow(self.B - self.k *
                pow(self.g(self.N), int(x, 16), self.N),
                (self.a + int(self.скремблер, 16) * int(x, 16)), self.N)
        self.ключ_сессии = self.Хэш(S.__str__())

    def сгенерировать_подтверждение(self):
        M = self.Хэш((int(self.Хэш(self.N.__str__()), 16) ^ int(self.Хэш(self.g(self.N).__str__()), 16)).__str__() +
                      self.Хэш(self.username) + self.соль + self.A.__str__() + self.B.__str__() + self.ключ_сессии)

        self.сервер.проверить_М(M)