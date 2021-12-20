import gql from "graphql-tag";

export const getTokenMetadata = gql`
  query ($offset: Int, $limit: Int) {
    token_metadata(
      order_by: { updated_at: desc }
      offset: $offset
      limit: $limit
      where: { metadata: { _has_key: "assetUri" } }
    ) {
      id
      metadata
      token_id
      created_at
      link
      updated_at
    }
  }
`;

export const getSingleTokenMetadata = gql`
  query ($id: bigint = 1) {
    token_metadata_by_pk(id: $id) {
      id
      metadata
      token_id
      created_at
      link
      updated_at
    }
  }
`;
