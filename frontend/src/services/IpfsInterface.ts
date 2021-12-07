import { create as createIpfs } from "ipfs-core";
import { IPFS_GATEWAY_URL } from "@/constants";
import all from "it-all";

async function* streamAsyncIterable(stream: any) {
  const reader = stream.getReader();
  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) {
        return;
      }
      yield value;
    }
  } finally {
    reader.releaseLock();
  }
}

/**
 * exposes an interface for interaction with ipfs
 */
class IpfsInterface {
  private ipfs: any;

  /**
   * function to initialize the ipfs instance
   */
  async init(): Promise<void> {
    try {
      this.ipfs = await createIpfs();
    } catch (e) {
      throw Error("Failed to initialize ipfs instance!");
    }
  }

  async writeFile(data: any, path: string) {
    const { cid: assetCid } = await this.ipfs.add({
      path,
      content: JSON.stringify(data),
    });

    const assetURI = path
      ? this.ensureIpfsUriPrefix(assetCid) + "/" + path
      : this.ensureIpfsUriPrefix(assetCid);

    await this.getFile(assetCid);

    return {
      assetURI,
      metadataGatewayURL: this.makeGatewayURL(assetURI),
    };
  }

  async getFile(cid: any) {
    async function readJsonFromAsyncIterable(readable: any) {
      const uint8array: any = await all(readable);

      const asText: any = new Promise((resolve, reject) => {
        const fr = new FileReader();
        fr.onload = () => resolve(fr.result);
        fr.onerror = reject;
        fr.readAsText(new Blob(uint8array));
      });

      return JSON.parse(await asText());
    }

    const file = await readJsonFromAsyncIterable(this.ipfs.cat(cid));
    console.log("file", file);
  }

  /**
   * @param cidOrURI either a CID string, or a URI string of the form `ipfs://${cid}`
   * @returns input string with the `ipfs://` prefix stripped off
   */
  stripIpfsUriPrefix(cidOrURI: string): string {
    if (cidOrURI.startsWith("ipfs://")) {
      return cidOrURI.slice("ipfs://".length);
    }
    return cidOrURI;
  }

  ensureIpfsUriPrefix(cidOrURI: string): string {
    let uri = cidOrURI.toString();
    if (!uri.startsWith("ipfs://")) {
      uri = "ipfs://" + cidOrURI;
    }
    // Avoid the Nyan Cat bug (https://github.com/ipfs/go-ipfs/pull/7930)
    if (uri.startsWith("ipfs://ipfs/")) {
      uri = uri.replace("ipfs://ipfs/", "ipfs://");
    }
    return uri;
  }

  /**
   * Return an HTTP gateway URL for the given IPFS object.
   * @param ipfsURI an ipfs:// uri or CID string
   * @returns a url to view the IPFS object on the configured gateway.
   */
  makeGatewayURL(ipfsURI: string): string {
    return IPFS_GATEWAY_URL + "/" + this.stripIpfsUriPrefix(ipfsURI);
  }

  // /**
  //  * Helper to construct metadata JSON for
  //  * @param string assetCid - IPFS URI for the NFT asset
  //  * @param object options
  //  * @returns metadata object of asset
  //  */
  // async makeAssetMetadata(metadata: any, path: string) {
  //    const { cid: metadataCid } = await this.writeFile(metadata, path)
  //   this.ipfs.add({
  //     path: "/nft/metadata.json",
  //     content: JSON.stringify(metadata),
  //   });
  //   const metadataURI =
  //     this.ensureIpfsUriPrefix(metadataCid) + "/metadata.json";
  //   return {
  //     name,
  //     description,
  //     image: assetURI,
  //   };
  // }
}

export default IpfsInterface;
