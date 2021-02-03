# 1. Webサーバの設定
## Apache

## Nginx


---
# 2. デプロイチェック
Djangoプロジェクトをデプロイする前に、設定・セキュリティ・パフォーマンスを見直す。

**デプロイの確認 `django-admin manage.py check --deploy`**

ex) `django-admin manage.py check --deploy --settings="production_settings"`

## 重要な設定
#### `SECRET_KEY`
**秘密鍵は、巨大なランダムの値でなければならず、それは秘密にしておく必要がある**

本番環境で使用されている秘密鍵が他の場所で使用されていないことを確認し、ソース管理にコミットすることしないように。これにより、攻撃者が秘密鍵を取得する可能性が低くなる。

設定モジュールで秘密鍵をハードコーディングする代わりに、環境変数からロードするようにしてください。

```python
import os
SECRET_KEY = os.environ['SECRET_KEY']
```
または
```python
with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()
```


#### `DEBUG`
**本番環境ではデバッグを有効にしてはいけない**

開発環境では`DEBUG = True`をして開発するが、本番環境では`False`にする。なぜなら、プロジェクトに関する多くの情報(ソースコード,ローカル変数,設定,使用されているライブラリの抜粋など)が漏洩するから。

```python
DEBUG = False
```

## 環境固有の設定
#### [`ALLOWED_HOSTS`](https://docs.djangoproject.com/ja/1.11/ref/settings/#std:setting-ALLOWED_HOSTS)
`DEBUG = False`の場合、Djangoは`ALLOWED_HOSTS`に適切な値を指定しなければ、全く動作しないようになっている。

```python
ALLOWED_HOST = ['www.example.com']
```

この設定は、CSRF攻撃に対してサイトを保護するために必要である。

また、ホストを検証するためにDjangoの前にあるWebサーバーを構成する必要があります。 Djangoにリクエストを転送するのではなく、静的エラーページで応答するか、間違ったホストに対するリクエストを無視する必要があります。 こうすることで、あなたのDjangoログ（またはエラー報告がそのように設定されている場合は電子メール）に偽のエラーを避けることができます。 たとえば、nginxでは、認識されないホストに「444応答なし」を返すようにデフォルトサーバを設定することができます：

```shell
server {
    listen 80 default_server;
    return 444;
}
```

#### [`CACHES`](https://docs.djangoproject.com/ja/1.11/ref/settings/#std:setting-CACHES)
キャッシュを使用している場合、接続パラメータは開発段階と運用段階で異なる場合があります。 Djangoはプロセス毎のローカルメモリキャッシングをデフォルトにしていますが、それは望ましくないかもしれません。([`CACHES`](https://docs.djangoproject.com/ja/1.11/ref/settings/#std:setting-CACHES)を参照)

キャッシュサーバには、しばしば弱い認証があります。アプリケーションサーバーからの接続のみを受け入れるようにしてください。

もしMemcachedを使用しているのなら、パフォーマンスを改善するために[cached sessions](https://docs.djangoproject.com/ja/1.11/topics/http/sessions/#cached-sessions-backend)を使うことを検討してください。

#### [`DATABASES`](https://docs.djangoproject.com/ja/1.11/ref/settings/#std:setting-DATABASES)

 - データベースの接続パラメータは、開発段階と運用段階ではおそらく異なる。
 - データベースのパスワードを非常に敏感です。SECRET_KEYとまったく同じように保護する必要があります。
 - 最大限のセキュリティを確保するには、データベースサーバがアプリケーションサーバからの接続のみを受け入れるようにしてください。
 - データベースのバックアップを設定していない場合は、今すぐ実行してください。


#### [`EMAIL_BACKEND`](https://docs.djangoproject.com/ja/1.11/ref/settings/#std:setting-EMAIL_BACKEND)および関連する設定
もしサイトがEメールを送信するなら、以下の値は正しく設定されている必要がある。

デフォルトでは、Djangoは`webmaster@localhost`と`root@localhost`で送信するようになっている。しかしながら、いくつかのメールプロバイダーはこれらのアドレスを拒否するようになっている。違う送信用アドレスを使うためには、**[`DEFAULT_FROM_EMAIL`](https://docs.djangoproject.com/ja/1.11/ref/settings/#std:setting-DEFAULT_FROM_EMAIL)**と**[`SERVER_EMAIL`](https://docs.djangoproject.com/ja/1.11/ref/settings/#std:setting-SERVER_EMAIL)**を修正する。

#### [`STATIC_ROOT`](https://docs.djangoproject.com/ja/1.11/ref/settings/#std:setting-STATIC_ROOT)そして[`STATIC_URL`](https://docs.djangoproject.com/ja/1.11/ref/settings/#std:setting-STATIC_URL)
Staticファイルは開発サーバーによって自動的に表示される。本番サーバーの場合, [collectstatic](https://docs.djangoproject.com/ja/1.11/ref/contrib/staticfiles/#django-admin-collectstatic)がコピーする`STATIC_ROOT`フォルダを開発者が定義しなけらばならない。

詳しくは、[静的ファイル (画像、JavaScript、CSS など) の管理](https://docs.djangoproject.com/ja/1.11/howto/static-files/)を参照

#### `MEDIA_ROOT`そして`MEDIA_URL`


## HTTPS
#### `CSRF_COOKIE_SECURE`

#### `SESSION_COOKIE_SECURE`


## パフォーマンス最適化
#### `CONN_MAX_AGE`

#### `TEMPLATES`


## エラーレポート
#### `LOGGING`

#### [`ADMINS`](https://docs.djangoproject.com/ja/1.11/ref/settings/#std:setting-ADMINS)そして[`MANAGERS`](https://docs.djangoproject.com/ja/1.11/ref/settings/#std:setting-MANAGERS)
`ADMINS`はEメールによって500エラーが通知される。

`MANAGERS`は404エラーが通知される。[`IGNORABLE_404_URLS`](https://docs.djangoproject.com/ja/1.11/ref/settings/#std:setting-IGNORABLE_404_URLS)であやしい報告を除外することも可能。

Eメールによるエラー報告の詳細は[Error reporting](https://docs.djangoproject.com/ja/1.11/howto/error-reporting/)を参照。

#### デフォルトのErrorViewをカスタマイズする

 - [404（ページが見つかりません）ビュー](https://docs.djangoproject.com/ja/1.11/ref/views/#http-not-found-view)
 - [500（サーバーエラー）ビュー](https://docs.djangoproject.com/ja/1.11/ref/views/#http-internal-server-error-view)
 - [403（HTTP禁止）ビュー](https://docs.djangoproject.com/ja/1.11/ref/views/#http-forbidden-view)
 - [400（不正な要求）ビュー](https://docs.djangoproject.com/ja/1.11/ref/views/#http-bad-request-view)


---
# 設定ファイル`development.py`と`production.py`のテンプレート


---
# 参考文献

[Django を Apache と mod_wsgi とともに使うには？](https://docs.djangoproject.com/ja/1.11/howto/deployment/wsgi/modwsgi/)
[デプロイチェックリスト](https://docs.djangoproject.com/ja/1.11/howto/deployment/checklist/#secret-key)
