import { BeaconWallet } from "@taquito/beacon-wallet";
import { TezosToolkit } from "@taquito/taquito";
import { AccountInfo, Network, NetworkType } from "@airgap/beacon-sdk";

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

export const connectWallet = async (): Promise<BeaconWallet | undefined> => {
  try {
    const wallet = await getWallet();
    if (await wallet.client.getActiveAccount()) {
      return wallet;
    }

    // Send permission request to the connected wallet. This will either be the browser extension, or a wallet over the P2P network.
    await wallet.requestPermissions({ network });

    return wallet;
  } catch (e) {
    console.log(e);
  }
};

export const getAddress = async (): Promise<string | undefined> => {
  try {
    const wallet = await getWallet();
    const account = (await wallet.client.getActiveAccount()) as AccountInfo;
    //const address = await wallet.getPKH();
    return account.address;
  } catch (e) {
    console.log(e);
  }
};

export const getBalance = async (): Promise<number | undefined> => {
  try {
    if (typeof Tezos !== undefined) {
      const address = (await getAddress()) as string;
      const balance = await Tezos.tz.getBalance(address);
      return balance.toNumber();
    }
  } catch (e) {
    console.log(e);
  }
};

export const disconnectWallet = async (): Promise<void> => {
  try {
    const wallet = await getWallet();
    await wallet.clearActiveAccount();
  } catch (e) {
    console.log(e);
  }
};
