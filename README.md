# 勤怠管理システム

![Backend Test](https://github.com/Seina88/attendance-system/actions/workflows/backend-test.yml/badge.svg)

## 環境構築

1. リポジトリのクローン

   ```sh
   git clone https://github.com/Seina88/attendance-system.git
   cd attendance-system/
   ```

2. 環境変数の設定

   ```sh
   cp .env.sample .env
   ```

3. Visual Studio Code の設定

   ```sh
   cp ./.vscode/settings.sample.json ./.vscode/settings.json
   ```

## サーバの起動

### Docker

1. Docker コンテナのビルド・起動、Web ページを開く

   ```shell
   make build
   make start
   open http://localhost
   ```

2. Docker コンテナの停止

   ```shell
   make stop
   ```

### ローカル

1. パッケージのインストール

   ```shell
   make install
   ```

2. API サーバの起動

   ```shell
   make backend-start
   ```

3. Vue サーバの起動

   ```shell
   make frontend-start
   ```

4. サーバの停止

   2, 3 の画面で、それぞれ`Ctrl + C`

## テスト

```shell
$ make test

===================================================================== test session starts ======================================================================
platform linux -- Python 3.9.4, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /app/backend/src
plugins: Faker-8.7.0
collected 15 items

tests/domains/user/test_user.py::TestUser::test_すべての引数を与えた場合に正常に登録される PASSED                                                        [  6%]
tests/domains/user/test_user.py::TestUser::test_idをNoneで与えた場合にUUIDが発行される PASSED                                                            [ 13%]

...

tests/interfaces/user/test_update_user.py::TestUpdateUser::test_api_tokenを付与しなかった場合400エラー PASSED                                            [ 93%]
tests/interfaces/user/test_update_user.py::TestUpdateUser::test_ユーザ情報を更新 PASSED                                                                  [100%]

====================================================================== 15 passed in 2.28s ======================================================================
```
