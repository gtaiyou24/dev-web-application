# Django2.1 + Nginx環境構築

## 環境

| 環境 | 詳細  |
|:----:|:-----|
| OS | CentOS7 |
| 言語 | Python3.6 |
| フレームワーク | Django2.1 |
| WSGI | uWSGI |
| データベース | MySQL |
| Webサーバ | Nginx |


## プロジェクトを作成

### Djangoのバージョンを確認
```bash
python -m django --version
# 2.1.7
```

### プロジェクトを作成
```bash
cd ~/path/to/hogehgoe

django-admin startproject myproject

# .
# ├── manage.py
# └── myproject
#     ├── __init__.py
#     ├── settings.py
#     ├── urls.py
#     └── wsgi.py

# 1 directory, 5 files
```

### 初期設定

 - データベースの変更


### 開発サーバー
```bash
python manage.py runserver
```
[http://localhost:80000/](http://localhost:80000/)にアクセスする

### アプリケーションの作成
```bash
python manage.py startapp myapp
```

## 参考資料

 - 「[DockerでDjangoの開発環境を構築 - Qiita](https://qiita.com/fujimisakari/items/6fd1761eca87995083af)」：https://qiita.com/fujimisakari/items/6fd1761eca87995083af
 - 「[docker-composeでNginx + Django + MySQLのWeb三階層を構成する - ビビリフクロウの足跡](http://bbrfkr.hatenablog.jp/entry/2018/11/19/144114)」：http://bbrfkr.hatenablog.jp/entry/2018/11/19/144114
 - 「[Docker-Composeで作るDjango開発環境(Django + MySQL + uWSGI + Nginx) - moto blog](https://nmmmk.hatenablog.com/entry/2018/05/01/101126)」：https://nmmmk.hatenablog.com/entry/2018/05/01/101126