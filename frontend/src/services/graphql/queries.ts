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
      hash
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
  subscription SubscribeToTokenEvent($token_id: bigint = 1) {
    event(where: { token_id: { _eq: $token_id } }) {
      _from_id
      event_type
      id
      level
      ophash
      price
      _to_id
      timestamp
      token_id
    }
  }
`;

export const getEventsByAccount = gql`
  query GetEventsByAccount($accountId: String) {
    event(
      where: {
        _or: [
          { _from_id: { _eq: $accountId } }
          { _to_id: { _eq: $accountId } }
        ]
      }
      order_by: { timestamp: desc }
    ) {
      _from_id
      event_type
      id
      level
      ophash
      price
      _to_id
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

export const getCreations = gql`
  query GetCreations($address: String = "") {
    account_by_pk(address: $address) {
      creations {
        creator_id
        id
        description
        files
        cert_state
        name
        price
      }
    }
  }
`;

export const getPurchases = gql`
  query GetPurchases($address: String = "") {
    account_by_pk(address: $address) {
      purchases {
        creator_id
        id
        description
        files
        cert_state
        name
        price
        hash
        artifact_uri
      }
    }
  }
`;
