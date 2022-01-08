FROM node:14

WORKDIR /opt/taia-x/contracts

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "serve"]