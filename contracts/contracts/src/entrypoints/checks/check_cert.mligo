let check_dataset_not_certified(dataset_id, s: token_id * taia_x_storage) : bool =
    match Big_map.find_opt dataset_id s.certificates with
        | Some(_c) -> false
        | None -> true

let check_dataset_cert(c: cert) : bool =
    match c.signature with
        | Some(sig) -> Crypto.check c.provider_pbk sig c.root_hash
        | None -> false    
