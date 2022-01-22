export interface NFT {
  owner: string;
  id: number;
  isOwned: boolean;
  onSale: boolean;
  price: null | number;
  metadataUri: string;
}

export interface MintParams {
  operator: string;
  address: string;
  price: number;
  metadataUri: string;
}

export interface AddRoleData {
  add_role: UserRoleMapping;
}

export interface RemoveRoleData {
  remove_role: UserRoleMapping;
}

interface UserRoleMapping {
  user: string;
  role: Role;
}
interface Role {
  provider?: boolean;
  consumer?: boolean;
}

export interface Alert {
  id: number;
  message: string;
  type: "info" | "warning" | "success" | "error";
  visible: boolean;
}

interface Format {
  uri: string;
  hash: string;
  mimeType: string;
}

interface Attribute {
  name: string;
  value: string;
}

interface Level {
  name: string;
  value: number;
}

interface Stat {
  name: string;
  value: number;
}

export interface TokenMetadata {
  name: string;
  owner: string;
  version?: number;
  tags: Array<string>;
  symbol: string;
  decimals: number;
  price: number;
  creators?: Array<string>;
  collection_id?: number;
  formats?: Array<Format>;
  attributes?: Array<Attribute>;
  levels?: Array<Level>;
  stats?: Array<Stat>;
  displayUri?: string;
  artifactUri: string;
  thumbnailUri?: string;
}
