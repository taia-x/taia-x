(**
Update dynamic role parameter from Tezos.sender.
@return storage with updated user roles
*)
let user_manager_update_roles (updates, storage: update_roles list * nft_token_storage): (operation list) * nft_token_storage =
    let updater = Tezos.sender in
    let new_users = exec_update_role(updates, updater, storage.users) in
    ([] : operation list), { storage with users = new_users; }