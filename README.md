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

3. パッケージのインストール

   ```sh
   make install
   ```

4. API サーバの起動

   ```sh
   make backend-start
   ```

5. Vue サーバの起動

   ```sh
   make frontend-start
   ```
