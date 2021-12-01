import WalletInterface from "./WalletInterface";
import IamInterface from "./IamInterface";

const walletInterface = new WalletInterface();
const { Tezos } = walletInterface;
const iamInterface = new IamInterface(Tezos);

export { walletInterface, iamInterface };
