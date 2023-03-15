FROM node:lts-alpine

RUN mkdir -p /app

WORKDIR /app
ADD ./package*.json /app/
ADD ./tsconfig* /app/

RUN npm i --include=dev
