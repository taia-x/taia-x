type mint_param = {
    owner: address;
    operator: address option;
    token_metadata_uri: bytes;
    price_arg : tez 
}
(**
Create a dataset and a token (they both have the same id), associate token to given owner, (and possibly setup an operator for this newly minted token).
Several checks are carried out: the token  must be a new token (and not an already existing token).
Only a provider, defined in the storage (market/users), can execute this entrypoint 
@return storage with new token, and operators
*)
let mint (mint_param, store : mint_param * nft_token_storage) : (operation  list) * nft_token_storage =
    if not is_role(Tezos.sender, Provider, store.users)
    then (failwith("A new token can only be minted by a provider") : (operation  list) * nft_token_storage)
    else
     
    let token_id: token_id = get_dataset_id (store) in

    // let update_sale(p, s : mint_param * nft_token_storage ) : (operation  list) * nft_token_storage =
    //     let temp_sale : sale = (token_id , p.price_arg) in
    //     let new_sale_addition : sale = Set.add temp_sale s.market.sale in
    //     ([] : operation list),  { s with market = { s.market with sales=new_sale_addition; } }
    
    let create_token_with_operator (p, s : mint_param * nft_token_storage ) : (operation  list) * nft_token_storage =
        let new_owners: owners = add_token_to_owner (token_id, p.owner, s.market.owners) in
        let ledger_with_minted_token = Big_map.add token_id p.owner s.ledger in
        let ledger_and_owners_are_consistent : bool = check_ownership_is_consistent_in_ledger_and_owners (({owner=p.owner; token_id=token_id} : ownership), ledger_with_minted_token, new_owners) in
        if ledger_and_owners_are_consistent then
            let next_dataset_id = token_id + 1n in
            
            let new_dataset = ({ isOwned=true; owner=p.owner; price=(Some (p.price_arg) : price option); onSale=true; id=token_id;  } : dataset) in
            let datasets_with_new_dataset = Big_map.add token_id new_dataset s.market.datasets in
            let datasets_ids_with_new_id = Set.add token_id s.market.datasetIds in
            
            let new_token_metadata_info = Map.literal [(("" : string), p.token_metadata_uri)] in
            let new_token_metadata = ({ token_id=token_id; token_info=new_token_metadata_info; }) in
            let token_metadata_with_new_token_metadata = Big_map.add token_id new_token_metadata s.token_metadata in

            let temp_sale : sale = ({ token_id = token_id ;price= p.price_arg }) in
            let new_sale_addition : sale set = Set.add temp_sale s.market.sales in

            match mint_param.operator with
            | None -> ([] : operation list),  { s with ledger = ledger_with_minted_token; token_metadata=token_metadata_with_new_token_metadata; market = { s.market with datasets=datasets_with_new_dataset; datasetIds=datasets_ids_with_new_id; nextDatasetId=next_dataset_id; owners=new_owners } }
            | Some(operator_address) ->
                let update : update_operator = Add_operator({ owner = p.owner; operator = operator_address; token_id = token_id; }) in
                let operators_with_minted_token_operator = update_operators (update, s.operators) in
                ([] : operation list),  { s with ledger = ledger_with_minted_token; operators = operators_with_minted_token_operator; token_metadata=token_metadata_with_new_token_metadata; market = { s.market with datasets=datasets_with_new_dataset; sales=new_sale_addition; datasetIds=datasets_ids_with_new_id; nextDatasetId=next_dataset_id; owners=new_owners; } }
        else
            (failwith("Error: cannot mint this token") : (operation  list) * nft_token_storage)
    in
    let token_owner_option : address option = Big_map.find_opt token_id store.ledger in
    match token_owner_option with
    | Some(_ownr) -> (failwith("This non-fungible token already exists"): (operation  list) * nft_token_storage)
    | None -> create_token_with_operator (mint_param, store)


