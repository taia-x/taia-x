FROM node:14.5.0-alpine

WORKDIR /usr/src/frontend

COPY package*.json ./  

RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "run", "serve"]