RUS_LITERALS = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

monoTable = {'а': 0.077058541718083, 'б': 0.0166554208228423, 'в': 0.04241208516880443, 'г': 0.01843981748279512,
             'д': 0.028449354884115208, 'е': 0.07711976792113055, 'ё': 6.311979695623715e-06, 'ж': 0.009743171858164767,
             'з': 0.01591376320860651, 'и': 0.062005101341990006, 'й': 0.01084334991911198, 'к': 0.032365938285249723,
             'л': 0.04749764720956846, 'м': 0.0279513396861305, 'н': 0.06151718531151829, 'о': 0.10705938121138252,
             'п': 0.024285973076881805, 'р': 0.04162687489466884, 'с': 0.04921324329083898, 'т': 0.05431521647881163,
             'у': 0.026014824315513142, 'ф': 0.0018430980711221247, 'х': 0.00809132677182004, 'ц': 0.00334029965492407,
             'ч': 0.013618727391277728, 'ш': 0.008659404944426175, 'щ': 0.0026649178274923326,
             'ъ': 0.00041343467006335334, 'ы': 0.018099601777201005, 'ь': 0.018578681036098842,
             'э': 0.0029843040000908927, 'ю': 0.0059540904468818505, 'я': 0.020990488477796665}


class Decrypt:

    def __init__(self):
        self.frequency_table = monoTable
        self.decode_table = dict()
        self.bi_decode_table = dict()

    def create_decrypt_table(self, filename):
        table = dict()
        f = open(filename, 'r', encoding="utf-8")
        text = f.read()
        text = text.lower().replace(" ", "")
        for letter in RUS_LITERALS:
            table[letter] = text.count(letter) / len(text)

        for k, v in table.items():
            self.decode_table[k] = list(self.frequency_table.keys())[list(self.frequency_table.values()).index(v)]
        f.close()

    def decrypt_with_mono(self, filename):

        f = open(filename, 'r', encoding="utf-8")
        f1 = open(filename[:-4] + "_Decrypted_mono" + '.txt', 'w', encoding="utf-8")

        for line in f:
            line = line.lower()
            for letter in line:
                if letter not in self.decode_table.keys():
                    f1.write(letter)
                else:
                    f1.write(self.decode_table.get(letter))
        f.close()
        f1.close()

    def create_bi_table(self, filename):
        table = dict()
        f = open(filename, 'r', encoding="utf-8")
        text = f.read()
        text = text.lower()

        for i in range(len(text) - 1):
            l = text[i] + text[i + 1]
            if text[i] in RUS_LITERALS and text[i + 1] in RUS_LITERALS:
                if l in table.keys():
                    table[l] += 1
                else:
                    table[l] = 1
        f.close()

        sum = 0
        for k, v in table.items():
            sum += v

        for k, v in table.items():
            table[k] = v / sum

        self.bitable = table

    def decrypt_with_bigram(self, filename):

        table = dict()
        f = open(filename, 'r', encoding="utf-8")
        f1 = open(filename[:-4] + "_Decrypted_bi" + '.txt', 'w', encoding="utf-8")

        text = f.read()
        text = text.lower()


        for i in range(len(text) - 1):
            l = text[i] + text[i + 1]
            if text[i] in RUS_LITERALS and text[i + 1] in RUS_LITERALS:
                if l in table.keys():
                    table[l] += 1
                else:
                    table[l] = 1

        sum = 0
        for k, v in table.items():
            sum += v

        for k, v in table.items():
            table[k] = v / sum

        i = 0

        for k, v in table.items():
            self.bi_decode_table[k] = list(self.bitable.keys())[list(self.bitable.values()).index(v)]

        while i < len(text) - 1:
            l = text[i] + text[i + 1]
            if text[i] in RUS_LITERALS and text[i + 1] in RUS_LITERALS:
                f1.write(self.bi_decode_table[l])
                i += 2
            elif text[i] in RUS_LITERALS and text[i + 1] not in RUS_LITERALS:
                f1.write(self.decode_table.get(text[i]))
                i += 1
            else:
                f1.write(text[i])
                i += 1
        f.close()
        f1.close()
