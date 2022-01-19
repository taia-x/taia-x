type certify_param = {
    dataset_id: token_id;
    signature: signature;
}

(**
Certify a dataset
Several checks are carried out: the sender must be registered as certifier the cert must exist for the dataset_id and the cert signature must be valid 
@return storage with modified certificates
*)
let certify(certify_param, storage : certify_param * taia_x_storage) : (operation  list) * taia_x_storage =
    let issuer: address = Tezos.sender in
    if not is_role(issuer, Certifier, storage.users)
    then (failwith("A dataset can only be certified by a certifier") : (operation  list) * taia_x_storage)
    else
      let cert : cert =  match Big_map.find_opt certify_param.dataset_id storage.certificates with
        | Some c -> c
        | None -> (failwith("No corresponding certificate found for this dataset id") : cert)
      in
      let new_cert : cert = {cert with issuer = (Some (issuer) : address option); signature=Some(certify_param.signature); state=Certified} in
      let cert_is_valid: bool = check_dataset_cert new_cert in
      if(cert_is_valid) then
        let updated_certs = Big_map.update certify_param.dataset_id (Some (new_cert)) storage.certificates in
        ([] : operation list),  { storage with certificates=updated_certs; }
      else 
        (failwith("Error: certificate is invalid") : (operation  list) * taia_x_storage)
