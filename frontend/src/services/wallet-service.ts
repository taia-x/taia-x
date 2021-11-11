import { BeaconWallet } from "@taquito/beacon-wallet";
import { TezosToolkit } from "@taquito/taquito";
import { AccountInfo, Network, NetworkType } from "@airgap/beacon-sdk";
import { BigNumber } from "bignumber.js";

const Tezos = new TezosToolkit("https://granadanet.api.tez.ie");
const network: Network = { type: NetworkType.GRANADANET };

let wallet: BeaconWallet | undefined;

const getWallet = async () => {
  if (!wallet) {
    wallet = new BeaconWallet({ name: "Taia-X" });
    Tezos.setWalletProvider(wallet);
  }

  return wallet;
};

export const connectWallet = async (): Promise<void> => {
  try {
    const wallet = await getWallet();
    if (await wallet.client.getActiveAccount()) {
      return;
    }
    await wallet.requestPermissions({ network });
  } catch (e) {
    console.log(e);
  }
};

export const getAddress = async (): Promise<string> => {
  try {
    const wallet = await getWallet();
    const account = (await wallet.client.getActiveAccount()) as AccountInfo;
    //const address = await wallet.getPKH();
    return account.address;
  } catch (e) {
    console.log(e);
  }
  return "";
};

export const getBalance = async (): Promise<number> => {
  try {
    if (typeof Tezos !== undefined) {
      const address = (await getAddress()) as string;
      const balance = await Tezos.tz.getBalance(address);
      if (balance) return balance.toNumber();
    }
  } catch (e) {
    console.log(e);
  }
  return 0;
};

export const disconnectWallet = async (): Promise<void> => {
  try {
    const wallet = await getWallet();
    await wallet.clearActiveAccount();
  } catch (e) {
    console.log(e);
  }
};

export const getContractStorage = async (): Promise<BigNumber> => {
  const contract = await Tezos.contract.at(
    "KT1WSAFm8PzQPhj5wBFRfneTL8smSaJ45BLt"
  );
  const storage: BigNumber = await contract.storage();
  return storage;
};

export const increment = async (): Promise<void> => {
  try {
    const contract = await Tezos.wallet.at(
      "KT1WSAFm8PzQPhj5wBFRfneTL8smSaJ45BLt"
    );
    const op = await contract.methods.increment(5).send();
    if (op) {
      console.log(`Hash: ${op.opHash}`);
      const result = await op.confirmation(3);
      if (result.completed) {
        console.log(`Transaction correctly processed!
      Block: ${result.block.header.level}
      Chain ID: ${result.block.chain_id}`);
      } else {
        console.log("An error has occurred");
      }
    }
  } catch (e) {
    console.log(e);
  }
};
