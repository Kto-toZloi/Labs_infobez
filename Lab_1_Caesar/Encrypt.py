import copy

RUS_LITERALS = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


class Caesar:

    def __init__(self, shift, keyword):
        self.shift = shift
        self.keyword = keyword
        self.alphabet = copy.copy(RUS_LITERALS)
        self.table = self.generate_algorithm_table()

    def generate_algorithm_table(self):
        for let in self.keyword:
            self.alphabet.remove(let)

        self.alphabet = list(self.keyword) + self.alphabet

        for i in range(self.shift):
            tmp = self.alphabet[-1]
            for j in range(len(self.alphabet) - 1):
                self.alphabet[-1 - j] = self.alphabet[-2 - j]
            self.alphabet[0] = tmp

        return dict(zip(RUS_LITERALS, self.alphabet))

    def encrypt(self, text):
        f = open(text, 'r', encoding="utf-8")
        f1 = open(text[:-4] + "_Encrypted" + '.txt', 'w', encoding="utf-8")

        for line in f:
            line = line.lower()
            for letter in line:
                if letter not in self.table.keys():
                    f1.write(letter)
                else:
                    f1.write(self.table.get(letter))

        f.close()
        f1.close()
