FROM centos:7

LABEL maintainer="管理者アカウント<メールアドレス>"
LABEL title="イメージタイトル"

# デフォルトシェルの指定
SHELL ["/bin/bash", "-c"]

# 必要なパッケージをインストール
RUN yum -y update
RUN yum -y install readline-devel zlib-devel bzip2-devel sqlite-devel openssl-devel \
    libXext.x86_64 libSM.x86_64 libXrender.x86_64 gcc gcc-c++ libffi-devel python-devel git

# ロケーション設定(日本語ロケールを設定)
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"

# python3系をインストール
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum install -y python36u python36u-devel python36u-libs python36u-pip

# requirements.txtに記載されたパッケージをインストール
ARG WORKDIR_PATH="/home/tinder_bot"
RUN mkdir -p $WORKDIR_PATH
ADD requirements.txt $WORKDIR_PATH
RUN pip3.6 install --upgrade pip
RUN pip3.6 install -r requirements.txt