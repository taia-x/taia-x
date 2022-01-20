(** 
  Updates cert storage using an `update_cert_param` command.
  Helper function to implement `update_cert` entrypoint
*)
let update_cert (update, storage : update_cert_param * cert_storage)
    : cert_storage =
  let process_cert = (fun (p, state, update : user_storage * update_cert_param) ->
    let new_cert : cert = {cert with issuer = (Some (iss) : address option); signature=Some(sign); state=state} in
    let cert_is_valid: bool = check_dataset_cert new_cert in
    if(cert_is_valid) then
      let updated_certs = Big_map.update certify_param.dataset_id (Some (new_cert)) storage.certificates in
      ([] : operation list),  { storage with certificates=updated_certs; }
    else 
      (failwith("Error: certificate is invalid") : (operation  list) * taia_x_storage)
  ) in
  match update with
  | Certify cp -> process_cert (cp, Certified) storage
  | Reject cp -> process_cert (cp, Rejected) storage