# Taia-x Contracts

## Prerequisites

- [Docker](https://docs.docker.com/v17.12/install/)
  - Used for LIGO compilations and running a local sandbox Tezos node.
- [NodeJS](https://nodejs.org/en/)

## Project setup

- Install npm dependencies.

  ```
  yarn install
  ```

- Create `.env` file according `.env.template` by filling the necessary entries.

  > A test faucet can be obtained from https://faucet.tzalpha.net/. It must be saved as json string to `FAUCET`.

  > A secret (unencrypted: ...) can be obtained by running sandbox-info (Only alice is needed for now). It must be saved to `ALICE_KEY`.
  >
  > ```shell
  > yarn run sandbox-info
  > ```

  ```
  ALICE_SECRET=<ALICE_SECRET>
  FAUCET={"mnemonic": ["...", "...", ...], "secret": "...", "amount": "...", "pkh": "...", "password": "...", "email": "..."
  ```
- Replace the value of `compile` in `contracts/package.json` as follows:
  - Linux or OSX: ```docker run --rm -v '$PWD':'$PWD' -w '$PWD' ligolang/ligo:0.29.0 compile contract ./contracts/src/main.mligo --entry-point main > ./contracts/out/main.tz```
  - Windows: ```docker run --rm -v '%CD%':/cd -w /cd ligolang/ligo:0.29.0 compile contract ./contracts/src/main.mligo --entry-point main > ./contracts/out/main.tz```


  

## Usage

- Compiling the smart contracts outputs michelson files to `/contracts/out/`. These files may either be deployed to a local sandbox or a testnet as explained below.

  ```shell
  yarn run compile
  ```

### Deploy on local sandbox

- Starting the local sandbox Tezos node

  ```shell
  yarn run start-sandbox
  ```

- Alices secret must be available at `.env` file, as explained [above](#Project-setup).

- Deploying contracts on local sandbox

  ```shell
  yarn run deploy:sandbox
  ```

### Deploy on granada testnet

- A test faucet must be available at `.env` file, as explained [above](#Project-setup).

- Deploying contracts on testnet

  ```shell
  yarn run deploy:testnet
  ```

## Useful links

| Description                                       | Link                                                                          |
| ------------------------------------------------- | ----------------------------------------------------------------------------- |
| Starting and Using a Sandbox                      | https://assets.tqtezos.com/docs/setup/2-sandbox/#starting-and-using-a-sandbox |
| Ligo CLI Commands (e.g. for compiling a contract) | https://ligolang.org/docs/api/cli-commands                                    |
