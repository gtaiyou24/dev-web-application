# モデルの変更を実施する
モデルの変更を実施するための4ステップ

 1. (models.pyの中の)モデルを変更する
 2. `settings.py`の`INSTALLED_APPS`にDjangoアプリケーション(`polls.apps.PollsConfig`)を追加する
 3. これらの変更のためのマイグレーションを作成するために`python manage.py makemigrations`を実行します。
 4. データベースにこれらの変更を適用するために`python manage.py migrate`を実行します。