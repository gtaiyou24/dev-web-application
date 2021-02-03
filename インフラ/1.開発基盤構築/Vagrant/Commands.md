# 仮想マシンの構築

 1. **Box(仮想マシンのテンプレート)を取得**
    1. [VagrantのBox](https://app.vagrantup.com/boxes/search)から選ぶ
    2. ```vagrant box add [box名]``` ex)```vagrant box add hashicorp/precise64```
    3. ```vagrant box list```でインストールしたboxの一覧を表示できる
    - ```vagrant box remove [box名]```で削除できる
    - ```ls ~/.vagrant.d/boxes```でインストールしたboxに移動できる
 2. **仮想マシンを初期化する**
    - 仮想マシンごとにディレクトリを作成する必要がある: ```mkdir DIRECTORY_NAME```
    - ```cd DIRECTORY_NAME```
    - 仮想マシンを初期化: ```vagrant init [box名]```
        - →`Vagrantfile`というRubyファイルができる
 3. **仮想マシンを起動する**
    - ```vagrant up```
        - 仮想マシンの実態はVirtualBoxにある


# 仮想マシンの停止・再起動・削除

| コマンド | 説明 |
|:-------:|:----|
| ```vagrant status``` | 状態の確認 |
| ```vagrant suspend``` | スリープさせたい場合 |
| ```vagrant resume``` | 復帰させたい場合 |
| ```vagrant halt``` | 仮想マシンを停止 |
| ```vagrant reload``` | 再起動 |
| ```vagrant destroy``` | 仮想マシン自体を削除 |

# 仮想マシンに接続する

 - 仮想マシンに接続し、作業する
```bash
vagrant ssh
```
→仮想マシンの中にvagrantユーザで入る

 - Webページを作ってブラウザから閲覧する
```bash
sudo yum -y install httpd # apacheをインストール
sudo service httpd start # httpサーバーを起動
sudo chkconfig httpd on # 再起動してもWebサーバーが自動的にオンになるようにする
sudo service iptables sotp # ファイヤーウォールを切る。ローカルで開発するので問題ない
sudo chkconfig iptables off
```

# Webページを表示する

 1. Webページを作る
```bash
cd /var/www/html
# このフォルダをwebページを作る
```

 2. 一旦仮想マシンから出る
```bash
exit
```

 3. Macから仮想マシンの中身を見る
```bash
vi Vagrantfile
~~~
Vagrantfileの編集（`config.vm.network :private_network, ip: "192.168.33.10"`のコメントアウトを外す）
~~~
vagrant reload # 仮想マシンを再起動
```

→その後ブラウザにアクセスして`192.168.33.10`で観れる


# 共有フォルダを使う
Webページを作成するときにMac上で修正したら即座に反映されるようにする→共有フォルダを使う

```bash
vagrant ssh
sudo rm -rf /var/www/html # 仮想マシン側のドキュメントルートを削除する
sudo ln -fs /vagrant /var/www/html # Mac側のWeb開発するための作業パス
```


# Provisioningを使う
### Provisioning
> ```vagrant up```をしたあとに、自動的に実行される一連の処理のことを指す<br>
> →webサーバのインストールやファイヤーウォールの設定を自動でやってくれる

webサーバのインストールやファイヤーウォールの設定を自動でやってくれる

Chefとかでも行えるが今回はshellスクリプトで行う
```bash
vi Vagrantfile
# Vagrantfileの編集
config.vm.provision :shell, :path => "provision.sh"
```

provision.sh↓
```bash
sudo yum -y install httpd
sudo service httpd start
sudo chkconfig httpd on
```

仮想マシンがすでに立ち上がっている状態でprovisionだけを再実行したい場合
```bash
vagrant provision
```

# Boxを自作する
現在の仮想マシンの状態からBoxを作っていく方法について見ていきます。またそのBoxをもとに仮想マシンを作り、動作確認も行います。


```
vagrant package
vagrant box add my_box package.box
ls ~/.vagrant.d/boxes
rm package.box
cd ..
mkdir myBox
cd myBox
vagrant init my_box
vagrant up
vagrant ssh
sudo service httpd status
```

# Pluginを使う
Vagrantに便利な機能を提供するpluginの導入方法

```
vagrant plugin install [プラグイン名]
vagrant plugin -h
vagrant plugin list
vagrant plugin uninstall [インストールしたプラグイン名]
```
