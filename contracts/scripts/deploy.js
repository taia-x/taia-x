const { TezosToolkit } = require("@taquito/taquito");
const { importKey, InMemorySigner } = require("@taquito/signer");
const fs = require("fs");

const deploy = async () => {
  const mode = process.argv[2] || "sandbox";
  console.log(">>> Deploy with mode:", mode);

  try {
    const config = JSON.parse(
      fs.readFileSync(`./config/${mode}.config.json`).toString()
    );

    const Tezos = new TezosToolkit(config.url);

    if (mode === "testnet") {
      const { email, password, mnemonic, secret } = config.faucet;
      await importKey(Tezos, email, password, mnemonic.join(" "), secret);
    } else {
      Tezos.setProvider({
        signer: await InMemorySigner.fromSecretKey(config.alice.secret),
      });
    }

    const code = fs.readFileSync("./build/counter.tz").toString();
    console.log("Originate");
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
