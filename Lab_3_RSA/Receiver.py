import Lab_2_Diffie_Hellman.Negotiator as Negotiator
import math
from Lab_3_RSA.Sender import Отправитель


class Принимающий:

    def __init__(self):
        простое_число_1, простое_число_2 = Negotiator.generate_prime_number(100, 1000),\
               Negotiator.generate_prime_number(2000, 3000)  # два простых числа

        модуль = простое_число_1 * простое_число_2  # module

        значение_функции_эйлера_для_двух_простых_чисел = (простое_число_1 - 1) * (простое_число_2 - 1)  # функция эйлера

        while 1:
            открытая_экспонента = Negotiator.generate_prime_number(3, значение_функции_эйлера_для_двух_простых_чисел - 1)
            if math.gcd(значение_функции_эйлера_для_двух_простых_чисел, открытая_экспонента) == 1:
                break

        self.открытый_ключ = [открытая_экспонента, модуль]

        #  алгоритм поиска числа, обратного числу е по модулю ф
        d = 1
        while (d * открытая_экспонента) % значение_функции_эйлера_для_двух_простых_чисел != 1:
            d += 1

        self.закрытый_ключ = [d, модуль]
        self.отправитель = Отправитель(self.открытый_ключ, self)

    def принять(self, сообщение_отправителя):
        декодированное_сообщение = ""
        for символ in сообщение_отправителя:
            декодированное_сообщение += chr(pow(символ, self.закрытый_ключ[0], self.закрытый_ключ[1]))

        print(f"{декодированное_сообщение=}")
