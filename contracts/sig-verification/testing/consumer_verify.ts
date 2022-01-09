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
        console.log(contract.methodsObject.verifySig3().getSignature())
        console.log(`Now send a test transaction..`);
        contract.methodsObject.verifySig3({
            pbk: 'edpktz4dr5yhgw56ZmJ2V8SqMsg3o13bjgZimJcbvqmBrcFYwnLyYW',
            provider_sig:  'edsigtym57ZmmpZBAyP5mimwrs7ioh6U2D8t2s4surG4L2q6zyaBGBC9hKt6k7zNbYgvfp7GM8ULHYgJviTRzgoUMNM8Cc71rWK'
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