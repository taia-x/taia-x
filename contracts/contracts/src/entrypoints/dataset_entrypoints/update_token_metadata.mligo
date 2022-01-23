type update_token_metadata_param = {
    token_id: token_id;
    token_metadata_uri: bytes;
}

(**
Update the token metadata
@return storage with modified token metadata 
*)
let update_token_metadata (update_token_metadata_param, storage : update_token_metadata_param * taia_x_storage) : (operation list) * taia_x_storage =
    if not is_owner(update_token_metadata_param.token_id, Tezos.sender, storage.ledger)
    then (failwith("Only the owner of a dataset can update its token metadata") : (operation  list) * taia_x_storage)
    else
        let newTokenMetadataInfo = Map.literal [(("" : string), update_token_metadata_param.token_metadata_uri)] in
        let newTokenMetadata = ({ token_id=update_token_metadata_param.token_id; token_info=newTokenMetadataInfo; }) in
        let newTokenMetadataWithNewTokenMetadata = Big_map.update update_token_metadata_param.token_id (Some(newTokenMetadata)) storage.token_metadata in
        let newStorage : taia_x_storage = { storage with token_metadata=newTokenMetadataWithNewTokenMetadata } in
    ([] : operation list), newStorage