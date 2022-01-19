type verify_sig_param = {
    dataset_id: dataset_id;
}

(**
Verify signature of a dataset cert
@return storage
*)
let verify_sig(_verify_sig_param, storage : verify_sig_param * taia_x_storage) : (operation  list) * taia_x_storage =
    // let cert : cert =  match Big_map.find_opt certify_param.dataset_id storage.certificates with
    //   | Some c -> if(c.state = cert_state.Certified) then c else (failwith("Sender is not the responsible certifier of this dataset id"))
    //   | None -> (failwith("No corresponding certificate found for this dataset id") : address)
    // in
    // let updated_certs = Big_map.update certify_param.dataset_id cert s.market.datasets in
    // ([] : operation list),  { s with certificates=updated_certs; }
    ([] : operation list),  { storage }
