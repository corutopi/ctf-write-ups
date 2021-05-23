## check_url
### 解法
- 問題サーバーはGETパラメータのurlに指定したサイトにアクセスする作りになっている。
- ソースを見ると、localhostから自サーバーにアクセスするとAdminからのアクセスとしてflagが得られるのがわかるので、urlにはlocalhostへアクセスするパスを指定する
- しかし、https://localhost/ はソース内で落とされてしまい、https://127.0.0.1/ は'.'が化けてしまうので時サーバーへのアクセスにできない
- そこで、localhost, 127.0.0.1 以外で自サーバーを表す方法がないか調べてみる。
    - https://qiita.com/naka_kyon/items/88478be20b300e757fc0
- 以下の指定でアクセスしてみると無事flagが表示された。
    - https://check-url.quals.beginners.seccon.jp/?url=http://0x7F000001/

### flag
```
ctf4b{5555rf_15_53rv3r_51d3_5up3r_54n171z3d_r3qu357_f0r63ry}
```