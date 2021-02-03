# CentOS + Django + Python3 + GitHub環境の構築


## 1. CentOS + pyenv + Python3を仮想マシンにインストール
このインストール手順は[CentOS7 + pyenv + Python3 + GitHubの開発環境の構築](.build-python3-env.md)の**`3. Python3をインストール`**までを参照、実行する。

しかし、開発用フォルダのプロジェクトフォルダ内ではすでにDjangoのアプリケーションがあるものとする。


## 2. Django/Nginxのインストール/設定

**Nginxのインストール/設定**
```zsh
(vagrant)$ sudo rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm # CentOS7系なので、nginx-release-centos-7-0.el 7.ngx.noarch.rpmをリポジトリに追加
(vagrant)$ sudo yum -y update nginx-release-centos                  # Nginxをインストール
(vagrant)$ sudo yum -y --enablerepo=nginx install nginx
(vagrant)$ nginx -v
nginx version: nginx/1.8.1

(vagrant)$ sudo systemctl start nginx                               # Webサーバーを起動
(vagrant)$ sudo systemctl enable nginx                              # WebサーバーNginxの自動起動設定
(vagrant)$ sudo systemctl stop firewalld                            # ファイヤーウォールを切る
```

**Djangoのインストール/設定**
```zsh
(vagrant)$ pip install django
(vagrant)$ sudo rm -rf /var/www/html                               # 仮想マシン側のドキュメントルートを削除する
(vagrant)$ sudo ln -fs /vagrant /var/www/html/PROJECT_NAME         # ローカル側のWeb開発するための作業パス
(vagrant)$ exit
$ vim Vagrantfile
```
```ruby
~~
config.vm.network "forwarded_port", guest: 80, host: 8080
config.vm.network :private_network, ip: "192.168.33.10"
~~
```
```zsh
$ vagrant reload                 # 設定を反映させるため再起動
```

```zsh
vagrant ssh
(vagrant)$ sudo rm -rf /var/www/html # 仮想マシン側のドキュメントルートを削除する
(vagrant)$ sudo ln -fs /vagrant /var/www/html # Mac側のWeb開発するための作業パス
```

別ターミナルを開き、
```zsh
$ cd /var/www/html/PROJECT_NAME
$ python manage.py runserver
```

→ブラウザにアクセスして`192.168.33.10`で観れる

## 参考文献

 - [5分でできるVagrantでDjangoの環境構築 - Qiita](https://qiita.com/244mix/items/6fd9991c6fcba00c4c71)
 - [Vagrant＋Flaskでローカル開発環境を構築する。 - 備忘録](http://hchckeeer.hatenadiary.jp/entry/2016/07/30/183734)
 - [vagrant環境にDjangoをインストールしてみた | shuusetuのブログ](http://blog.shuusetu.com/?p=245)
 - [仮想マシンにPython3とWEBフレームワークDjangoをインストール方法 | ハジプロ！](https://hajipro.com/local-development-environment-mac/centos-python3-nginx-django)
