type update_token_metadata_param = {
    token_id: token_id;
    token_metadata_uri: string;
}

(**
Update the token metadata
@return storage with modified token metadata 
*)
let update_token_metadata (update_token_metadata_param, storage : update_token_metadata_param * nft_token_storage) : (operation list) * nft_token_storage =
    if not is_owner(update_token_metadata_param.token_id, Tezos.sender, storage.ledger)
    then (failwith("Only the owner of a dataset can update its token metadata") : (operation  list) * nft_token_storage)
    else
        let newTokenMetadataInfo = Map.literal [(("" : string), (Bytes.pack update_token_metadata_param.token_metadata_uri))] in
        let newTokenMetadata = ({ token_id=update_token_metadata_param.token_id; token_info=newTokenMetadataInfo; }) in
        let newTokenMetadataWithNewTokenMetadata = Big_map.update update_token_metadata_param.token_id (Some(newTokenMetadata)) storage.token_metadata in
        let newStorage : nft_token_storage = { storage with token_metadata=newTokenMetadataWithNewTokenMetadata } in
    ([] : operation list), newStorage