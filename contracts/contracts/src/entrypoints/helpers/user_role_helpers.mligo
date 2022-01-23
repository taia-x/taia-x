(** 
  Updates role storage using an `update_roles` command.
  Helper function to implement `Update_roles` entrypoint
*)
let update_roles (update, storage : update_roles * user_storage)
    : user_storage =
  match update with
  | Add_role rp -> 
    Big_map.update (rp.user, rp.role) (Some unit) storage
  | Remove_role rp -> 
    Big_map.remove (rp.user, rp.role) storage