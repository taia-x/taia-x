#if !INTERFACE
#define INTERFACE


// Allowed roles, you can add a new annotation right here, for example 'Dev' or 'Moderator'
type role = Consumer | Certifier | Provider | NoRole 

type token = {
    hash: string;
}

type store = {
  datasets : (address, token) big_map;
  users : (address, role) big_map;
}

type return = operation list * store 

#endif