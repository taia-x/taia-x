#if ! USER_MANAGER_INTERFACE
#define USER_MANAGER_INTERFACE

type role = Consumer | Certifier | Provider 

type role_param =
[@layout:comb]
{
  user : address;
  role : role;
}

type update_roles =
[@layout:comb]
  | Add_role of role_param
  | Remove_role of role_param


type user_manager_entry_points =
  | Update_roles of update_roles list

#endif