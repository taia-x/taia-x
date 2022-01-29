import { ContractAbstraction, TezosToolkit, Wallet } from "@taquito/taquito";
import { CONTRACT } from "@/constants";
import { AddRoleData, RemoveRoleData, MintParams } from "@/types";
import { char2Bytes } from "@taquito/utils";

/**
 * exposes an interface for interaction with the role smart contract
 */
class TezosInterface {
  private contract: ContractAbstraction<Wallet>;

  /**
   * constructor to set Tezos Toolkit instance
   * @param Tezos Tezos Toolkit instance from wallet interface
   */
  private constructor(contract: ContractAbstraction<Wallet>) {
    this.contract = contract;
  }

  /**
   * static function that replaces constructor to initialize contract instance
   * @param Tezos tezos instance
   */
  static async initialize(Tezos: TezosToolkit): Promise<TezosInterface> {
    const contract = await Tezos.wallet.at(CONTRACT);
    return new TezosInterface(contract);
  }

  /**
   * call entrypoint on the role smart contract which assigns a specified role to a tezos address
   * @param address tezos account address
   * @param role name of role ("certifier" || "provider" || "consumer")
   */
  async manageRoles(
    data: AddRoleData | RemoveRoleData | Array<AddRoleData | RemoveRoleData>
  ): Promise<void> {
    const roleData = Array.isArray(data) ? data : [data];
    try {
      const op = await this.contract.methods.update_user_roles(roleData).send();
      if (op) {
        const result = await op.confirmation(1);
        if (result.completed) {
          console.log("Transaction correctly processed!");
          console.log(`Block: ${result.block.header.level}`);
          console.log(`Chain ID: ${result.block.chain_id}`);
        } else {
          console.log("An error has occurred");
        }
      }
    } catch (e: any) {
      throw new Error(e.toString());
    }
  }

  /**
   * mint nft token on tezos blockchain
   * @param address tezos account address
   * @param metadataUri ipfs metadata uri formatted as ipfs//{CID}
   */
  async mintNft(mintParams: MintParams): Promise<void> {
    const { hash, operator, address, price, metadataUri } = mintParams;
    console.log(price);
    try {
      const op = await this.contract.methods
        .mint(hash, operator, address, price, char2Bytes(metadataUri))
        .send();
      if (op) {
        const result = await op.confirmation(1);
        if (result.completed) {
          console.log("Transaction correctly processed!");
          console.log(`Block: ${result.block.header.level}`);
          console.log(`Chain ID: ${result.block.chain_id}`);
        } else {
          console.log("An error has occurred");
        }
      }
    } catch (e: any) {
      throw new Error(e.toString());
    }
  }

  /**
   * buy nft token on tezos blockchain
   * @param address tezos account address
   * @param metadataUri ipfs metadata uri formatted as https://ipfs.io/{CID}
   */
  async buy(price: number, tokenId: number): Promise<void> {
    try {
      const op = await this.contract.methods
        .buy(tokenId)
        .send({ amount: price, mutez: true });
      if (op) {
        const result = await op.confirmation(1);
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
      throw new Error(`Unable to buy token with token_id ${tokenId}!`);
    }
  }
}

export default TezosInterface;
