import { TezosToolkit } from '@taquito/taquito';
import { InMemorySigner } from '@taquito/signer';


async function add_cert() {
    const provider = 'https://hangzhounet.api.tez.ie';
    const signer: any = new InMemorySigner('');
        const tezos = new TezosToolkit(provider);
    tezos.setSignerProvider( signer );
    try {
        console.log("signer pkh:");
        console.log(await signer.publicKeyHash());
        const contract = await tezos.contract.at('KT19XGiSVTRpS4oHJXRQ8eVUodk8yKDakMnY');
        console.log("Printing contract methods...");
        console.log(contract.methods);
        console.log("Showing initial storage...");
        console.log(await contract.storage())
        console.log(`Interacting with Smart Contract..`);
        console.log(`First show the signature of the method`);
        console.log(contract.methodsObject.save_cert().getSignature())
    } catch (ex) {
        console.log(ex)
    }
}

// tslint:disable-next-line: no-floating-promises
add_cert();