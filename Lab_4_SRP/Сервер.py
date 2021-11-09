import random
from Lab_4_SRP.Хэш_функция import hash_it


class Сервер:

    def __init__(self, K, N, g):
        self.имя_пользователя, self.соль, self.верификатор, self.K, self.N = 0, 0, 0, K, N
        self.скремблер = None
        self.A = None
        self.Хэш = hash_it
        self.g = g
        self.ключ_сессии = None

    def зарегать(self, список):
        self.имя_пользователя, self.соль, self.верификатор = список

    def проверить_А(self, список, клиент):
        i, self.A = список
        if self.A == 0:
            raise Exception("A = 0")

        self.b = random.randint(0, 10000000000000000)

        self.B = (self.K * self.верификатор + pow(self.g(self.N), self.b, self.N)) % self.N

        клиент.проверить_B([self.соль, self.B])

    def вычислить_скремблер(self):
        self.скремблер = self.Хэш(self.A.__str__() + self.B.__str__())
        if self.скремблер == 0:
            raise Exception("скремблер = 0")

    def вычислить_ключ_сессии(self):
        S = pow(self.A * pow(self.верификатор, int(self.скремблер, 16), self.N), self.b, self.N)
        self.ключ_сессии = self.Хэш(S.__str__())

    def проверить_М(self, M_клиента):
        M = self.Хэш(
            (int(self.Хэш(self.N.__str__()), 16) ^
             int(self.Хэш(self.g(self.N).__str__()), 16)
             ).__str__() +
                     self.Хэш(self.имя_пользователя) + self.соль + self.A.__str__() + self.B.__str__() + self.ключ_сессии)

        if M == M_клиента:
            print(f"OK  M1 сгенерировалось и значение одинаковое как на сервере так и на клиенте {M=}")
        else:
            raise Exception("NOT OK MMMMMMMM")
