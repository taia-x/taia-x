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
        token_id
        timestamp
        recipient_id
        price
        ophash
        level
        id
        event_type
        caller_id
      }
      artifact_uri
      creator_id
      description
      files
      formats
      id
      price
      metadata
      name
      tags
      timestamp
    }
  }
`;
