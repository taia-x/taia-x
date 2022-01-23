type update_user_roles_param = update_roles list

(**
Update dynamic user role parameter from Tezos.sender.
@return storage with updated user roles
*)
let update_user_roles (updates, storage: update_user_roles_param * taia_x_storage): (operation list) * taia_x_storage =
    let updater = Tezos.sender in    
    let process_update = (fun (roles, update : user_storage * update_roles) ->
      let _u = check_update_roles_params_valid (update, updater) in
      update_roles (update, roles)
    ) in
    let new_users = List.fold process_update updates storage.users in
    ([] : operation list), { storage with users = new_users; }