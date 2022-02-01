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
      creator_id
      id
      description
      files
      cert_state
      name
      price
      tags
      artifact_uri
      formats
      metadata
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

export const getEventsByAccount = gql`
  query getEventsByAccount($accountId: String) {
    event(
      where: {
        _or: [
          { caller_id: { _eq: $accountId } }
          { recipient_id: { _eq: $accountId } }
        ]
      }
    ) {
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

export const getFilteredTokenMetadata = (where: string) => gql`
  query getFilteredTokenMetadata {
    token(where: { metadata: { _is_null: false }, _and: ${where} }) {
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
