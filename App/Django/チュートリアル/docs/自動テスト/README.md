# 自動テスト

## テストの実行
pollsはアプリケーション名
```bash
python manage.py test polls
```

### テストの実行に失敗した場合
`python manage.py test polls`を実行する際に以下のエラーに出くわしました。
```bash
Creating test database for alias 'default'...
Got an error creating the test database: (1044, "Access denied for user 'mysite'@'%' to database 'test_mysite'")
```
このエラーは、Djangoのテスト用データベース`test_mysite`が存在しない＆該当のユーザーに対して権限がないために発生するものです。

そのため、rootユーザーでdbサービスのデータベースにアクセスし、`test_mysite`を作成し、該当のユーザーに対して権限を付与する必要があります。
```sql
mysql> CREATE DATABASE test_mysite;
# Query OK, 1 row affected (0.00 sec)

mysql> GRANT ALL PRIVILEGES ON test_mysite.* TO 'mysite'@'%';
```

これで再度、自動テストを実行すると正常に実行される。なお、テスト用データベースは削除される。

## 参考文献

 - [Django におけるテスト | Django ドキュメント | Django](https://docs.djangoproject.com/ja/2.1/topics/testing/)