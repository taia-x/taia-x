import { ContractAbstraction, TezosToolkit, Wallet } from "@taquito/taquito";
import { CONTRACT } from "@/constants";
import { NFT, AddRoleData, RemoveRoleData } from "@/types";

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
      const op = await this.contract.methods.user_manager(roleData).send();
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
      throw new Error(`Unable to assign roles!`);
    }
  }

  /**
   * fetch nft token from tezos blockchain
   */
  async fetchNfts(): Promise<any> {
    try {
      const storage: any = await this.contract.storage();
      const datasetIds = storage["market"].datasetIds;
      if (datasetIds) {
        const tokenIds: number[] = datasetIds.map((token: any) => token.c[0]);
        const nfts: Array<NFT> = await Promise.all(
          tokenIds.map(async (tokenId) => {
            const [tokenRaw, metadata] = await Promise.all([
              storage.market.datasets.get(tokenId.toString()), // get dataset for a token id
              storage.token_metadata.get(tokenId.toString()), // get metadata for a token id
            ]);
            const nft: NFT = {
              owner: tokenRaw.owner,
              id: tokenRaw.id.c[0],
              isOwned: tokenRaw.isOwned,
              onSale: tokenRaw.onSale,
              price: tokenRaw.price,
              metadataUri: Buffer.from(
                metadata.token_info.get("token_metadata_uri").substring(12),
                "hex"
              ).toString(), // convert bytes to string and strip off some hex numbers which are not needed
            };
            return nft;
          })
        );
        return nfts;
      }
    } catch (e) {
      throw new Error(`Unable to fetch nft's from contract: ${CONTRACT}!`);
    }
  }

  /**
   * mint nft token on tezos blockchain
   * @param address tezos account address
   * @param metadataUri ipfs metadata uri formatted as https://ipfs.io/{CID}
   */
  async mintNft(address: string, metadataUri: string): Promise<void> {
    try {
      const op = await this.contract.methods
        .mint("tz1ittpFnVsKxx1M8YPKt7VJEaZfwiBZ6jo7", address, metadataUri)
        .send();
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
      throw new Error(`Unable to mint token for address ${address}!`);
    }
  }
}

export default TezosInterface;
