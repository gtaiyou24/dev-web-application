# staticファイルの公開方法
Djangoアプリケーションを本番環境に公開する際には、各種設定が必要だが今回はstaticファイルの設定方法について説明する

### staticファイルとは
staticファイルとは、静的なファイルと呼ばれるCSS, JS, IMAGEなどのファイルの総称。これらのファイル群はアプリケーションのページを表示(レンダリング)する際にcssを効かせたり、JSで動的な動きをページ内で実行するために必要となる。

### 本番公開する際に公開する際にどのような問題が起こる？
静的なファイル群は、ページの読み込み高速化、メンテナンス性の向上のため一か所にまとめる必要がある。adminページの静的ファイル群と開発したdjangoアプリケーションのcssファイル群は別々に管理されているため、一か所にまとめて公開しなければいけない。

### ステップ
 1. settingsファイルで`STATIC_ROOT`を設定します。このとき、`STATICFILES_DIRS`の値を同じだとエラーが発生するため、一時的に`STATICFILES_DIRS`の値をコメントアウトするなどして対応。2.が終了したらコメントを外す。
 2. `python manage.py collectstatic`

### 参考文献
 - [Django での static files の扱い方まとめ - AWS / PHP / Python ちょいメモ](http://hideharaaws.hatenablog.com/entry/2014/12/12/230825)のWSGIでハンドル時（本番）
 - [Python Django チュートリアル(6) - Qiita](http://qiita.com/maisuto/items/86add9263a641899b1e3#djangoの設定変更)のdjangoの設定変更
 - [How to use Django with Apache and mod_wsgi¶](https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/modwsgi/#serving-files)のserving-files
