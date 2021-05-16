FROM node:16.0.0

# 静的コンテンツを配信するシンプルな http サーバをインストールする
RUN npm install -g http-server

# カレントワーキングディレクトリとして '/app/frontend' フォルダを指定する
WORKDIR /app/frontend

# `package.json` と `package-lock.json` （あれば）を両方コピーする
COPY package.json yarn.lock ./

# プロジェクトの依存ライブラリをインストールする
RUN yarn install

# カレントワーキングディレクトリ(つまり 'app' フォルダ)にプロジェクトのファイルやフォルダをコピーする
COPY . .

# 本番向けに圧縮しながらアプリケーションをビルドする
RUN yarn run build

EXPOSE 8080
CMD [ "http-server", "dist" ]
