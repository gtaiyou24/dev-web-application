djangoはデフォルトで`auth_user`というユーザテーブルを用意している。そのデフォルトのモデルをカスタマイズしたいときがある。

ex)

 - カラムを追加したい
 - 独自のメソッドを追加したい

大体こんな感じだ。

そこで、djangoのデフォルトのUserモデルをカスタマイズする方法をまとめます。

# Userモデルのカスタマイズ

 1. `AbstractBaseUser`を継承して独自のUserモデルを作成する
 2. `django.contrib.auth.models`の`AbstractUser`をまねて必要そうなメソッド、カラムを追加する
 3. `settings.py`に認証するUserモデルを指定する

### 1. `AbstractBaseUser`を継承して独自のUserモデルを作成する
https://docs.djangoproject.com/ja/1.9/topics/auth/customizing/#a-full-example
https://docs.djangoproject.com/ja/1.9/topics/auth/customizing/#extending-the-existing-user-model
https://github.com/gtaiyou24/django/blob/master/django/contrib/auth/base_user.py
https://github.com/gtaiyou24/django/blob/master/django/contrib/auth/models.py

# 3. `settings.py`に認証するUserモデルを指定する

settings.pyの`AUTH_USER_MODEL='users.User'`

# 4. `python manage.py migrate auth`を実行
