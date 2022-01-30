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

export const getSingleCreator = gql`
  query getSingleCreator($creatorId: String) {
    event(
      where: {
        _or: [
          { caller_id: { _eq: $creatorId } }
          { recipient_id: { _eq: $creatorId } }
        ]
      }
    ) {
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
    token(
      where: {
        metadata: { _is_null: false }
        _and: { creator_id: { _eq: $creatorId } }
      }
      order_by: { timestamp: desc }
    ) {
      creator_id
      id
      name
      tags
      metadata
    }
  }
`;