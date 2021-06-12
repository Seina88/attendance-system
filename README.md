# 勤怠管理システム

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

============================================================ test session starts =============================================================
platform linux -- Python 3.9.4, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /app/backend/src
collected 4 items

tests/domains/user/test_user.py::TestUser::test_すべての引数を与えた場合に正常に登録される PASSED                                      [ 25%]
tests/domains/user/test_user.py::TestUser::test_idをNoneで与えた場合にUUIDが発行される PASSED                                          [ 50%]
tests/domains/user/test_user.py::TestUser::test_update関数を実行するとid以外のメンバ変数が更新される PASSED                            [ 75%]
tests/domains/user/test_user.py::TestUser::test_update関数の引数にNoneを指定したメンバ変数は更新されない PASSED                        [100%]

============================================================= 4 passed in 0.21s ==============================================================
```
