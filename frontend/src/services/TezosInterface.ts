import { BeaconWallet } from "@taquito/beacon-wallet";
import { TezosToolkit } from "@taquito/taquito";
import { AccountInfo, Network, NetworkType } from "@airgap/beacon-sdk";
import { GRANADANET_NODE_URL } from "@/constants";

let wallet: BeaconWallet | undefined;

class TezosInterface {
  private network: Network;
  private Tezos: TezosToolkit;

  constructor() {
    this.network = { type: NetworkType.GRANADANET };
    this.Tezos = new TezosToolkit(GRANADANET_NODE_URL);
  }

  async getWallet(): Promise<BeaconWallet> {
    if (!wallet) {
      wallet = new BeaconWallet({ name: "Taia-X" });
      this.Tezos.setWalletProvider(wallet);
    }
    return wallet;
  }

  async connectWallet(): Promise<void> {
    try {
      const wallet = await this.getWallet();
      if (await wallet?.client.getActiveAccount()) {
        return;
      }
      await wallet.requestPermissions({ network: this.network });
    } catch (e) {
      console.log(e);
    }
  }

  async getAddress(): Promise<string> {
    try {
      const wallet = await this.getWallet();
      const account = (await wallet?.client.getActiveAccount()) as AccountInfo;
      if (account) return account.address;
    } catch (e) {
      console.log(e);
    }
    return "";
  }

  async getBalance(): Promise<number> {
    try {
      if (typeof this.Tezos !== undefined && typeof wallet !== undefined) {
        const address = await this.getAddress();
        if (address) {
          const balance = await this.Tezos.tz.getBalance(address);
          if (balance) return balance.toNumber();
        }
      }
    } catch (e) {
      console.log(e);
    }
    return 0;
  }

  async disconnectWallet(): Promise<void> {
    try {
      const wallet = await this.getWallet();
      await wallet?.clearActiveAccount();
    } catch (e) {
      console.log(e);
    }
  }
}

export default TezosInterface;
