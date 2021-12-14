import { create as createIpfs } from "ipfs-core";
import { IPFS_GATEWAY_URL } from "@/constants";

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

  /**
   * write json stringified object to ipfs
   * @param content the content to upload to ipfs
   * @returns gatewayUrl to access the file on ipfs
   */
  async writeFile(
    content: any
  ): Promise<{ assetURI: string; gatewayUrl: string }> {
    const { cid: assetCid } = await this.ipfs.add({
      content: JSON.stringify(content),
    });

    const assetURI = this.ensureIpfsUriPrefix(assetCid);

    return { assetURI, gatewayUrl: this.makeGatewayURL(assetURI) };
  }

  /**
   * stript ipfs uri prefix
   * @param cidOrURI either a CID string, or a URI string of the form `ipfs://${cid}`
   * @returns input string with the `ipfs://` prefix stripped off
   */
  stripIpfsUriPrefix(cidOrURI: string): string {
    if (cidOrURI.startsWith("ipfs://")) {
      return cidOrURI.slice("ipfs://".length);
    }
    return cidOrURI;
  }

  /**
   * ensures to have an IPFS prefix before CID
   * @param cidOrURI either a CID string, or a URI string of the form `ipfs://${cid}`
   * @returns ipfs uri
   */
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
   * constructs an HTTP gateway url for the given IPFS uri
   * @param ipfsURI an ipfs:// uri or CID string
   * @returns a ipfs gateway url
   */
  makeGatewayURL(ipfsURI: string): string {
    return IPFS_GATEWAY_URL + "/" + this.stripIpfsUriPrefix(ipfsURI);
  }
}

export default IpfsInterface;
