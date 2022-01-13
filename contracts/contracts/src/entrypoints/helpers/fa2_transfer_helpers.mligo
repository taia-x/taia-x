let exec_update_operator (updates, updater, ops_storage : update_operator list * address * operator_storage) : operator_storage =
    let process_update = (fun (ops, update : operator_storage * update_operator) ->
      let _u = validate_update_operators_by_owner (update, updater) in
      update_operators (update, ops)
    ) in
    List.fold process_update updates ops_storage

(**
Update ledger balances according to the specified transfers. Fails if any of the
permissions or constraints are violated.
@param txs transfers to be applied to the ledger
@param owner_validator function that validates of the tokens from the particular owner can be transferred.
 *)
let transfer (txs, _owner_validator, _ops_storage, ledger, owners, datasets, _emitter
          : (transfer list) * operator_validator * operator_storage * ledger * owners * datasets * address option) : ledger * owners * datasets=
  let make_transfer = (fun (l, _tx : (ledger * owners * datasets) * transfer) ->
    l
  )
  in
  let ledger_owner_and_datasets = (ledger, owners, datasets) in
  List.fold make_transfer txs ledger_owner_and_datasets