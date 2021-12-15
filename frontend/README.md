# Frontend Setup

## Prerequisites

- [Docker](https://docs.docker.com/v17.12/install/)
  - if you want to run the frontend inside a docker container
- [NodeJS](https://nodejs.org/en/)
- [Temple Wallet](https://templewallet.com/)
  - to be able to interact with smart contract
- [IPFS](https://docs.ipfs.io)

> 🚨 Be aware, that the frontend is currently only tested with the Temple Wallet! Support for other wallets may work, but is not guaranteed at the moment.

## Recommended VSCode Extensions

- [Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur)
- [Headwind](https://marketplace.visualstudio.com/items?itemName=heybourn.headwind)
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
- [Tailwind CSS IntelliSence](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)

## Development Environment Setup

- install all necessary dependencies

```
npm install ipfs-core
npm install
```

- run a development server via npm script
- the frontend will be accessible at http://localhost:8080/

```
npm run serve
```

- run a development server via Docker
- the frontend will be accessible at http://localhost:8080/

```
docker run -p 8080:8080 taia-x-frontend
```

## Production Environment Setup

- install all necessary dependencies

```
npm install
```

- compile, minify and build for production

```
npm run build
```

## Tests, Linting and Docs

- run unit tests

```
npm run test:unit
```

- lint and fix file formatting

```
npm run lint
```

- generate typedoc documentation
- to access the documentation, open `./docs/index.html` in a live-server

```
npm run docs
```
