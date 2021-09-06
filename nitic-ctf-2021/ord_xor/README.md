## ord_xor
### 解法
- flagの各文字について、i文字目を数値化し、i回iをxorした結果が暗号文になっている。
- xor は2回行うと基の数字に戻る(x xor i xor i = x)ので、偶数番目の文字はそのまま、奇数番目の文字は1回iでxorした結果になっている。
- よって奇数i番目の文字をiでxorした結果が平文となり、これはsample内の関数xorを暗号文に適用するとえられる。

## 暗号文 / 平文
nhtjcZcsfroydRx`rl / nitic_ctf{ord_xor}

## flag
```
nitic_ctf{ord_xor}
```
