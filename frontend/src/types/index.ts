export interface NftMetadata {
  name: string;
  description: string;
  price: number;
  tags: Array<string>;
  image: string;
  assetUri: string;
}

export interface OntologyMetadata {
  name: string;
  description: string;
}

export interface NFT {
  owner: string;
  id: number;
  isOwned: boolean;
  onSale: boolean;
  price: null | number;
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
  certifier?: boolean;
  provider?: boolean;
  consumer?: boolean;
}
