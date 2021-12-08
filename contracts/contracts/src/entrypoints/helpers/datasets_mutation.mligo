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


let set_dataset_on_sale_flag(tokenId, isOnSale, datasets: token_id * bool * datasets ) : datasets =
    let dataset : dataset = get_dataset_from_datasets(tokenId, datasets) in
    let updated_dataset : dataset = {dataset with onSale = isOnSale} in
    let datasets_with_updated_dataset: datasets = Big_map.update tokenId (Some(updated_dataset)) datasets in
    datasets_with_updated_dataset

let set_dataset_sale_flag_and_new_owner (tokenId, isOnSale, newOwner, datasets: token_id * bool * address * datasets ) : datasets =
    let dataset : dataset = get_dataset_from_datasets(tokenId, datasets) in
    let updated_dataset : dataset = {dataset with onSale = isOnSale; owner = newOwner} in
    let datasets_with_updated_dataset: datasets = Big_map.update tokenId (Some(updated_dataset)) datasets in
    datasets_with_updated_dataset

let update_price_on_sale_flag_for_a_dataset (tokenId, isOnSale, price, datasets: token_id * bool * price * datasets ) : datasets =
    let dataset : dataset =  get_dataset_from_datasets(tokenId, datasets) in
    let updated_dataset : dataset = {dataset with onSale = isOnSale; price = Some(price)} in
    let datasets_with_updated_dataset: datasets = Big_map.update tokenId (Some(updated_dataset)) datasets in
    datasets_with_updated_dataset