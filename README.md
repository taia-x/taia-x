<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">taia-x</h3>

  <p align="center">
    NFT-based Sharing Platform for Digital Twin Data on Tezos – a Project with GAIA-X
    <br />
    <a href="https://github.com/taia-x/taia-x/wiki"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="https://github.com/taia-x/taia-x/issues">Report Bug</a>
    ·
    <a href="https://github.com/taia-x/taia-x/issues">Request Feature</a>
  </p>
</div>

### Built With

- [Vue.js](https://vuejs.org/)
- [Tezos](https://tezos.com/developer-portal/)
- [Github Actions](https://github.com/features/actions)
- [TzKT](https://github.com/baking-bad/tzkt)
- [DipDup](https://github.com/dipdup-net/dipdup-py)
- [Hasura](https://github.com/hasura/graphql-engine)
- [Zokrates](https://zokrates.github.io/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

How to set up your project locally.

### Prerequisites

To run the project locally you need to have install node.js and Docker

### Installation (Sandbox)

1. In the `./contracts` directory run:

```bash
$ yarn install
```

2. Rename the `.env.template` in `./contracts` to `.env` file. The file should include the following data.

```bash
ALICE_SECRET=edsk3QoqBuvdamxouPhin7swCvkQNgq4jP5KZPbwWNnwdZpSpJiEbq
JON=jon,edpkuTWU5vkNqfFXSAJuZNVa4gAdF6iU3tZongtkgesoytne2YcqVj,tz1ggvpTMyxX5QVYqbpLVmNGCsgDpDyUMawq,unencrypted:edsk3Un2TGaZYUL1gCDPyUvkYvtxznkmZwfa4fdcjdWrne2kyvd3Lj
LAURA=laura,edpkv2PkEkoaYN9KP769GrFgshMoVn8cvHUuYVUkogxiqZMctxPbB8,tz1TUEs5dubGJoCkvSK11zFqTWU9jh6cV8kb,unencrypted:edsk3VdieyzxcsjFRxApVvLk8LQmQELiuJtGrww27WHamxF83dZwyY
MAGGY=maggy,edpkv8V18vjq3HjYXVtHHtiUB6VBkQBUVmQK4zkHKtZGHLQKagGKa7,tz1fekugemWNMQKcLjxv7YghhyDHwPqd1bVF,unencrypted:edsk3W5FsSG9GMWJNL2nPYJd5NNN8rtikT5Nq3hiJf9NGjDSZW8cco
SOURCE_FILE=/opt/taia-x/contracts/contracts/src/taia_x_main.mligo
OUTPUT_FILE=/opt/taia-x/contracts/contracts/out/taia_x_main.tz
ENTRY_POINT=main
```

3. In the `./contracts` folder compile and run the sandbox via:

```bash
$ docker compose up
```

4. In the `./contracts` folder deploy the contract to the sandbox via:

```bash
$ yarn run deploy:sandbox
```

5. Copy the contract address from the console output and assign it to `VUE_APP_CONTRACT_ADDRESS` in `./frontend/.env.template` and rename the file to `.env`.

6. Rename the `.env.template` in `./dipdup` to `.env` file and assign the contract address to `CONTRACT_ADDRESS`.

7. In the `./ipfs` folder run the ipfs cluster:

See [here](https://github.com/taia-x/taia-x/tree/main/ipfs) how to fix CORS error if it happens, when minting a token.

```bash
$ docker compose up
```

8. Rename the `.env.template` in `./backend` do `.env` and run the backend:

```bash
$ docker compose up
```

9. In the `./tzkt` folder run the tzkt indexer:

```bash
$ docker compose up
```

10. In the `./dipdup` folder build and run the selective contract indexer:

```bash
$ docker compose build
$ docker compose up
```

11. In the `./frontend` folder build and run taia-x:

```bash
$ docker compose build
$ docker compose up
```

or run without docker via `npm run serve`

12. Stop all containers by running `docker compose down` in the respective folders.

<p align="right">(<a href="#top">back to top</a>)</p>

### Wallet Setup (Sandbox)

1. Create a new Network for your local Sandbox with a local RPC endpoint. Set the RPC-Url to `http://localhost:20000` and the name to an arbitrary name.

<img width="357" alt="Bildschirmfoto 2022-02-04 um 16 26 02" src="https://user-images.githubusercontent.com/35061229/152557104-0a19e580-879a-4308-8b23-e17eae8f2170.png">

2. Import all accounts from the `.env` file in `./contracts` by it's private key, which starts with `edsk...`. The `.env` includes 4 predefined users:

- ALICE
- MAGGY
- JON
- LAURA

<img width="355" alt="Bildschirmfoto 2022-02-04 um 16 31 28" src="https://user-images.githubusercontent.com/35061229/152557131-b1f0dec3-fc7c-4e94-9570-37d00f01cc66.png">

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>

### Running Github Actions locally

Install [act](https://github.com/nektos/act#installation) following one of the options in the docs

To see the github actions available:

```
act -l
```

To run a specific action:

```
act -j GITHUB_ACTION_NAME
```

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Pull the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Project Link: [https://github.com/taia-x/taia-x](https://github.com/taia-x/taia-x)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/alvaro-alonso/taia-x.svg
[contributors-url]: https://github.com/taia-x/taia-x/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/alvaro-alonso/taia-x.svg
[forks-url]: https://github.com/taia-x/taia-x/network/members
[stars-shield]: https://img.shields.io/github/stars/alvaro-alonso/taia-x.svg
[stars-url]: https://github.com/taia-x/taia-x/stargazers
[issues-shield]: https://img.shields.io/github/issues/alvaro-alonso/taia-x.svg
[issues-url]: https://github.com/taia-x/taia-x/issues
[license-shield]: https://img.shields.io/github/license/alvaro-alonso/taia-x.svg
[license-url]: https://github.com/taia-x/taia-x/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
