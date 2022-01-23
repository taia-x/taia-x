import { TezosToolkit } from '@taquito/taquito';
import { InMemorySigner } from '@taquito/signer';


async function verify_sig() {
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
        console.log(contract.methodsObject.verifySig1().getSignature())
        console.log(`Now send a test transaction..`);
        contract.methodsObject.verifySig1({
            message_packed: '6d6279746573',
            pbk: 'edpkuYzXL37pTYVHu7rTodeyH9bQ2rfDKadWqqGCqL8m8G1W4UH55E',
            provider_sig:  'edsigtffaz6wutLRzi7Ni15KPcoUZULJiyF3tHX78iBp17Fdt4jTTDmJjVe6QfK8ggimYGDcv7bLFziMPKSP2JxG5sb8NGKZcQG'
        }).send().then((op) => {
            console.log(`Awaiting for ${op.hash} to be confirmed...`);
             return op.confirmation().then(() => op.hash);
          }).then((hash) => console.log(`Operation injected: https://hangzhou.tzstats.com/${hash}`))
          .catch((error) => console.log(`Error: ${JSON.stringify(error, null, 2)}`))
    } catch (ex) {
        console.log(ex)
    }
}

// tslint:disable-next-line: no-floating-promises
verify_sig();