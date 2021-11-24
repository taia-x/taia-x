// Allowed roles, you can add a new annotation right here, for example 'Dev' or 'Moderator'
type role is Customer | Certifier | Provider | NoRole 

type action is
  | MakeCustomer of (address)
  | MakeCertifier of (address)
  | MakeProvider of (address)
  | RemoveRole of (address)

type store is record
  users: big_map(address, role);
end  

type return is list(operation) * store

// Function that checks if an account is an User role
// Must be integrated into functions that can only be used by an User 
function isCustomer (const addressOwner : address; var store : store) : bool is
  block {
    var isCustomer: bool := case Big_map.find_opt(addressOwner, store.users) of
      | None -> False
      | Some(userRole) ->
          case userRole of
            | Certifier -> False
            | Provider -> False
            | Customer -> True
            | NoRole -> False
          end
    end;
  } with isCustomer;

// Function that checks if an account is an Admin role
// Must be integrated into functions that can only be used by an Admin 
function isProvider (const addressOwner : address; var store : store) : bool is
  block {
    var isProvider: bool := case Big_map.find_opt(addressOwner, store.users) of
      | None -> False
      | Some(userRole) ->
          case userRole of
            | Certifier -> False
            | Provider -> True
            | Customer -> False
            | NoRole -> False
          end
    end;
  } with isProvider;

// Function that checks if an account is an Certifier role
// Must be integrated into functions that can only be used by an Admin 
function isCertifier (const addressOwner : address; var store : store) : bool is
  block {
    var isCertifier: bool := case Big_map.find_opt(addressOwner, store.users) of
      | None -> False
      | Some(userRole) ->
          case userRole of
            | Certifier -> True
            | Provider -> False
            | Customer -> False
            | NoRole -> False
          end
    end;
  } with isCertifier;

// Add/Update an account with an Certifier role
function makeCertifier (const userAddress : address; var store : store) : return is
  block {
    const newUsers : big_map(address, role) = Big_map.update(userAddress, Some(Certifier), store.users);
  } with ((nil : list (operation)), store with record [users = newUsers;]);

// Add/Update an account with an Provider role
function makeProvider (const userAddress : address; var store : store) : return is
  block {
    const newUsers : big_map(address, role) = Big_map.update(userAddress, Some(Provider), store.users);
  } with ((nil : list (operation)), store with record [users = newUsers;]);

// Add/Update an account with an Customer role
function makeCustomer (const userAddress : address; var store : store) : return is
  block {
    const newUsers : big_map(address, role) = Big_map.update(userAddress, Some(Customer), store.users);
  } with ((nil : list (operation)), store with record [users = newUsers;]);

// Remove a role to some user
function removeRole (const userAddress : address; var store : store) : return is
  block {
    const newUsers : big_map(address, role) = Big_map.update(userAddress, Some(NoRole), store.users);
  } with ((nil : list (operation)), store with record [users = newUsers;]);

function main (const action: action; var store: store): return is
  block {
    skip
  } with case action of
    | MakeCertifier(n) -> makeCertifier(n, store)
    | MakeProvider(n) -> makeProvider(n, store)
    | MakeCustomer(n) -> makeCustomer(n, store)
    | RemoveRole(n) -> removeRole(n, store)
  end;