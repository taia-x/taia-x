import { create } from "ipfs-http-client";
import { IPFS_GATEWAY_URL } from "@/constants";

type ipfsOptions = {
  host: string;
  port: number;
  protocol: "http" | "https";
};

/**
 * exposes an interface for interaction with ipfs
 */
class IpfsInterface {
  private ipfs: any;

  /**
   * constructor to set ipfs instance
   * @param options ipfs options for api node
   */
  constructor(options: ipfsOptions) {
    this.ipfs = create(options);
  }

  /**
   * write json file to ipfs
   * @param content the content to upload to ipfs
   * @returns cid to access the file on ipfs
   */
  async writeFile(content: any): Promise<string> {
    try {
      const { path } =
        content instanceof File
          ? await this.ipfs.add(content)
          : await this.ipfs.add(Buffer.from(JSON.stringify(content)));
      const cid = `ipfs://${path}`;
      return cid;
    } catch (e: any) {
      throw new Error(e.toString());
    }
  }

  /**
   * constructs an HTTP gateway url for the given IPFS uri
   * @param ipfsURI an ipfs:// uri
   * @returns gateway url to access ifps content via fetch request
   */
  makeGatewayURL(ipfsURI: string): string {
    if (ipfsURI.startsWith("ipfs://")) {
      return IPFS_GATEWAY_URL + "/" + ipfsURI.slice("ipfs://".length);
    }
    return ipfsURI;
  }
}

export default IpfsInterface;
