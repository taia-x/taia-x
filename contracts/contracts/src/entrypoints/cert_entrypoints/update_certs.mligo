type update_certs_param = update_cert_param list

(**
Certify a dataset
Several checks are carried out: the sender must be registered as certifier the cert must exist for the dataset_id and the cert signature must be valid
@return storage with modified certificates
*)
let update_certs(updates, storage : update_certs_param * taia_x_storage) : (operation  list) * taia_x_storage =
    let issuer: address = Tezos.sender in
    if is_role(issuer, Certifier, storage.users)
    then
      let process_update = (fun (_certificates, update : cert_storage * update_cert_param) -> update_cert_state (update, issuer, storage)) in
      let new_certificates: cert_storage = List.fold process_update updates storage.certificates in
      ([] : operation list),  { storage with certificates=new_certificates; }
    else
      (failwith("A dataset can only be certified by a certifier") : (operation  list) * taia_x_storage)
