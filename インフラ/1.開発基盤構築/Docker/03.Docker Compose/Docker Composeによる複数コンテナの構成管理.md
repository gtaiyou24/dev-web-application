# Docker Composeによる複数コンテナの構成管理
複数コンテナの一括管理ができる「DockerCompose」の構成管理ファイルである「dockercompose.yml」の書き方について説明します。

<!-- MarkdownTOC -->

- docker-compose.ymlの概要
- 文法
    - イメージの指定\(`image`\)
    - イメージのビルド\(`build`\)
    - コンテナ内で動かすコマンドの指定\(`command`/`entrypoint`\)
    - コンテナ間の連携\(`links`\)
    - コンテナ間の通信\(`ports`/`expose`\)
    - サービスの依存関係の定義\(`depends_on`\)
    - コンテナの環境変数の指定\(`environment`/`env_file`\)
    - コンテナ名の設定\(`container_name`\)
    - コンテナのラベル設定\(`labels`\)
    - コンテナのデータ管理\(`volumes`/`volumes_from`\)
    - コンテナを自動起動\(`restart`\)

<!-- /MarkdownTOC -->


## docker-compose.ymlの概要

 - Compose定義ファイル(`docker-compose.yml` or `docker-compose.yaml`)に、システム内で稼働する複数のサーバ群の構成をまとめて定義
 - Compose定義ファイルに、システム内で稼働する複数のサーバ群の構成をまとめて定義
    - Compose定義ファイルには管理したいコンテナのサービス(`services:`) / ネットワーク(`networks:`) / ボリューム(`volumes:`)を定義します

ex) Compose定義ファイルの例
```yaml
# バージョンを指定
version: "3"

# サービス定義
services:
    webserver:
        image: ubuntu
        ports:
            - "80:80"
        networks:
            - webnet
    redis:
        image: redis
        networks:
            - webnet

# ネットワーク定義
networks:
    webnet:

# データボリューム定義
volumes:
    data-volume:
```

---
## 文法

### イメージの指定(`image`)
> Dockerコンテナのもとになる、ベースイメージを指定するには、imageを使います。

```yaml
services:
    webserver:
        image: <イメージ名>:<タグ名>
```

 - imageには、イメージの名前またはイメージIDのいずれかを指定する
 - イメージのタグwp指定しない場合、最新バージョン(latest)がダウンロードされる

### イメージのビルド(`build`)
> イメージの構成をDockerfileに記述して、それを自動でビルドしてベースイメージに指定するときはbuildを指定します。buildには、Dockerfileのファイルパスを指定します。

```yaml
services:
    webserver:
        build: <Dockerfileのファイルパス>
```

 - buildには、dockercompose.ymlのあるディレクトリをカレントディレクトリとしたときのDockerfileの場所を指定します
 - 該当のDockerfile内でFROM命令でイメージを指定する

### コンテナ内で動かすコマンドの指定(`command`/`entrypoint`)
> コンテナで動かすコマンドは、commandで指定します

```yaml
# コンテナ内で動かすコマンドの指定
command: /bin/bash

command:
    - python manage.py runserver 127.0.0.1:8000
```
または、entrypointを上書きすることも可能
```yaml
entrypoint:
    - php
    - -d
    - memory_limit=-1
```

### コンテナ間の連携(`links`)
> 別のコンテナへリンク機能を使って連携したいときは、linksに連携先のコンテナ名を設定します。

```yaml
links:
    - <サービス名>
    - <サービス名>:<エイリアス名>  # コンテナ名とは別にエイリアス名を付けたいとき
```

### コンテナ間の通信(`ports`/`expose`)
> コンテナが公開するポートは、portsで指定します。

```yaml
ports:
    - "3000"
    - "8000:8000"
    - "49100:22"
    - "127.0.0.1:8001:8001"
    - "<ホストマシンのポート番号>":"<コンテナのポート番号>"
    - "<コンテナのポート番号>"
```
> ホストマシンへポートを公開せず、リンク機能を使って連携するコンテナにのみポートを公開するときは、exposeを指定します。<br>

ex) コンテナの内部のみに公開するポートの指定
```yaml
expose:
    - "3000"
    - "8000"
```

### サービスの依存関係の定義(`depends_on`)
> 複数のサービスの依存関係を定義するときは、depends_onを指定します。

ex) webserverコンテナを開始する前にdbコンテナとredisコンテナを開始したいときの例
```yaml
services:
    webserver:
        build: .
        depends_on:
            - db
            - redis
    redis:
        image: redis
    db:
        image: postgres
```

ここで注意しておきたいのは、depends_onがコンテナの開始の順序を制御するだけで、コンテナ上のアプリケーションが利用可能になるまで待つという制御を行わない点です。つまり、依存関係にあるデータベースサーバの準備が整うまで待つわけではないため、アプリケーション側で対策する必要があります。


### コンテナの環境変数の指定(`environment`/`env_file`)
> コンテナ内の環境変数を指定するときは、environmentを指定します。

```yaml
# 配列形式での指定
environment:
    - HOGE=fuga
    - FOO

# ハッシュ形式での指定
environments:
    HOGE: fuga
    FOO:
```

> 設定したい環境変数の数が多いときは、別ファイルで環境変数を定義して、そのファイルを読み込むこともできます。環境変数ファイルを読み込むときは、env_fileを指定します。

ex) ディレクトリ構成
```bash
tree
.
├── docker-compose.yml
└── envfile
```
ex) envfile
```bash
# envfile
HOGE=fuga
FOO=bar
```
ex) 環境変数ファイルの読み込み
```yaml
# docker-compose.yml
env_file: envfile
```

環境変数ファイルの複数読み込み
```yaml
env_file:
    - ./envfile1
    - ./app/envfile2
    - ./tmp/envfile3
```

### コンテナ名の設定(`container_name`)
> DockerComposeで生成されるコンテナに名前を付けるときは、container_nameを指定します。

```yaml
# docker-compose.yml
container_name: <コンテナ名>
```

### コンテナのラベル設定(`labels`)
> コンテナにラベルを付けるときは、labelsを指定します

```yaml
# 配列形式での指定
labels:
    - "com.example.description=Accounting webapp"
    - "com.example.department=Finance"

# ハッシュ形式での指定
labels:
    com.example.description: "Accountingwebapp"
    com.example.department: "Finance"
```

 - 設定したラベルを確認するときは、docker-compose configコマンドを使う


### コンテナのデータ管理(`volumes`/`volumes_from`)
> コンテナにボリュームをマウントするときは、volumesを指定します。

ボリュームの指定
```yaml
volumes:
    - /var/lib/mysql  # /var/lib/mysqlをマウント
    - cache/:/tmp/cache  # ホスト側でマウントするパスを指定 <ホストのディレクトリパス>:<コンテナのディレクトリパス>
```

> 下記の例のようにボリュームの指定の後ろにroを指定することで、ボリュームを読み取り専用としてマウントすることができます。設定ファイルが格納されたボリュームなどのように、書き込みを禁止したい場合に指定してください。

ボリュームの読み取り専用の設定
```yaml
volumes:
    - ~/configs:/etc/configs/:ro
```

> 別のコンテナからすべてのボリュームをマウントするときは、volumes_fromにコンテナ名を指定します。

ボリュームのマウント指定
```yaml
volumes_from:
    - <コンテナ名>
```

### コンテナを自動起動(`restart`)
> ホストOSを起動したタイミングでコンテナを起動させる

OSの起動時にコンテナを起動させる
```yaml
services:
    webserver:
        restart: always
```

| オプション | 説明 |
|:---------|:------|
| `no` | 再起動しない(デフォルト) |
| `always` | 明示的に`stop`がされない限り、終了ステータスに関係なく常に再起動が行われる |
