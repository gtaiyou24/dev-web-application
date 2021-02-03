# Python3.6の環境構築

## Dockerfileを作成


## イメージを作成
```bash
cd ~/path/to/dockerfileのパス

docker build -t イメージ名:タグ .
# ex) docker build -t myproject:1.0 .
```

イメージを確認
```bash
docker image ls | grep イメージ名
```

## コンテナを起動
```bash
# dockerとフォルダを共有した場所に移動
cd /my/project
# コンテナ起動(-v でフォルダを共有)
docker run --rm --name "コンテナ名" -it -v $(pwd):/root イメージ名:タグ /bin/bash

# at docker
bash-4.2#
```

別のコンソールからコンテナが起動していることを確認する
```bash
docker ps -a | grep コンテナ名
```