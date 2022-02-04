const { TezosToolkit } = require("@taquito/taquito");
const { importKey } = require("@taquito/signer");
const migrate = require("../migration/1_initial_migration");
const fs = require("fs");
const path = require("path");

require("dotenv").config({ path: path.resolve(__dirname, "../.env") });
const SANDBOX_URL = "http://127.0.0.1:20000";
const TESTNET_URL = "https://rpc.tzkt.io/hangzhou2net";


const deploy = async () => {
  const mode = process.argv[2] || "sandbox";
  console.log(">>> Deploy with mode:", mode);
  
  var Tezos;
  try {
    if (mode === "sandbox") {
      const ALICE_SECRET = process.env.ALICE_SECRET;
      Tezos = new TezosToolkit(SANDBOX_URL);
      await importKey(Tezos, ALICE_SECRET)
    } else {
      const FAUCET = JSON.parse(process.env.FAUCET);
      const { email, password, mnemonic, secret } = FAUCET;
      Tezos = new TezosToolkit(TESTNET_URL);
      await importKey(Tezos, email, password, mnemonic.join(" "), secret);
    }
    
    const code = fs
      .readFileSync(path.resolve(__dirname, "../contracts/src/taia_x_main.mligo"))
      .toString();
    console.log("Originate...");

    const initial_storage = await migrate(Tezos);

    const op = await Tezos.contract.originate({
      code,
      storage: initial_storage,
    });

    console.log("Awaiting confirmation...");
    const contract = await op.contract();
    console.log("Deployment successful!");
    console.log(">>> Gas used:", op.consumedGas);
    console.log(">>> Operation hash:", op.hash);
    console.log(">>> Contract address:", op.contractAddress);
  } catch (error) {
    console.error(error);
  }
};

deploy();
