type user_role = Consumer | Provider

type role = User of user_role | Certifier // Certifier role can not be changed

(** 
(user, role) -> unit
To manage permitted user roles
*)
type user_storage = ((address * role), unit) big_map

type role_param =
[@layout:comb]
{
  user : address;
  role : user_role;
}

type update_roles =
[@layout:comb]
  | Add_role of role_param
  | Remove_role of role_param