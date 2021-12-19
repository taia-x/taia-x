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
  <a href="https://github.com/taia-x/taia-x">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">taia-x</h3>

  <p align="center">
    NFT-based Sharing Platform for Digital Twin Data on Tezos – a Project with GAIA-X
    <br />
    <a href="https://github.com/taia-x/taia-x"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/taia-x/taia-x">View Demo</a>
    ·
    <a href=https://github.com/taia-x/taia-x/issues">Report Bug</a>
    ·
    <a href="https://github.com/taia-x/taia-x/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)



<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Vue.js](https://vuejs.org/)
* [Tezos](https://tezos.com/developer-portal/)
* [Github Actions](https://github.com/features/actions)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Zokrates](https://zokrates.github.io/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

How to set up your project locally.

### Prerequisites

To run the project locally you need to have install node.js and Docker

### Installation

1. in the `backend` directory, create `.env`  file according `.env.template` by filling the necessary entries.
2. in the `contracts` directory, create `.env`  file according `.env.template` by filling the necessary entries.
3. start the local network by running:
```
$ docker-compose up
```
4. deploy the latest contracts to the local blockchain:

  - go to the `contracts` directory and install the packages
  ```
  $ cd contracts
  $ yarn install
  ```
  - compile the smart-contract:
    - Windows:
    ```
    docker run --rm -v \"%CD%\":/cd -w /cd ligolang/ligo:0.28.0 compile-contract ./contracts/src/counter.ligo main > ./contracts/out/counter.tz
    ```
    - Linux and OSX:
    ```
    $ docker run --rm -v '$PWD':'$PWD' -w '$PWD' ligolang/ligo:0.28.0 compile-contract ./contracts/src/counter.ligo main > ./contracts/out/counter.tz
    ```
  - deploy the smart-contract to the blockchain:
  ```
  $ yarn run deploy:testnet
  ```

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

<!-- ROADMAP -->
## Roadmap

- [] Feature 1
- [] Feature 2
- [] Feature 3
    - [] Nested Feature

<p align="right">(<a href="#top">back to top</a>)</p>



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



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/alvaro-alonso/taia-x.svg?style=for-the-badge
[contributors-url]: https://github.com/taia-x/taia-x/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/alvaro-alonso/taia-x.svg?style=for-the-badge
[forks-url]: https://github.com/taia-x/taia-x/network/members
[stars-shield]: https://img.shields.io/github/stars/alvaro-alonso/taia-x.svg?style=for-the-badge
[stars-url]: https://github.com/taia-x/taia-x/stargazers
[issues-shield]: https://img.shields.io/github/issues/alvaro-alonso/taia-x.svg?style=for-the-badge
[issues-url]: https://github.com/taia-x/taia-x/issues
[license-shield]: https://img.shields.io/github/license/alvaro-alonso/taia-x.svg?style=for-the-badge
[license-url]: https://github.com/taia-x/taia-x/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
