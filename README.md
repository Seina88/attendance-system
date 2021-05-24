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

   ```sh
   make build
   make start
   open http://localhost
   ```

2. Docker コンテナの停止

   ```sh
   make stop
   ```

### ローカル

1. パッケージのインストール

   ```sh
   make install
   ```

2. API サーバの起動

   ```sh
   make backend-start
   ```

3. Vue サーバの起動

   ```sh
   make frontend-start
   ```

4. サーバの停止

   2, 3 の画面で、それぞれ`Ctrl + C`
