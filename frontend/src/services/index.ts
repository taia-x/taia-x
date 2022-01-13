import WalletInterface from "./WalletInterface";
import TezosInterface from "./TezosInterface";
import IpfsInterface from "./IpfsInterface";
import { IPFS_API_PROTOCOL, IPFS_API_HOST, IPFS_API_PORT } from "@/constants";

let tezosInterface: TezosInterface;

const walletInterface = new WalletInterface();
const { Tezos } = walletInterface;
const ipfsInterface = new IpfsInterface({
  host: IPFS_API_HOST,
  port: IPFS_API_PORT,
  protocol: IPFS_API_PROTOCOL,
});

const initInterfaces = async (): Promise<void> => {
  tezosInterface = await TezosInterface.initialize(Tezos);
};

export { walletInterface, tezosInterface, ipfsInterface };
export default initInterfaces;
