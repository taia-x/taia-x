type buy_param = {
    token_id: token_id;
}

(**
Buy a dataset by simply transferring price (in mutez) from buyer to seller.
Several checks are carried out: the dataset must be owned by someone and must exist. The amount sent must match the dataset price
@return storage
*)
let buy(buy_parameters, storage : buy_param * taia_x_storage) : (operation  list) * taia_x_storage =
    let buyer: address = Tezos.sender in
    let price: price = Tezos.amount in

    if not is_role(buyer, User Consumer, storage.users)
    then (failwith("A dataset can only be bought by a consumer") : (operation  list) * taia_x_storage)
    else
      // check if dataset price equals Tezos.amount 
      let _dataset : dataset =  match Big_map.find_opt buy_parameters.token_id storage.market.datasets with
        | Some d -> if (d.price = (Some price: price option)) then d else (failwith("The amount sent is not equal to the price of the dataset"): dataset)
        | None -> (failwith("This dataset does not exist") : dataset)
      in
      // check if dataset is owned and if buyer is not dataset owner himself 
      let dataset_owner : address =  match Big_map.find_opt buy_parameters.token_id storage.ledger with
        | Some owner -> if (buyer = owner) then (failwith("The buyer is already the owner of this dataset"): address) else owner
        | None -> (failwith("This dataset is not owned by anyone") : address)
      in
      // check if seller address (= dataset owner) is a valid contract
      let seller : unit contract = match (Tezos.get_contract_opt dataset_owner: unit contract option) with
        | Some (contract) -> contract
        | None -> (failwith ("Dataset owner is an invalid contract") : unit contract)
      in
      let withdrawTransaction : operation = Tezos.transaction unit price seller in
      [withdrawTransaction], storage
