import WalletInterface from "./WalletInterface";
import IamInterface from "./IamInterface";
import IpfsInterface from "./IpfsInterface";

const walletInterface = new WalletInterface();
const { Tezos } = walletInterface;
const iamInterface = new IamInterface(Tezos);
const ipfsInterface = new IpfsInterface();
ipfsInterface.init();

export { walletInterface, iamInterface, ipfsInterface };
