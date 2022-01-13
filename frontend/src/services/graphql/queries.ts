import gql from "graphql-tag";

export const getTokenMetadata = gql`
  query GetAllTokenMetadata($offset: Int = 0, $limit: Int = 12) {
  token(where: {metadata: {_is_null: false}}, limit: $limit, order_by: {timestamp: desc}, offset: $offset) {
    id
    artifact_uri
    metadata
    name
    description
    timestamp
    creator_id
  }
}
`;

export const getSingleTokenMetadata = gql`
  query GetSingleTokenMetadata($id: bigint = 1) {
  token_by_pk(id: $id) {
    artifact_uri
    creator_id
    description
    id
    metadata
    name
    timestamp
  }
}
`;
