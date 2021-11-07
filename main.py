from Lab_1_Caesar.Encrypt import *
from Lab_1_Caesar.Decrypt import *
from Lab_2_Diffie_Hellman.Negotiator import *
from Lab_2_Diffie_Hellman.bum_in_the_middle import *
import Lab_3_RSA.Sender
import Lab_3_RSA.Receiver as Приёмник
from Lab_4_SRP.Хэш_функция import hash_it


def lab_1():
    encryptor = Caesar(3, "лодка")
    encryptor.encrypt("Lab_1_Caesar/text.txt")

    decrypter = Decrypt()

    decrypter.create_decrypt_table("Lab_1_Caesar/text_Encrypted.txt")
    decrypter.decrypt_with_mono("Lab_1_Caesar/text_Encrypted.txt")

    decrypter.create_bi_table("Lab_1_Caesar/text.txt")
    decrypter.decrypt_with_bigram("Lab_1_Caesar/text_Encrypted.txt")


def lab_2():
    g = 7
    p = 5
    alice = Negotiator(g, p, "Alice")
    bob = Negotiator(g, p, "Bob")
    eve = Intruder(g, p)

    bob.set_alien_mod(alice.uniq1)
    alice.set_alien_mod(bob.uniq1)
    eve.on_exchange(alice.uniq1, bob.uniq1)


def lab_3():
    Приёмник.Принимающий().отправитель.отправить()

def lab_4():

    s = "qwezxczxczxczxczxvgfdshsdfns"
    b = ""
    for i in s:
        b += i
        hash_it(b)


if __name__ == '__main__':
    while 1:
        a = input("\n1. для лабораторной 1"\
              "\n2. для лабораторной 2"\
              "\n3. для лабораторной 3"\
              "\n4. для лабораторной 4"\
              "\n0. Выход\n"
                  )

        if a == "1":
            lab_1()
        elif a == "2":
            lab_2()
        elif a == "3":
            lab_3()
        elif a == "4":
            lab_4()
        elif a == "0":
            exit()

