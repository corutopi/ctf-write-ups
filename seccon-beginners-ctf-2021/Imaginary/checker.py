
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import json

key = b'iiiiiiiiiiiiiiii'
cipher = AES.new(key, AES.MODE_ECB)
numbers = {"1000 + 1i": (1000, 1), "100 + 1337i": (100, 1337)}
# numbers = {"1000000 + 1i": (1000000, 1), "1 + 1337i": (1, 1337)}


# 暗号化
print(json.dumps(numbers).encode())
dump = pad(json.dumps(numbers).encode(), AES.block_size)
enc = cipher.encrypt(dump)
print(enc)
print(enc.hex().encode())
data = enc.hex().encode()


# 複合化
# data = b'ae42469f3aaf95a2d086557dbf20a6ea46d9fc8772ec0571274c76581c248c89' + \
#        b'0b056b0ad0038f987c64027585e6f1cfad3d52b97ec23d23c08b5fa799ff7efc'
# data = b'0b056b0ad0038f987c64027585e6f1cfad3d52b97ec23d23c08b5fa799ff7efc'
enc = bytes.fromhex(data.decode())
print(enc)
cipher = AES.new(key, AES.MODE_ECB)
plaintext = unpad(cipher.decrypt(enc), AES.block_size)
print(plaintext)
