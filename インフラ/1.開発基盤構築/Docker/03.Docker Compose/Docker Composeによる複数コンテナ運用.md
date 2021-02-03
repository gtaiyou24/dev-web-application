# Docker Composeによる複数コンテナ運用

## Docker Composeのバージョン確認
```bash
docker-compose --version
# docker-compose version 1.23.2, build 1110ad01
```

## Docker Composeの基本コマンド

### 複数コンテナの生成(`up`)
> 作成したdockercompose.ymlをもとに、複数コンテナの生成／起動を行うときは、`docker compose up`コマンドを使います。

```bash
docker-compose up [オプション] [サービス名.]
```

| オプション | 説明 |
|:----------|:-----|
| `-d` | バックグラウンドで実行 |
| `--no-deps` | リンクのサービスを起動しない |
| `--build` | コンテナ起動時にDockerfileをビルドする |
| `--no-build` | イメージをビルドしない |
| `-t`, `--timeout` | コンテナのタイムアウトを秒指定(デフォルト10秒) |
| `--scale サービス名1=サービス名1の数 サービス名2=サービス名2の数` | 各サービスが起動するコンテナ数を指定 |

### 複数コンテナの確認(`ps`/`logs`)
> DockerComposeでは複数のコンテナが連携しながら動作します。それらの複数コンテナの一覧表示を行うときは、`docker compose ps`コマンドを使います

```bash
docker-compose ps [オプション]
```

| オプション | 説明 |
|:----------|:-----|
| `-q` | コンテナIDのみを表示する |


コンテナのログを確認する
```bash
docker-compose logs
```

### コンテナでのコマンド実行(`run`)
> Docker Composeで起動したコンテナで、任意のコマンドを実行したいときは、`docker compose run`コマンドを使います。

コンテナでのコマンド実行
```bash
docker-compose run <コンテナ名> <コマンド>

# ex) docker compose upコマンドで起動したserver_aという名前のコンテナで/bin/bashを実行する例
docker-compose run myapp_nginx /bin/bash
```

### 複数コンテナの起動/停止/再起動(`start`/`stop`/`restart`)
> Docker Composeを使うと、複数のサービスを一括で起動／一時停止／停止／再起動できます。

```bash
# コンテナ一括起動
docker-compose start

# コンテナ一括停止
docker-compose stop

# コンテナ一括再起動
docker-compose restart
```

特定のコンテナのみを操作したいとき
```bash
docker-compose restart <コンテナ名>
```

### 複数コンテナの一時停止/再開(`pause`/`unpause`)
> Docker Composeを使うと、複数のサービスを一括で一時停止／再開できます。

```bash
# コンテナ一括一時停止
docker-compose pause

# コンテナ一括再開
docker-compose unpause
```

### サービスの構成確認(`port`/`config`)
> サービスの公開用のポートを確認する

```bash
docker-compose port [オプション] サービス名 プライベートポート番号
```

| オプション | 説明 |
|:----------|:-----|
| `--protocol=proto` | プロトコル. tcpまたはudp |
| `--index=index` | コンテナのインデックス名 |

ex) webserverという名前のサービスの80番ポートに割り当てられている設定を確認
```bash
docker-compose port webserver 80
```

> Composeの構成を確認する
```bash
docker-compose config
```

### 複数コンテナの強制停止/削除(`kill`/`rm`)


### 複数リソースの一括削除(`down`)


