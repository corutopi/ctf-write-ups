## simple_RSA
### 解法
- 公開鍵nを素因数分解することは(時間内では)できない。
- 暗号化されているflagのbit数と公開乗数eに着目すると、
    - (2 ** 375) ** 3 = 2 ** 1125
    - 1125 < 2046（公開鍵のbit桁数）
- となり、暗号化後の c の値は単純に暗号化前の flag をe乗した値のままであることがわかる。
- よって c のe乗根がflagとなる。
- c も巨大数なため素因数分解はできないが、x ** 3 = c となる値xを 0 ～ 2**376 の間で2分探索すれば高速に求められる。

### flag
```
ctf4b{0,1,10,11...It's_so_annoying.___I'm_done}
```

### その他
- solver の実行には Crypto モジュールのインストールが必要。
- windows の場合
    ```
    $ pip install pycryptodome
    ```
- linux の場合
    ```
    $ pip install pycrypto
    ```
