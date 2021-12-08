const { TezosToolkit, MichelsonMap } = require("@taquito/taquito");
const { importKey } = require("@taquito/signer");
const web3 = require("web3");

const fs = require("fs");
require("dotenv").config();

const SANDBOX_URL = "http://127.0.0.1:20000";
const TESTNET_URL = "https://granadanet.api.tez.ie";
const FAUCET = JSON.parse(process.env.FAUCET);
const ALICE_SECRET = process.env.ALICE_SECRET;

const deploy = async () => {
  const mode = process.argv[2] || "sandbox";
  console.log(">>> Deploy with mode:", mode);

  try {
    const Tezos = new TezosToolkit(
      mode === "sandbox" ? SANDBOX_URL : TESTNET_URL
    );

    // Signing on testnet mode needs different parameters as on sandbox mode
    const { email, password, mnemonic, secret } = FAUCET;
    mode === "sandbox"
      ? await importKey(Tezos, ALICE_SECRET)
      : await importKey(Tezos, email, password, mnemonic.join(" "), secret);

    const admin = await Tezos.signer.publicKeyHash();
    const empty_datasets = new MichelsonMap();
    const empty_sales = [];
    const empty_dataset_ids = [];
    const empty_owners = new MichelsonMap();
    const empty_users = new MichelsonMap();

    const market = {
      admin: admin,
      sales: empty_sales,
      datasets: empty_datasets,
      datasetIds: empty_dataset_ids,
      nextDatasetId: 0,
      owners: empty_owners,
      users: empty_users,
    };

    const metadata = new MichelsonMap();
    const token_info = new MichelsonMap();
    const token_metadata = new MichelsonMap();
    const empty_ledger = new MichelsonMap();
    const empty_operators = new MichelsonMap();

    // Set TZIP-16 contract metadata, with a JSON Blob
    metadata.set(
      "",
      web3.utils
        .asciiToHex(
          "sha256://0x19faf07472cc91927ff455a82c0d51a682164b3b18125e6a5b1763a14f09a60c/https:%2F%2Ftezosdataset.io%2Fmetadata%2Fcontract_metadata.json"
        )
        .slice(2)
    );

    // Set TZIP-16 token metadata with a JSON Blob
    // token_info.set(
    //     "", web3.utils.asciiToHex("https://ipfs.io/ipfs/QmZKJKce6Y9yyuPvatGZuqsvY3dYd6TH6qt9AsTW22xtgq").slice(2)
    // );

    // Set TZIP-12 token metadata, in the token_metadata big map
    // token_info.set(
    //     "symbol", web3.utils.asciiToHex("TLD").slice(2)
    // );
    // token_info.set(
    //     "name", web3.utils.asciiToHex("Tezosdataset").slice(2)
    // );
    // token_info.set(
    //     "decimals", web3.utils.asciiToHex("0").slice(2)
    // );
    // token_info.set(
    //     "thumbnailUri", web3.utils.asciiToHex("https://tezosdataset.io/logo512.png").slice(2)
    // );

    // token_metadata.set(
    //     1, {
    //     token_info: token_info,
    //     token_id: 1
    // }
    // );

    const initial_storage = {
      market: market,
      ledger: empty_ledger,
      operators: empty_operators,
      metadata: metadata,
      token_metadata: token_metadata,
    };

    const code = fs.readFileSync("./contracts/out/taia_x_main.tz").toString();
    console.log("Originate...");

    const op = await Tezos.contract.originate({
      code,
      storage: initial_storage,
    });

    console.log("Awaiting confirmation...");
    const contract = await op.contract();
    console.log("Deployment successful!");
    console.log(">>> Gas used:", op.consumedGas);
    console.log(">>> Storage:", await contract.storage());
    console.log(">>> Operation hash:", op.hash);
  } catch (error) {
    console.error(error);
  }
};

deploy();
