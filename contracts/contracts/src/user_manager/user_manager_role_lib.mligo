
#if ! USER_MANAGER_ROLE_LIB
#define USER_MANAGER_ROLE_LIB

let user_manager_not_allowed = "USER_MANAGER_USER_NOT_ALLOWED" 

(** 
(user, role) -> unit
To manage permitted user roles
*)
type user_storage = ((address * role), unit) big_map

(** 
  user, role * user_storage -> unit
*)
type role_validator = (address * role * user_storage)-> unit


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



(**
Validate if role update is performed by the user himself.
*)
let validate_role_update (update, updater : update_roles * address)
    : unit =
  let role = match update with
  | Add_role role -> role
  | Remove_role role -> role
  in
  if role.user = updater then unit else failwith user_manager_not_allowed


(**
Instantiate role update by first validating the input
@param updater an address that initiated the operation; usually `Tezos.sender`.
*)
let exec_update_role (updates, updater, user_storage : update_roles list * address * user_storage) : user_storage =
    let process_update = (fun (roles, update : user_storage * update_roles) ->
      let _u = validate_role_update (update, updater) in
      update_roles (update, roles)
    ) in
    List.fold process_update updates user_storage

(**
User role check
 *)
let is_role (user, role, u_storage: (address * role * user_storage)) : bool =
      match Big_map.find_opt (user, role) u_storage with
      | None -> (failwith(user_manager_not_allowed) : bool)
      | Some _u -> true

#endif