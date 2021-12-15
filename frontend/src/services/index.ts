import WalletInterface from "./WalletInterface";
import TezosInterface from "./TezosInterface";
import IpfsInterface from "./IpfsInterface";

let walletInterface: WalletInterface;
let tezosInterface: TezosInterface;
let ipfsInterface: IpfsInterface;

const initInterfaces = async (): Promise<void> => {
  walletInterface = new WalletInterface();
  const { Tezos } = walletInterface;
  ipfsInterface = new IpfsInterface();
  ipfsInterface.init();
  tezosInterface = await TezosInterface.initialize(Tezos);
};

export { walletInterface, tezosInterface, ipfsInterface };
export default initInterfaces;
