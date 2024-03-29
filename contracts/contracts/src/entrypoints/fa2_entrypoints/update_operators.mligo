(**
FA2 update operator
A list of operator are removed or added, for given token(s)
@return callback operation
*)
let fa2_update_operators (updates, storage: update_operator list * taia_x_storage): (operation  list) * taia_x_storage =
    let updater = Tezos.sender in
    let new_ops = exec_update_operator(updates, updater, storage.operators) in
    // let new_ops = storage.operators in
    ([] : operation list), { storage with operators = new_ops; }