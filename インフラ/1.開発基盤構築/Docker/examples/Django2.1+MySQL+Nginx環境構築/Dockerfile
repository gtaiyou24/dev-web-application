FROM centos:7

LABEL maintainer="taiyou24<gtaiyou24@gmail.com>"
LABEL title="Matching Engine"

# デフォルトシェルの指定
SHELL ["/bin/bash", "-c"]

# 必要なパッケージをインストール
RUN yum -y update
RUN yum -y install gcc zlib-devel bzip2 bzip2-devel readline readline-devel \
           sqlite sqlite-devel openssl openssl-devel git

# ロケーション設定(日本語ロケールを設定)
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"

# pyenvをインストール
RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv
RUN echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bash_profile \
    echo 'eval "$(pyenv init -)"' >> ~/.bash_profile \
    source ~/.bash_profile
RUN pyenv --version

# python3系をインストール
RUN pyenv install 3.6.4
# pythonバージョンの切り替え
RUN pyenv global 3.6.4 \
    pyenv rehash
RUN python --version


# requirements.txtに記載されたパッケージをインストール
# ホームディレクトリ(/home)に移動
WORKDIR /home
ADD requirements.txt /home
RUN pip3.6 install --upgrade pip
RUN pip3.6 install -r requirements.txt