const { TezosToolkit } = require("@taquito/taquito");
const { importKey } = require("@taquito/signer");
const migrate = require("../migration/1_initial_migration");

const fs = require("fs");
const path = require('path')

require('dotenv').config({ path: path.resolve(__dirname, '../../.env') })

const SANDBOX_URL = "http://127.0.0.1:20000";
const TESTNET_URL = "https://rpc.tzkt.io/hangzhou2net";

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

    const code = fs.readFileSync(path.resolve(__dirname, '../contracts/out/taia_x_main.tz')).toString();
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
