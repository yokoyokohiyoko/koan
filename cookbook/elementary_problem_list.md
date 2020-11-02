# Cook book 問題リスト

## 問題の出題方法

下記のフォーマットに従ってください

```
1. 問題
    + タグ: 
    + レベル:
```
+ ナンバリングは必ず `1. ` でお願いします。markdown の処理で incrementされます。
+ タグは `#` で始まる英単語でお願いします。複数可（スペース区切り）
+ レベルは以下のいずれかでお願いします. （主観でいいです）
    1. introduction
    1. elementary
    1. pre-intermediate
    1. intermediate

## 解答方法
+ このレポジトリにプルリクを出すという方法で提出してください。
+ プルリクに不慣れな人はまず[fintalk/study-git 他の人のリポジトリーの変更依頼を出そう](https://github.com/fintalk/study-git/blob/main/pullrequest.md)を読んで学んでください

1. Koan レポジトリを folk する
1. `cookbok/submit` ディレクトリのなかに自分の名前でディレクトリを作る.（例: `cookbok/submit/shinseitaro`) 
1. そのディレクトリの中に問題一つに対してファイル一つを作成して解答する。（ファイル名は任意。）
1. Koan に pull request を出す

--- 

## 問題

1. 1から10の整数をリストを`変数x`に格納して printしてください。ただし range 関数を使うこと。さらに全要素を2乗したリストを`変数y`に格納して printしてください。
    + タグ： #list 
    + レベル: introduction

1. AからG のアルファベットをリスト`変数x`に格納して printしてください. ただし list 関数を使い，引数は一つだけ渡すこと. また，同リストを全部大文字にした別のリストを`変数y`に格納して printしてください。
    + タグ： #list #string
    + レベル: introduction

1. 実行すると "HOGE!" をプリントする関数 hoge を定義してください。
    + タグ： #function 
    + レベル: introduction

1. 引数 name を引き取り、"Hello [name] さん!" と出力する関数 hello を定義してください。
    + タグ： #function 
    + レベル: introduction

1. 引数 name を引き取り、[name] が s で始まる名前であれば、"Hello Mr. [name] さん!", m で始める名前であれば、"Hello Miss. [name] さん!" ,  k で始める名前であれば、"Hello Ms. [name] さん!", それ以外であれば、"Hello [name] さん!" と出力する関数 hello を定義してください。
    + タグ： #function 
    + レベル: introduction

1.  `x = [1,2]` と `y = [3,4]` をつなげて一つのリスト [1,2,3,4]にしてください。ただし リストのメソッド関数を使うこと. x + y  ではダメです．
    + タグ： #list
    + レベル: introduction

1.  `x = [1,2]` と `y = [3,4]` を使って、[1,2,[3,4]] というリスト z を作成して下さい
    + タグ： #list
    + レベル: introduction

1. 0から50の整数リスト l を作成してください
    + タグ： #list
    + レベル: introduction

1. 0から50の整数リスト l を作成して、全部出しあわせてください。
    + タグ： #list
    + レベル: introduction

1.  `x = -500.123` の 絶対値、整数値、5乗、丸めた整数、を組み込み関数を使って取得し、タプルで返して下さい


