let set_cert_state (p, issuer, state, storage : cert_params * address * cert_state * taia_x_storage): cert_storage =
  let _dataset : dataset =  match Big_map.find_opt p.dataset_id storage.market.datasets with
    | Some d -> if(d.owner = issuer) then (failwith("Dataset owner is not allowed to change his certificate state") : dataset) else (d)
    | None -> (failwith("No corresponding dataset found for this dataset id") : dataset)
  in

  let new_cert : cert =  match Big_map.find_opt p.dataset_id storage.certificates with
    | Some c -> ({c with issuer = (Some (issuer) : address option); hash=p.hash; state=state;})
    | None -> (failwith("No corresponding certificate found for this dataset id") : cert)
  in
  Big_map.update (p.dataset_id: token_id) (Some (new_cert)) storage.certificates

(**
  Updates cert storage using an `update_cert_param` command.
  Helper function to implement `update_cert` entrypoint
*)
let update_cert_state (update, issuer, storage: update_cert_param * address * taia_x_storage) : cert_storage =
  match update with
    | Certify cert_param -> set_cert_state (cert_param, issuer, Certified, storage)
    | Reject cert_param -> set_cert_state (cert_param, issuer, Rejected, storage)