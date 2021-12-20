FROM node:14

WORKDIR /opt/taia-x/frontend

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "serve"]