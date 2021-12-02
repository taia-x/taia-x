import { TezosToolkit } from "@taquito/taquito";
import { IAM_CONTRACT_ADDRESS } from "@/constants";

/**
 * exposes an interface for interaction with the role smart contract
 */
class IamInterface {
  private Tezos: TezosToolkit;

  /**
   * constructor to set Tezos Toolkit instance
   * @param Tezos Tezos Toolkit instance from wallet interface
   */
  constructor(Tezos: TezosToolkit) {
    this.Tezos = Tezos;
  }

  /**
   * function to call entrypoint on the role smart contract which assigns a specified role to a tezos address
   * @param address tezos account address
   * @param role name of role ("certifier" || "provider" || "consumer")
   */
  async assignRole(address: string, role: string): Promise<void> {
    try {
      const contract = await this.Tezos.wallet.at(IAM_CONTRACT_ADDRESS);
      let op;
      switch (role) {
        case "certifier":
          op = await contract.methods.makeCertifier(address).send();
          break;
        case "provider":
          op = await contract.methods.makeProvider(address).send();
          break;
        case "consumer":
          op = await contract.methods.makeConsumer(address).send();
          break;
        default:
          break;
      }
      if (op) {
        const result = await op.confirmation(3);
        if (result.completed) {
          console.log("Transaction correctly processed!");
          console.log(`Block: ${result.block.header.level}`);
          console.log(`Chain ID: ${result.block.chain_id}`);
        } else {
          console.log("An error has occurred");
        }
      }
    } catch (e) {
      console.log(e);
    }
  }
}

export default IamInterface;
