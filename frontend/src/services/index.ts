import WalletInterface from "./WalletInterface";
import TezosInterface from "./TezosInterface";
import IpfsInterface from "./IpfsInterface";
import { IPFS_API_PROTOCOL, IPFS_API_HOST, IPFS_API_PORT } from "@/constants";

let walletInterface: WalletInterface;
let tezosInterface: TezosInterface;
let ipfsInterface: any;

const initInterfaces = async (): Promise<void> => {
  walletInterface = new WalletInterface();
  const { Tezos } = walletInterface;
  ipfsInterface = new IpfsInterface({
    host: IPFS_API_HOST,
    port: IPFS_API_PORT,
    protocol: IPFS_API_PROTOCOL,
  });
  tezosInterface = await TezosInterface.initialize(Tezos);
};

export { walletInterface, tezosInterface, ipfsInterface };
export default initInterfaces;
