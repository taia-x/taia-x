let set_cert_state (cert_param, issuer, state, certificates : cert_params * address * cert_state * cert_storage): cert_storage =
  let new_cert : cert =  match Big_map.find_opt cert_param.dataset_id certificates with
    | Some c -> ({c with issuer = (Some (issuer) : address option); signature=Some(cert_param.signature); state=state})
    | None -> (failwith("No corresponding certificate found for this dataset id") : cert)
  in 
  let cert_is_valid: bool = check_dataset_cert new_cert in
  if cert_is_valid then
    Big_map.update (cert_param.dataset_id : token_id) (Some (new_cert)) certificates
  else
    (failwith("Error: certificate is invalid") : cert_storage)

(** 
  Updates cert storage using an `update_cert_param` command.
  Helper function to implement `update_cert` entrypoint
*)
let update_cert_state (update, issuer, certificates: update_cert_param * address * cert_storage) : cert_storage =
  match update with
    | Certify cert_param -> set_cert_state (cert_param, issuer, Certified, certificates)
    | Reject cert_param -> set_cert_state (cert_param, issuer, Rejected, certificates)