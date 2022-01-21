#if !FA2_TAIA_X
#define FA2_TAIA_X

#include "tzip-12/fa2_interface.mligo"
#include "tzip-12/fa2_errors.mligo"
#include "tzip-12/lib/fa2_operator_lib.mligo"

#include "domain_storage/storage_definition.mligo"
#include "entrypoints/entrypoints.mligo"


type taia_x_entry_points =
    | Fa2 of fa2_entry_points
    | Mint of mint_param
    | Update_token_metadata of update_token_metadata_param
    | Buy of buy_param
    | Update_user_roles of update_user_roles_param
    | Update_certs of update_certs_param

let fa2_main (param, storage : fa2_entry_points * taia_x_storage)
    : (operation  list) * taia_x_storage =
    match param with
     | Transfer txs_michelson -> fa2_transfer(txs_michelson, storage)
     | Balance_of pm -> fa2_balance(pm, storage)
     | Update_operators updates_michelson -> fa2_update_operators(updates_michelson, storage)

let main (param, storage : taia_x_entry_points * taia_x_storage)
      : (operation  list) * taia_x_storage =
    match param with
    | Fa2 fa2 -> fa2_main (fa2, storage)
    | Mint p -> mint(p,storage)
    | Update_token_metadata p -> update_token_metadata(p, storage)
    | Buy p -> buy(p, storage)
    | Update_user_roles p -> update_user_roles(p, storage)
    | Update_certs p -> update_certs(p, storage)

#endif
