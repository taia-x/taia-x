import { BeaconWallet } from "@taquito/beacon-wallet";
import { TezosToolkit } from "@taquito/taquito";
import {
  NetworkType,
  RequestSignPayloadInput,
  SigningType,
} from "@airgap/beacon-sdk";
import { CUSTOM_NODE_URL } from "@/constants";
import { char2Bytes } from "@taquito/utils";

export let wallet: BeaconWallet | undefined;

/**
 * exposes an interface for interaction with the wallet
 */
class WalletInterface {
  readonly Tezos: TezosToolkit;

  constructor() {
    this.Tezos = new TezosToolkit(CUSTOM_NODE_URL);
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
      this.Tezos.setProvider({ wallet });
    } catch (e: any) {
      throw new Error(e.toString());
    }
  }

  /**
   * function to get the tezos address of the current tezos account
   *
   * @returns tezos acount address
   */
  async getAccount(): Promise<{ publicKey: string; address: string }> {
    try {
      const wallet = await this.getWallet();
      const activeAccount = await wallet.client.getActiveAccount();
      const { publicKey, address } = activeAccount as any;
      //await this.signMessage(1, "tz1TUEs5dubGJoCkvSK11zFqTWU9jh6cV8kb");
      // const signer = new InMemorySigner(
      //   "edsk3VdieyzxcsjFRxApVvLk8LQmQELiuJtGrww27WHamxF83dZwyY"
      // );
      // const bytes = char2Bytes("1");
      // const signature = await signer.sign(bytes);
      // console.log(signature);
      return { publicKey, address };
    } catch (e) {
      console.log(e);
      throw new Error("Unable to get tezos account address!");
    }
  }

  /**
   * function to sign a message via wallet
   *
   * @returns signature
   */
  async signMessage(
    token_id: number,
    address: string
  ): Promise<{ signature: string; payloadBytes: string }> {
    try {
      const wallet = await this.getWallet();
      //const ISO8601formatedTimestamp = new Date().toISOString();
      const input = String(token_id);
      // const formattedInput: string = [input].join(
      //   " "
      // );
      const bytes = char2Bytes(input);
      const payloadBytes = "05" + "01" + bytes;
      const payload: RequestSignPayloadInput = {
        signingType: SigningType.MICHELINE,
        payload: payloadBytes,
        sourceAddress: address,
      };
      const signedPayload = await wallet.client.requestSignPayload(payload);
      const { signature } = signedPayload;
      return { signature, payloadBytes };
    } catch (e) {
      throw new Error("Unable to get tezos account address!");
    }
  }

  /**
   * function to get the balance of the current tezos account
   *
   * @returns tezos account balance
   */
  // async getBalance(): Promise<number> {
  //   try {
  //     if (typeof this.Tezos !== undefined && typeof wallet !== undefined) {
  //       const address = await this.getAddress();
  //       if (address) {
  //         const balance = await this.Tezos.tz.getBalance(address);
  //         if (balance) return balance.toNumber();
  //       }
  //     }
  //   } catch (e: any) {
  //     throw new Error(e.toString());
  //   }
  //   return 0;
  // }

  /**
   * function to disconnect from wallet and clear active account
   */
  async disconnectWallet(): Promise<void> {
    try {
      const wallet = await this.getWallet();
      await wallet?.clearActiveAccount();
    } catch (e: any) {
      throw new Error(e.toString());
    }
  }
}

export default WalletInterface;
