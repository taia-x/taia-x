# Taia-x Contracts

## Prerequisites

- [Docker](https://docs.docker.com/v17.12/install/)
  - Used for LIGO compilations and running a local sandbox Tezos node.
- [NodeJS](https://nodejs.org/en/)

## Project setup

```
yarn install
```

## Usage

- Compiling the smart contracts outputs michelson files to `/build/`. These files may either be deployed to a local sandbox or a testnet as explained below.

  ```shell
  yarn run compile
  ```

### Deploy on local sandbox

- Starting the local sandbox Tezos node

  ```shell
  yarn run start-sandbox
  ```

- A secret (unencrypted: ...) can be obtained by running sandbox-info (Only alice is needed for now) inside `config/sandbox.config.js`.

  ```shell
  yarn run sandbox-info
  ```

- Deploying contracts on local sandbox

  ```shell
  yarn run deploy:sandbox
  ```

### Deploy on granada testnet

- A test faucet can be obtained from https://faucet.tzalpha.net/. Once saved, it can be imported inside faucet key of `config/testnet.config.js`

- Deploying contracts on testnet (faucet must be obtained as explained at the bottom)

  ```shell
  yarn run deploy:testnet
  ```

## Useful links

| Description                                       | Link                                                                          |
| ------------------------------------------------- | ----------------------------------------------------------------------------- |
| Starting and Using a Sandbox                      | https://assets.tqtezos.com/docs/setup/2-sandbox/#starting-and-using-a-sandbox |
| Ligo CLI Commands (e.g. for compiling a contract) | https://ligolang.org/docs/api/cli-commands                                    |
