# CentOS7 + pyenv + Python3 + GitHubの開発環境の構築

**Pythonの動作環境の想定**

 - VirtualBoxをインストールしていること


**実現したいこと**

 - ローカル側にソースコードを置き、gitで管理
 - Synched Folder 機能で仮想マシン側のマシンとデータ共有(ソースコード)
 - ローカル側でソースコードを編集し、仮想マシン上でソースコードを実行
 - ローカル側でソースコードをcommit/push



## 1. CentOSの設定

CentOS7(CentOS Linux 7 x86_64)のboxを追加していない場合は追加する。
```zsh
$ vagrant box add centos/7
$ vagrant box list          # CentOS7のBoxが追加されているのかを確認
```

Boxを追加したら、仮想マシンを初期化・起動する
```zsh
$ cd /var/www/html       # 開発用フォルダに移動
$ mkdir PROJECT_NAME     # プロジェクトフォルダを作成
$ cd PROJECT_NAME
$ vagrant init centos/7  # CentOSを初期化.`Vagrantfile`ができているはず.
$ vagrant up             # CentOSを起動
$ vagrant status         # CentOSが起動しているのを確認
Current machine states:

default                   running (virtualbox)
...
```

次に仮想マシンにssh接続して、動作に必要なサーバーの設定を行う
```zsh
$ vagrant ssh                    # CentOSに接続
(vagrant)$ sudo yum -y update    # OSを最新版にアップデート
```

## 2. pyenvをインストール

```bash
# at vagrant env.

# pyenvの依存ライブラリをインストール
$ sudo yum -y install readline-devel zlib-devel bzip2-devel sqlite-devel openssl-devel \
    libXext.x86_64 libSM.x86_64 libXrender.x86_64 gcc gcc-c++ libffi-devel python-devel

# gitコマンドがインストールされていなければインストール
$ sudo yum -y install git
$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
$ source ~/.bash_profile
$ exec $SHELL -l

# インストールできるバージョンを表示できればpyenvのインストールに成功した
$ pyenv install --list
```

## 3. Python3をインストール

```bash
# at vagrant env.

$ pyenv install 3.6.2
$ pyenv versions
$ pyenv global 3.6.2
```

## 4. 同期フォルダの設定

```bash
# at local env.

$ vim Vagrantfile
```
```ruby
~~
config.vm.synced_folder ".", "/vagrant_data"
~~
```
```bash
# at local env.

$ vagrant reload
$ vagrant ssh
```

## 5. 作業

 - ローカルで編集 <-> 仮想マシンで実行
 - ローカル側でGithubへコミットする


---
## Provision

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"

  config.vm.synced_folder ".", "/vagrant_data", create: true

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = 3072
  end

  config.vm.provision :shell, path: "set_os_env.sh"
  config.vm.provision :shell, path: "set_pyenv.sh", privileged: false
end

```

```bash
$ vim set_os_env.sh
```

```bash
#!/bin/bash

sudo yum -y update
sudo yum -y install readline-devel zlib-devel bzip2-devel sqlite-devel openssl-devel \
    libXext.x86_64 libSM.x86_64 libXrender.x86_64 gcc gcc-c++ libffi-devel python-devel
```

```bash
$ vim set_pyenv.sh
```

```bash
#!/bin/bash
PY_VERSION="3.6.2"

sudo yum -y install git
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
pyenv install $PY_VERSION
pyenv global $PY_VERSION
exec $SHELL -l
```

## 参考文献

 - [Vagrant + CentOS7 + pyenv + Python3 環境構築](https://runble1.com/centos7-pyenv-python3/)
 - [pyenv + virtualenv (CentOS7) - Qiita](https://qiita.com/saitou1978/items/e82421e29e118bd397cc)
 - [python(pyenv + virtualenv) + CentOS7インストールメモ - Qiita](https://qiita.com/Esfahan/items/0dfe70357549f92b23da)
 - [VagrantのShell Provisionで、nvmをインストールする際に気をつけること - Qiita](https://qiita.com/kawanamiyuu/items/cc3f4fa46a40005e11cc)
 - [プロビジョニングの実行ユーザを変更する方法 - stackoverflow](https://stackoverflow.com/questions/22547575/execute-commands-as-user-after-vagrant-provisioning)
