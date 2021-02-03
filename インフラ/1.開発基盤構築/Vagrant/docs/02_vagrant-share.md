# Vagrantのシェア

Vagrant Shareでは、世界各地の人とVagrant環境を共有することができます。これにより、ほとんどすべてのネットワーク上のVagrant環境で直接的にコラボレーションが可能になります。

Vagrantシェアは三つの主な特徴があります。これらの特徴は、相互に組み合わせて使うことができます。

 - **HTTP sharing**: この方法は他の人がアクセスできるURLを作ります。そのURLは、あなたのVagrant環境に直接アクセスできるものです。
    - この方法は、webhooksをテストするときもしくはマネージャー、チームメンバーなどにVagrant環境を見せたいときに便利
 - **SSH sharing**: this model will allow instant SSH access to your Vagrant environment by anyone by running `vagrant connect --ssh` on the remote side. This is useful for pair programming, debugging ops problems, etc.
    - この方法は、**<font color ="red">ペアプログラミング</font>**(デバック, etc)に向いている
 - **General sharing**: this model allows anyone to access any exposed port of your Vagrant environment by running ```vagrant connect``` on the remote side.
    - **<font color ="red">LAN経由</font>**でVagrant環境にアクセスしたいときに便利

**<font color="red">※Vagrantシェアを使うためには[ngrok](https://ngrok.com/)が必須</font>**


## HTTP Sharing




## SSH Sharing


---
## Connect
