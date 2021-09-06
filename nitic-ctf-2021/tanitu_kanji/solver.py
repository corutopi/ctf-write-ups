alphabets = "abcdefghijklmnopqrstuvwxyz0123456789{}_"
after1 = "fl38ztrx6q027k9e5su}dwp{o_bynhm14aicjgv"
after2 = "rho5b3k17pi_eytm2f94ujxsdvgcwl{}a086znq"

with open("./flag", "r") as file:
    enc_flag = file.read()


def reconv(s, table):
    res = ""
    for c in s:
        i = table.index(c)
        res += alphabets[i]
    return res


for i in range(2 ** 10):
    tmp_flag = enc_flag
    for j in range(10):
        if i >> j & 1:
            tmp_flag = reconv(tmp_flag, after1)
        else:
            tmp_flag = reconv(tmp_flag, after2)
    if i % 100000 == 0: print(i)
    if tmp_flag.startswith("nitic_ctf{"):
        print(tmp_flag)
