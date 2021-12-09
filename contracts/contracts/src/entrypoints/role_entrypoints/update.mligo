(**
Internal function to update dynamic role parameter from Tezos.sender.
@return storage with updated user roles
*)
let update_role(role_type, storage : role * nft_token_storage): (operation list) * nft_token_storage = 
    let new_users : (address, role) big_map = Big_map.update Tezos.sender (Some role_type) storage.market.users in
    let new_storage = { storage with market = { storage.market with users = new_users; } } in
    ([] : operation list), new_storage