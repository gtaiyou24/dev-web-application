# Vagrantfile

Vagrantfileには主に次のようなこをと記述します。

 - プロジェクトに必要なマシンのタイプ
 - マシンの設定方法
 - マシンのプロビジョニング方法

Vagrantはプロジェクトごとに1つのVagrantfileで実行され、そして**<font color="blue">VagrantファイルはGitHubなどのバージョン管理にコミットされることを想定されている</font>**。これにより、プロジェクトに携わっている他の開発者は、`vagrant up`で起動して、コードを確認することができる。Vagrantファイルは、Vagrantをサポートするすべてのプラットフォームで移植可能です。


## Lookup Path

任意のVagrantコマンドを実行すると、Vagrantはディレクトリツリーを登り、現在のディレクトリから最初に見つかるVagrantファイルで実行する。そのため、もし`/home/mitchellh/projects/foo`で`vagrant`を起動すると次のパスから順にVagrantfileを探します。

```
/home/mitchellh/projects/foo/Vagrantfile
/home/mitchellh/projects/Vagrantfile
/home/mitchellh/Vagrantfile
/home/Vagrantfile
/Vagrantfile
```

## Load Order and Merging

Vagrantは一連のVagrantfileを実際に読み込んで、設定をマージする。これにより、様々なレベルの特異性のあるvagrantfileが以前の設定を上書きすることができる。vagrantfileは次の順番で読み込まれる。もしvagrantfileがどのステップでも見つからない場合はVagrantは次のステップへ進む。

 1.

---
## 設定バージョン

```ruby
Vagrant.configure("2") do |config|
  # version 2 configs...
end
```

現在、Vagrantがサポートされている設定バージョンは「1」と「2」の2つだけです。バージョン1は、Vagrant 1.0.xの設定を表します。 "2"は1.1 + 2.0.xまでの構成を表します。設定バージョンは「2」が現役である。

Vagrantfilesをロードするとき、Vagrantは各バージョンに適切な設定オブジェクトを使用し、他の設定と同様にそれらを適切にマージします。

---
## Minimum Vagrant Version
VagrantのバージョンをVagrantファイルで指定して、特定のバージョンのVagrantをVagrantfileで使用するように強制することができます。

```ruby
Vagrant.require_version ">= 1.3.5"
```

another

```ruby
Vagrant.require_version ">= 1.3.5", "< 1.4.0"
```

---
## `config.vm`
config.vmでの設定は、Vagrantが管理するマシンの構成を変更します

 - `config.vm.box`: 仮想マシンが使用するBoxを指定。ここでの値は、インストールされたBoxもしくは、Boxの略称でなければならない。
 - `config.vm.box_check_update`
 - `config.vm.box_download_checksum`
 - `config.vm.box_download_checksum_type`
 - `config.vm.box_download_client_cert`
 - `config.vm.box_download_ca_cert`
 - `config.vm.box_download_ca_path`
 - `config.vm.box_download_insecure`
 - `config.vm.box_url`
 - `config.vm.box_version`
 - `config.vm.communicator`
 - `config.vm.graceful_halt_timeout`
 - `config.vm.guest`
 - `config.vm.hostname`
 - `config.vm.network`
 - `config.vm.post_up_message`
 - `config.vm.provider`
 - `config.vm.provision`
 - `config.vm.synced_folder`
 - `config.vm.usable_port_range`

## `config.ssh`
config.sshでの設定は、VagrantがSSH経由であなたのマシンにアクセスする方法の設定に関連しています。Vagrantのほとんどの設定と同様に、デフォルトは通常は問題ありませんが、好きなように微調整することができます。

 - `config.ssh.username`: Vagrantがデフォルトでsshするユーザ名を指定する。デフォルトは"vagrant"
 - `config.ssh.password`: Vagrantがsshユーザの認証に使用するパスワードを設定する。もしパスワードを使用する場合はVagrantは`insert_key`が`true`の場合にのみキーペアを自動的に挿入する。
 - `config.ssh.host`: sshへのホスト名 or IP。デフォルトは空です
 - `config.ssh.port`: sshへのポート番号。デフォルトでは22番ポート。
 - `config.ssh.guest_port`
 - `config.ssh.private_key_path`
 - `config.ssh.keys_only`
 - `config.ssh.shell`
 - `config.ssh.export_command_template`
 - `config.ssh.sudo_command`

## `config.winrm`


## `config.winssh`


## `config.vagrant`
