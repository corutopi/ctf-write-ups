## pwn_monster_1
### 解法
- やたら強い敵モンスターとのバトルを強いられ、勝つとflagがもらえる。
- モンスターにはname, HP, ATK の要素があるが、入力で指定できるのはnameのみ。そのまま戦うと負ける。
- ので、入力時に脆弱性をついてHP, ATKを書き換える方法を考える。
- name の読み込みは scanf で行っているので、この辺に使える脆弱性がないか検索してみる。
    - https://book.mynavi.jp/manatee/detail/id=64350
- メモリサイズより大きい入力を与えるとバッファオーバーフローを起こすらしいので試しにやたら長い文字列を入れてみたら勝てた。

### 入力
```
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

### flag
```
nitic_ctf{We1c0me_t0_pwn_w0r1d!}
```
