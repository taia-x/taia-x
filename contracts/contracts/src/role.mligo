#if !ROLE
#define ROLE

#include "interface.mligo"

// Function that checks if an account is a Consumer role
// Must be integrated into functions that can only be used by a Consumer 
let isConsumer(addressOwner, store : address * store) : bool = 
    match Big_map.find_opt addressOwner store.users with
        | None -> False
        | Some(userRole) -> (
            match userRole with
            | Certifier -> False
            | Provider -> False
            | Consumer -> True
            | NoRole -> False
        )
  

// Function that checks if an account is a Provider role
// Must be integrated into functions that can only be used by a Provider 
let isProvider(addressOwner, store : address * store) : bool = 
    match Big_map.find_opt addressOwner store.users with
        | None -> False
        | Some(userRole) -> (
            match userRole with
            | Certifier -> False
            | Provider -> True
            | Consumer -> False
            | NoRole -> False
        )
  


// Function that checks if an account is a Certifier role
// Must be integrated into functions that can only be used by a Certifier 
let isCertifier(addressOwner, store : address * store) : bool = 
    match Big_map.find_opt addressOwner store.users with
        | None -> False
        | Some(userRole) -> (
            match userRole with
            | Certifier -> True
            | Provider -> False
            | Consumer -> False
            | NoRole -> False
        )
  

// Add/Update an account with a Certifier role
let makeCertifier (store : store) : return = 
    let users : (address, role) big_map = Big_map.update Tezos.sender (Some Certifier) store.users in
    ([] : operation list), { store with users = users; }

// Add/Update an account with a Provider role
let makeProvider (store : store) : return = 
    let users : (address, role) big_map = Big_map.update Tezos.sender (Some Provider) store.users in
    ([] : operation list), { store with users = users; }

// Add/Update an account with a Consumer role
let makeConsumer (store : store) : return = 
    let users : (address, role) big_map = Big_map.update Tezos.sender (Some Consumer) store.users in
    ([] : operation list), { store with users = users; }

// Remove a role to some user
let removeRole (store : store) : return = 
    let users : (address, role) big_map = Big_map.update Tezos.sender (Some NoRole) store.users in
    ([] : operation list), { store with users = users; }


#endif


