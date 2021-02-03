# Django2.1 + MySQL環境構築

## ゴール
Djangoの初期画面をDocker環境を用いて表示する

---
## 作業手順

<!-- MarkdownTOC -->

- 作業フォルダを作成する
- \(Django\)プロジェクトの作成
- \(Django\)`requirements.txt`を作成する
- \(Django\)環境変数を定義した`env`ファイルを作成する
- \(Django\)`settings.py`のデータベース設定値を変更
- \(Django\)`Dockerfile`を作成する
- \(Django\)`wait-for-it.sh`をダウンロード
- \(Django\)ディレクトリの確認
- \(MySQL\)MySQL用のディレクトリを作成
- \(MySQL\)`Dockerfile`&`charset.cnf`を作成
- \(Docker\)`docker-compose.yml`を作成
- \(Docker\)docker-composeの実行
- \(Django\)appサーバーに接続
- \(MySQL\)dbサーバーに接続
- 参考文献

<!-- /MarkdownTOC -->

### 作業フォルダを作成する
```bash
# At local.
$ mkdir /path/to/myproject
$ cd /path/to/myproject
$ tree
# .
# ├── app  # Djangoディレクトリ.
# └── db   # MySQLディレクトリ.
```

### (Django)プロジェクトの作成
```bash
# At local.
$ cd /path/to/myproject
$ python -m django --version
# 2.1.7
$ django-admin startproject app
```
djangoの`app`プロジェクトを作成したら、`myproject`ディレクトリは以下のようになっているはずです。
```bash
$ tree
.
├── README.md
└── app
    ├── app
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
```

### (Django)`requirements.txt`を作成する
```bash
# At local.
$ cd /path/to/myproject
$ cd app
$ vim requirements.txt
```
requirements.txtに記述するpythonパッケージは作るアプリケーションによって異なるが、今回は必要最低限のパッケージのみをインストールする。
```bash
# requirements.txt
Django==2.1.7
mysqlclient==1.4.2.post1
```

### (Django)環境変数を定義した`env`ファイルを作成する
```bash
# At local.
$ cd /path/to/myproject
$ cd app
$ vim env
```
```bash
DB_HOST=db
DB_NAME=app
DB_USERNAME=app_user
DB_PASSWORD=password_for_app_user
DB_PORT=3306
```

### (Django)`settings.py`のデータベース設定値を変更
```bash
# At local.
$ cd /path/to/myproject
$ vim app/app/settings.py
```
```python
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USERNAME'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
    }
}
```

### (Django)`Dockerfile`を作成する
```bash
# At local.
$ cd /path/to/myproject
$ cd app
$ vim Dockerfile
```
記述するDockerfileは以下のように記述する.
```bash
# Dockerfile
FROM python:3

# 作業用ディレクトリを作成する
RUN mkdir -p /home/app
# 作成した作業用ディレクトリに移動する
WORKDIR /home/app

# 環境変数に移動する
ENV PYTHONDONTWRITEBYTECODE 1
ENV DOCKER true

RUN apt-get update
# MySQLクライアントとVimエディタをインストール
RUN apt-get install -y mysql-client vim
# Dockerfileと同階層に存在するrequirements.txtをDockerイメージに追加する
ADD ./requirements.txt .
# 追加したrequirements.txtを用いてpip installを実行
RUN pip install --no-cache-dir -r requirements.txt
```

### (Django)`wait-for-it.sh`をダウンロード
`python manage.py runserver`をDockerで実行する際に、MySQLが接続できている状態でないとDjango側のDockerをビルドできずに失敗する。`wait-for-it.sh`でMySQLが接続可能の状態であることを確認してからDjango側のDockerをビルドすることができる。
```bash
# At local.
$ cd /path/to/myproject
$ cd app
$ vim wait-for-it.sh
```
`wait-for-it.sh`の内容は、[wait-for-it/wait-for-it.sh at master · vishnubob/wait-for-it](https://github.com/vishnubob/wait-for-it/blob/master/wait-for-it.sh)からコピーしてくる。

### (Django)ディレクトリの確認
ここまでの作業でディレクトリ構造および作成したファイルは以下のようになっているはずです。
```bash
# At local.
$ cd /path/to/myproject
$ cd app
$ tree
.
├── README.md
└── app            # ←「(Django)プロジェクトの作成」で作成
    ├── Dockerfile # ←「(Django)`Dockerfile`を作成する」で作成
    ├── app
    │   ├── __init__.py
    │   ├── settings.py # ←「(Django)`settings.py`のデータベース設定値を変更」で修正
    │   ├── urls.py
    │   └── wsgi.py
    ├── env        # ←「(Django)環境変数を定義した`env`ファイルを作成する」で作成
    ├── manage.py
    ├── requirements.txt # ←「(Django)`requirements.txt`を作成する」で作成
    └── wait-for-it.sh   # ←「(Django)`wait-for-it.sh`をダウンロード」で作成
```
ここまでできたら次はMySQLの設定を行います。


### (MySQL)MySQL用のディレクトリを作成
```bash
# At local.
$ cd /path/to/myproject
$ mkdir db
$ ls
# README.md app       db
```

### (MySQL)`Dockerfile`&`charset.cnf`を作成
Dockerfileを作成する際に、「(Django)環境変数を定義した`env`ファイルを作成する」で作成した`env`ファイルの中身の値と同一になるように注意すること。
```bash
# At local.
$ cd /path/to/myproject
$ cd db
$ vim Dockerfile
```
```bash
FROM mysql:5.7

ENV MYSQL_DATABASE "app"
ENV MYSQL_ROOT_PASSWORD "password_for_root_user"
ENV MYSQL_USER "app_user"
ENV MYSQL_PASSWORD "password_for_app_user"

COPY charset.cnf /etc/mysql/conf.d/
```

次に`charset.cnf`ファイルを作成します。
```bash
$ vim charset.cnf
```
```bash
[mysqld]

# Query log
general_log=1
general_log_file="/tmp/sql.log"
log_output=FILE

# Slow Query log
slow_query_log=1
slow_query_log_file="/tmp/slow_sql.log"
long_query_time = 1
log_queries_not_using_indexes
log_slow_admin_statements

# character
character-set-server=utf8
collation-server=utf8_general_ci

[client]
default-character-set=utf8
```

### (Docker)`docker-compose.yml`を作成
```bash
$ cd /path/to/myproject
$ vim docker-compose.yml
```
```bash
version: "3.3"

# サービス定義
services:
  # DBサービス
  db:
    build: ./db  # /path/to/myproject/dbフォルダにあるDockerfileを指定
    ports:
      - "3306:3306"  # app→dbで接続するために3306ポートを開放

  # appサービス
  app:
    build: ./app
    env_file: ./app/env
    links:
      - db:db
    command: sh -c "./wait-for-it.sh db:3306; python3 manage.py runserver 0.0.0.0:8000"
    volumes:
      - ./app:/home/app
    ports:
      - "8080:8000"
    depends_on:
      - db
```

### (Docker)docker-composeの実行
```bash
cd path/to/myproject
docker-compose up --build -d

# コンテナが起動しているかを確認
docker-compose ps
#        Name                      Command               State                  Ports
# -------------------------------------------------------------------------------------------------
# django21mysql_app_1   sh -c ./wait-for-it.sh db: ...   Exit 2
# django21mysql_db_1    docker-entrypoint.sh mysqld      Up       0.0.0.0:3306->3306/tcp, 33060/tcp
```
[http://localhost:8080/](http://localhost:8080/)にアクセスするとDjangoの初期画面が表示されたら成功！


### (Django)appサーバーに接続
```bash
docker container exec -it myproject_app_1 /bin/bash
```


### (MySQL)dbサーバーに接続
```bash
# At local.
$ docker container exec -it myproject_db_1 /bin/bash

# At Docker.
root@cef417055358:/# mysql -u app_user -p
Enter password:    # ←「password_for_app_user」
mysql>
```



## 参考文献

 - [Quickstart: Compose and Django | Docker Documentation](https://docs.docker.com/compose/django/#define-the-project-components)
 - [DockerでDjangoの開発環境を作成する（Quickstart: Compose and DjangoのMySQL版） - aoishiの備忘録](https://aoishi.hateblo.jp/entry/2017/11/05/153341)
 - [DockerでDjangoの開発環境を構築 - Qiita](https://qiita.com/fujimisakari/items/6fd1761eca87995083af)
 - [docker-composeでNginx + Django + MySQLのWeb三階層を構成する - ビビリフクロウの足跡](http://bbrfkr.hatenablog.jp/entry/2018/11/19/144114)
 - [Django2(Python3)+Mysqlの開発環境をDockerで構築 - Qiita](https://qiita.com/cortyuming/items/e587fc045ee7424466b0)