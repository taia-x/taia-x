import gql from "graphql-tag";

export const getTokenMetadata = gql`
  query GetAllTokenMetadata($offset: Int = 0, $limit: Int = 12) {
    token(
      where: { metadata: { _is_null: false } }
      limit: $limit
      order_by: { timestamp: desc }
      offset: $offset
    ) {
      creator_id
      id
      name
      tags
      metadata
    }
  }
`;

export const getSingleTokenMetadata = gql`
  query GetSingleTokenMetadata($id: bigint = 1) {
    token_by_pk(id: $id) {
      events {
        creator_id
        event_type
        level
        ophash
        price
        timestamp
        id
        recipient_id
        token_id
      }
      artifact_uri
      creator_id
      description
      files
      formats
      id
      metadata
      name
      tags
      timestamp
    }
  }
`;
