with open("flag.txt") as f:
    enc_flag = f.read()


def xor(c: str, n: int) -> str:
    temp = ord(c)
    for _ in range(n):
        temp ^= n
    return chr(temp)


flag = ""
for i in range(len(enc_flag)):
    flag += xor(enc_flag[i], i)

print(enc_flag)
print(flag)
