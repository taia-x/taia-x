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
      description
      files
      cert_state
      name
      price
      tags
    }
  }
`;

export const getSingleTokenMetadata = gql`
  query GetSingleTokenMetadata($id: bigint = 1) {
    token_by_pk(id: $id) {
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

export const subscribeToTokenEvent = gql`
  subscription MySubscription($token_id: bigint = 1) {
    event(where: { token_id: { _eq: $token_id } }) {
      caller_id
      event_type
      id
      level
      ophash
      price
      recipient_id
      timestamp
      token_id
    }
  }
`;
