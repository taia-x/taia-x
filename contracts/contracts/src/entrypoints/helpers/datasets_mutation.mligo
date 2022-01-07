// NOTE: Usage of this fn in set_new_dataset_owner throws origination error in testnet
let get_dataset_from_datasets(tokenId, datasets: token_id * datasets): dataset =
    let dataset : dataset = match Big_map.find_opt tokenId datasets with
        | Some(found_dataset) -> found_dataset
        | None -> (failwith("This dataset does not exist") : dataset)
    in
    dataset

let set_new_dataset_owner(tokenId, newOwner, datasets: token_id * address * datasets ) : datasets =
    // let dataset : dataset = get_dataset_from_datasets tokenId, datasets
    let dataset : dataset = match Big_map.find_opt tokenId datasets with
        | Some(found_dataset) -> found_dataset
        | None -> (failwith("This dataset does not exist") : dataset)
    in
    let updated_dataset : dataset = {dataset with owner = newOwner} in
    let datasets_with_updated_dataset: datasets = Big_map.update tokenId (Some(updated_dataset)) datasets in
    datasets_with_updated_dataset

let get_dataset_id (s : nft_token_storage) : token_id =
    s.market.nextDatasetId