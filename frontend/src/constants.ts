export const CUSTOM_NODE_URL = "http://localhost:20000"; // Testnet: "https://granadanet.api.tez.ie";

type HTTP = "http" | "https";

export const CONTRACT =
  process.env.VUE_APP_CONTRACT_ADDRESS ||
  "KT1Gd4FXMY3uDE7xRNd1hTnFYizMNYwLBkLh";
console.log(process.env.VUE_APP_CONTRACT_ADDRESS);

// Roles
export const ROLE_CERTIFIER = "certifier";
export const ROLE_PROVIDER = "provider";
export const ROLE_CONSUMER = "consumer";

// IPFS
export const IPFS_API_PROTOCOL =
  (process.env.VUE_APP_IPFS_API_PROTOCOL as HTTP) || "http";
export const IPFS_API_HOST = process.env.VUE_APP_IPFS_API_HOST || "localhost";
export const IPFS_API_PORT =
  parseInt(<string>process.env.VUE_APP_IPFS_API_PORT, 10) || 5001;
export const IPFS_GATEWAY_URL =
  process.env.VUE_APP_IPFS_GATEWAY_URL || "http://localhost:8081/ipfs";

// GraphQL
export const HTTP_METADATA_API_URL =
  process.env.VUE_APP_HTTP_METADATA_API_URL ||
  "http://localhost:42000/v1/graphql";
export const WS_METADATA_API_URL =
  process.env.VUE_APP_WS_METADATA_API_URL || "ws://localhost:42000/v1/graphql";
