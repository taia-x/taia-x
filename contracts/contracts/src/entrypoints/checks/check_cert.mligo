let check_dataset_not_certified(dataset_id, s: token_id * taia_x_storage) : bool =
    match Big_map.find_opt dataset_id s.certificates with
        | Some(_c) -> false
        | None -> true
