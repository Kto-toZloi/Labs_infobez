class Intruder:

    def __init__(self, g, p):
        self.g = g
        self.p = p
        self.uniq_alice = None
        self.uniq_bob = None
        self.name = "Eve"
        print(f"{self.name}: p = {self.p}, g = {self.g}")

    def on_exchange(self, uniq_alice, uniq_bob):
        self.uniq_alice = uniq_alice
        self.uniq_bob = uniq_bob
        self.log()

    def log(self):
        print(f"{self.name}: p = {self.p}, g = {self.g}"
              f", uniq_alice_mod = {self.g}^a mod {self.p} = {self.uniq_alice}"
              f", uniq_bob_mod = {self.g}^b mod {self.p} =  {self.uniq_bob}"
              f", K = {self.uniq_alice}^b mod {self.p} = {self.uniq_bob}^a mod {self.p}")
