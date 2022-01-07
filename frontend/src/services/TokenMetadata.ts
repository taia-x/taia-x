import {
  HttpLink,
  split,
  InMemoryCache,
  ApolloClient,
} from "@apollo/client/core";
import { WebSocketLink } from "@apollo/client/link/ws";
import { getMainDefinition } from "@apollo/client/utilities";
import { HTTP_METADATA_API_URL, WS_METADATA_API_URL } from "@/constants";

// create an http link:
const httpLink = new HttpLink({
  uri: HTTP_METADATA_API_URL,
});

// create a WebSocket link:
const wsLink = new WebSocketLink({
  uri: WS_METADATA_API_URL,
  options: {
    reconnect: true,
  },
});

// cache implementation
const cache = new InMemoryCache();

// using the ability to split links, you can send data to each link
// depending on what kind of operation is being sent
const link = split(
  // split based on operation type
  ({ query }) => {
    const definition = getMainDefinition(query);
    return (
      definition.kind === "OperationDefinition" &&
      definition.operation === "subscription"
    );
  },
  wsLink,
  httpLink
);

// create the apollo client
export const tokenMetadataClient = new ApolloClient({
  link,
  cache,
});
