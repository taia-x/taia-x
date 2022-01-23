(**
User role check
 *)
let is_role (user, role, u_storage: (address * role * user_storage)) : bool =
      match Big_map.find_opt (user, role) u_storage with
      | None -> (failwith("This user is missing the necessary permissions.") : bool)
      | Some _u -> true

(**
Validate if role update params are valid: (1) update matches case and (2) update is performed by the user himself.
*)
let check_update_roles_params_valid (update, updater : update_roles * address)
    : unit =
  let role = match update with
  | Add_role role -> role
  | Remove_role role -> role
  in
  if role.user = updater then unit else failwith "Only the user himself is allowed to update his own role"
