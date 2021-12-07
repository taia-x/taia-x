// Function that checks if an account is a Consumer role
// Must be integrated into functions that can only be used by a Consumer 
let is_consumer(u, s : address * marketplace_storage) : bool = 
    match Big_map.find_opt u s.users with
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
let is_provider(u, s: address * marketplace_storage) : bool =
    match Big_map.find_opt u s.users with
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
let is_certifier(u, s : address * marketplace_storage) : bool = 
    match Big_map.find_opt u s.users with
        | None -> False
        | Some(userRole) -> (
            match userRole with
            | Certifier -> True
            | Provider -> False
            | Consumer -> False
            | NoRole -> False
        )
