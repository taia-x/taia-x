FROM node:14.17.1-alpine3.13

WORKDIR /opt/taia-x/frontend

COPY package*.json ./  

RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "run", "serve"]