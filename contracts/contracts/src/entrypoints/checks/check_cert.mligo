let check_cert_not_set(dataset_id, s: token_id * taia_x_storage) : bool =
    match Big_map.find_opt dataset_id s.certificates with
        | Some(_c) -> false
        | None -> true

let check_cert_valid(dataset_id, s: token_id * taia_x_storage) : bool =
    match Big_map.find_opt dataset_id s.certificates with
        | Some(c) -> c.state = Certified
        | None -> false