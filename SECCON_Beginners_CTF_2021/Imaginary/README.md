## Imaginary
### 解法
- TCP接続後、対話モードとなる。コマンドは以下の通り。
    - 1: 数字を二つ(A, Bとする)入力し、 "A + Bi": (A, B) の形で変数に辞書登録する
    - 2: 変数に登録されている情報を出力する
    - 3: AES暗号化されたjson形式情報を入力し、変数情報を上書きする
    - 4: 変数に登録されている情報をjson形式にした後、AES暗号化してExportする
    - 5: 変数の辞書keyに"1337i"が含まれる場合はflagを出力する
- コマンド1では"1337i"を直接辞書登録することができないので、コマンド3で登録することを考える。
- AES暗号化方式では固定長(今回の場合16byte)毎に暗号化を行うため、16文字毎に暗号化が行われる。
- これを利用し、以下①, ②のような辞書型をそれぞれコマンド1で作り、コマンド4で出力する
    - ① {"A + B": (A, B), "... }  -> 3つ目の'"'が16x文字目になるようにする
    - ② {... 1337i": (C, 1773)}   -> 1つめの'1'が16x + 1文字目になるようにする
- あとは出力結果の①[1 ～ 16x文字目]と②[16x+1 ～ 末文字目]を連結することで以下の形式のデータがAES暗号化されたハッシュ値を得ることができる。
    - {"A + B": (A, B), "1337i": (C, 1773)}
- これをコマンド3で登録し、コマンド5を実行するとflagが表示される。

### 例
- ①として、以下の登録状態になるようにコマンド1を実行。コマンド4で暗号化後のハッシュ値を取得。
    - {"1000 + 1i": (1000, 1), "100 + 1337i": (100, 1337)}
- ②として、以下の登録状態になるようにコマンド1を実行。コマンド4で暗号化後のハッシュ値を取得。
    - {"1000000 + 1i": (1000000, 1), "1 + 1337i": (1, 1337)}
- ①のハッシュ値の先頭 ～ 64文字目と②の65文字目 ～ 末尾を連結し、コマンド3に入力。
    - ※ハッシュ化前の16文字ごとに32文字のハッシュ値となる(16進数表記になるため)
- コマンド5 を実行

### flag
```
ctf4b{yeah_you_are_a_member_of_imaginary_number_club}
```