#if !INTERFACE
#define INTERFACE


// Allowed roles, you can add a new annotation right here, for example 'Dev' or 'Moderator'
type role is Consumer | Certifier | Provider | NoRole 

type token is record
  hash: string;
end  

type store is record
  datasets: big_map(address, token);
  users: big_map(address, role);
end

type return is list(operation) * store

#endif