(**
FA2 transfer
A list of transfer is carried out.
@return callback operation
*)

let fa2_transfer (transfers_list, storage: transfer list * taia_x_storage): (operation  list) * taia_x_storage =
    let validator = default_operator_validator in
    let (new_ledger, new_owners, new_datasets) = transfer (transfers_list, validator, storage.operators, storage.ledger, storage.market.owners, storage.market.datasets, Some(Tezos.sender)) in
    let new_storage = { storage with ledger = new_ledger; market = { storage.market with owners = new_owners; datasets=new_datasets}; }
    in
    ([] : operation list), new_storage