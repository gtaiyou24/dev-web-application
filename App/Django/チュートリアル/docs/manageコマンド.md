# `python manage.py`コマンドの一覧

<!-- MarkdownTOC -->

- マイグレーション系
    - マイグレーションファイルを生成する
    - マイグレーションファイルをSQLコマンドにして表示する
    - モデルのテーブルをデータベースに作成する
- シェル系\(`python manage.py shell`\)

<!-- /MarkdownTOC -->


## マイグレーション系
### マイグレーションファイルを生成する
pollsはアプリケーション名
```bash
python manage.py makemigrations polls
# Migrations for 'polls':
#   polls/migrations/0001_initial.py:
#     - Create model Choice
#     - Create model Question
#     - Add field question to choice
```
makemigrations を実行することで、Djangoにモデルに変更があったこと(この場合、新しいものを作成しました)を伝え、そして変更を マイグレーション の形で保存することができました。

### マイグレーションファイルをSQLコマンドにして表示する
マイグレーションがどんなSQLを実行するのか表示する。

pollsはアプリケーション名
```bash
python manage.py sqlmigrate polls 0001
```

### モデルのテーブルをデータベースに作成する
```bash
python manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, polls, sessions
# Running migrations:
#   Applying polls.0001_initial... OK
```


## シェル系(`python manage.py shell`)

