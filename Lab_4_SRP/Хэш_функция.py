def hash_it(data):
    """Функция для хэширования данных"""
    len_s = len(data)
    p = "".join(list(map(lambda y: bin(y)[2:], list(map(ord, list(data))))))
    x = int(p[7:] + '0' * 7, 2)
    p = int(p, 2)
    while (len_s := len_s - 1) >= 0:
        x = (1000003 * x) ^ p
        p += 1
    return hex(x ^ len(data))
