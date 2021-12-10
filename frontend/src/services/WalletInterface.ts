import { BeaconWallet } from "@taquito/beacon-wallet";
import { TezosToolkit } from "@taquito/taquito";
import { AccountInfo, Network, NetworkType } from "@airgap/beacon-sdk";
import { GRANADANET_NODE_URL, CUSTOM_NODE_URL } from "@/constants";

export let wallet: BeaconWallet | undefined;

/**
 * exposes an interface for interaction with the wallet
 */
class WalletInterface {
  private network: Network;
  readonly Tezos: TezosToolkit;

  constructor() {
    this.network = { type: NetworkType.CUSTOM };
    this.Tezos = new TezosToolkit(GRANADANET_NODE_URL);
  }

  /**
   * function to check if wallet instance exists or otherwise instantiates wallet
   *
   * @returns beacon wallet instance
   */
  async getWallet(): Promise<BeaconWallet> {
    if (!wallet) {
      wallet = new BeaconWallet({ name: "Taia-X" });
      this.Tezos.setWalletProvider(wallet);
    }
    return wallet;
  }

  /**
   * function to connect to the wallet and perhaps request permissions for interaction with the frontend if not already done
   */
  async connectWallet(): Promise<void> {
    try {
      const wallet = await this.getWallet();
      if (await wallet?.client.getActiveAccount()) {
        return;
      }
      await wallet.requestPermissions({
        network: {
          type: NetworkType.CUSTOM,
          rpcUrl: CUSTOM_NODE_URL,
        },
      });
    } catch (e) {
      console.log(e);
    }
  }

  /**
   * function to get the tezos address of the current tezos account
   *
   * @returns tezos acount address
   */
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

  /**
   * function to get the balance of the current tezos account
   *
   * @returns tezos account balance
   */
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

  /**
   * function to disconnect from wallet and clear active account
   */
  async disconnectWallet(): Promise<void> {
    try {
      const wallet = await this.getWallet();
      await wallet?.clearActiveAccount();
    } catch (e) {
      console.log(e);
    }
  }
}

export default WalletInterface;
