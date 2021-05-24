FROM node:16.0.0
RUN npm install -g http-server
WORKDIR /app/frontend
COPY package.json yarn.lock ./
RUN yarn install
COPY . .
RUN yarn run build
EXPOSE 8080
CMD [ "http-server", "dist" ]
