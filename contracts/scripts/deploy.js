const { TezosToolkit } = require("@taquito/taquito");
const { importKey, InMemorySigner } = require("@taquito/signer");
const fs = require("fs");
require("dotenv").config();

const FAUCET = JSON.parse(process.env.FAUCET);
const { SANDBOX_URL, TESTNET_URL, ALICE_SECRET } = process.env;

const deploy = async () => {
  const mode = process.argv[2] || "sandbox";
  console.log(">>> Deploy with mode:", mode);

  try {
    const Tezos = new TezosToolkit(
      mode === "sandbox" ? SANDBOX_URL : TESTNET_URL
    );

    if (mode === "sandbox") {
      Tezos.setProvider({
        signer: await InMemorySigner.fromSecretKey(ALICE_SECRET),
      });
    } else {
      const { email, password, mnemonic, secret } = FAUCET;
      await importKey(Tezos, email, password, mnemonic.join(" "), secret);
    }

    const code = fs.readFileSync("./build/counter.tz").toString();
    console.log("Originate...");
    const op = await Tezos.contract.originate({
      code,
      init: `0`,
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
