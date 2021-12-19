let transfer_bought_token (token_id, token_owner, buyer, operators, ledger, owners, datasets, emitter : token_id * address * address * operator_storage * ledger * owners * datasets * address option ) : ledger * owners * datasets =
    let token_transfer_transaction = [{from_=token_owner; txs=[{to_=buyer; token_id=token_id; amount=1n}]}] in
    let transfer_validator: operator_validator = default_operator_validator in
    let ledger_with_transferred_token, owners_with_transferred_token, datasets_with_updated_dataset: ledger * owners * datasets = transfer (token_transfer_transaction, transfer_validator, operators, ledger, owners, datasets, emitter) in
    ledger_with_transferred_token, owners_with_transferred_token, datasets_with_updated_dataset